import sys
import psutil
import datetime
from os.path import dirname, join, isdir
from model import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication
from PyQt5.QtCore import QTimer

from utils.functions import *

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None, configsFile=None):
		super(MainWindow, self).__init__(parent)

		self.configsFile = configsFile

		if not self.configsFile:
			self.configsFile = join(dirname(__file__), "configs.json")
		print(self.configsFile)
		self.configs = loadJsonFile(self.configsFile)

		self.setupUi(self)
		self.setFixedSize(600, 347)

		self.subprocess = None
		self.isInifityDuration = False
		self.isRunning = False
		self.startDate = None
		self.endDate = None
		self.timer = QTimer()

		self.setupComponents()
		self.setFieldsConstraint()
		self.setEvents()


	def setupComponents(self):
		self.durationDescriptionField.addItems(["sec", "min", "hours", "oo"])
		self.durationDescriptionField.setCurrentText("oo")

		outputDir = self.configs.get("outputDirectory")
		duration = self.configs.get("duration")
		accuracy = self.configs.get("accuracy")
		dateStartIsoFormat = self.configs.get("dateStart")
		motionstrackerPid = self.configs.get("motionstrackerPid")
		outputFormat = self.configs.get("outputFormat")


		if outputDir:
			self.dirField.setText(outputDir)

		if duration:
			if duration == "oo":
				self.durationDescriptionField.setCurrentText("oo")
				self.setActivateBtnActivationStyle()
			else:
				# duration: 13m (example)
				durationValue = int(duration[:-1]) # 13
				durationDescription = duration[-1] # "m"

				if durationDescription == "m":
					durationDescription = "min"
				elif durationDescription == "s":
					durationDescription = "sec"
				elif durationDescription == "h":
					durationDescription = "hours"
				else:
					durationDescription = "oo"

				self.durationDescriptionField.setCurrentText(durationDescription)
				self.durationField.setValue(durationValue)

				if dateStartIsoFormat:
					self.updateDates(
						datetime.datetime.fromisoformat(dateStartIsoFormat), 
						durationValue, 
						durationDescription
					)

			try:
				self.subprocess = psutil.Process(motionstrackerPid)
			except Exception as e:
				# print(e)
				self.setActivateBtnDeactivationStyle()
			else:
				self.setActivateBtnActivationStyle()
				self.timer.start(1000)
				

		if accuracy:
			self.accuracyField.setValue(accuracy)

		if outputFormat == "video":
			self.imagesRadioButton.setChecked(False)
			self.videoRadioButton.setChecked(True)
		else:
			self.imagesRadioButton.setChecked(True)
			self.videoRadioButton.setChecked(False)

	def setFieldsConstraint(self):
		self.durationField.setRange(1, 100)
		self.accuracyField.setRange(0, 1)

	def setEvents(self):
		self.activateButton.clicked.connect(self.handleClickOnActivateBtn)
		self.chooseButton.clicked.connect(self.handleClickOnChooseBtn)
		self.durationDescriptionField.activated.connect(self.handleClickOnDescriptionCbox)
		self.timer.timeout.connect(self.timerEventCallback)

	def timerEventCallback(self):
		if not self.endDate:
			return

		nowDate = datetime.datetime.now()

		if self.endDate <= nowDate:
			self.setActivateBtnDeactivationStyle()
			self.timer.stop()

	def handleClickOnDescriptionCbox(self):
		desc = self.durationDescriptionField.currentText()

		if desc == "oo":
			self.durationField.setEnabled(False)
		else:
			self.durationField.setEnabled(True)

	def handleClickOnChooseBtn(self):
		# choose directory

		outputDirectory = QFileDialog.getExistingDirectory(self)

		if outputDirectory:
			self.dirField.setText(outputDirectory)

	def handleClickOnActivateBtn(self):
		# print(self.isRunning, "click")
		if not self.isRunning:
			self.activate()
		else:
			self.deactivate()

	def activate(self):
		directory = self.dirField.text()
		durationValue = self.durationField.value()
		accuracy = self.accuracyField.value()
		outputFormat = ""

		if self.imagesRadioButton.isChecked():
			outputFormat = "images"
		else:
			outputFormat = "video"

		command = [
			sys.executable, # python executable 
			"/home/ridoineel/Dev/motions-tracker/src/motionstracker", 
			"-o", directory, 
			"-ac",  str(accuracy),
			"-f", outputFormat
		]

		durationDescription = self.durationDescriptionField.currentText()

		if durationDescription == "oo":
			self.isInifityDuration = True
		else:
			command += ["-d", str(durationValue) + durationDescription[0]]
		
		try:
			# print(command)
			self.subprocess = psutil.Popen(command)
		except Exception as e:
			print(e)
		else:
			# start timer
			self.timer.start(1000)

			# set start date and end date
			# and update activateButton style

			self.updateDates(datetime.datetime.now(), durationValue, durationDescription)
			self.setActivateBtnActivationStyle()


			# update configuration file

			if durationDescription == "oo":
				self.configs["duration"] = "oo"
			else:
				self.configs["duration"] = str(durationValue) + durationDescription[0]

			if isdir(directory):
				self.configs["outputDirectory"] = directory

			self.configs["dateStart"] = datetime.datetime.now().isoformat()

			self.configs["accuracy"] = float(accuracy)
			self.configs["outputFormat"] = outputFormat
			self.configs["motionstrackerPid"] = self.subprocess.pid

			updateJsonFile(self.configsFile, self.configs)

	def deactivate(self):
		if self.subprocess:
			print("terminate")
			self.subprocess.terminate()

			
		self.setActivateBtnDeactivationStyle()

	def setActivateBtnActivationStyle(self):
		self.activateButton.setStyleSheet("background: green; color: black")
		self.activateButton.setText("DEACTIVATE")
		self.isRunning = True

		if self.startDate == None or self.endDate == None:
			durationDescription = self.durationDescriptionField.currentText()
			self.updateDates(datetime.datetime.now(), self.durationField.value(), durationDescription)


		# update dates labels
		if self.startDate == None:
			self.startDateLabel.setText("...")
		else:
			self.startDateLabel.setText(self.startDate.isoformat().replace("T", " "))

		if self.endDate == None:
			self.endDateLabel.setText("...")
		else:
			self.endDateLabel.setText(self.endDate.isoformat().replace("T", " "))

		
	def setActivateBtnDeactivationStyle(self):
		self.activateButton.setStyleSheet("background: orange; color: black")
		self.activateButton.setText("ACTIVATE")
		self.isRunning = False

		self.startDateLabel.setText("...")
		self.endDateLabel.setText("...")

	def updateDates(self, startDate, durationValue, durationDescription):
		""" update start date and
			end date

		"""	

		self.startDate = startDate
		self.endDate = None
		durationSeconds = self.getDuration(durationValue, durationDescription)

		if durationSeconds:
			self.endDate = self.startDate + datetime.timedelta(seconds=durationSeconds)

	def getDuration(self, durationValue, durationDescription):
		""" get duration (second) 
			with duration integer and duration description

		"""

		durationSeconds = None

		if durationDescription != "oo":
			dd = durationDescription[0]

			if dd == "s":
				durationSeconds = durationValue
			elif dd == "m":
				durationSeconds = durationValue * 60
			else:
				durationSeconds = durationValue * 3600

		
		return durationSeconds


	def closeEvent(self, event):
		pass

def main():
	app = QApplication(sys.argv)

	configsFile = join(dirname(__file__), "assets/configs.json")

	mainWindow = MainWindow(configsFile=configsFile)
	mainWindow.show()

	app.exec_()

if __name__ == '__main__':
	main()