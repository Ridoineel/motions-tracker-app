# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/model.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 347)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background: #eee;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.activateButton = QtWidgets.QPushButton(self.centralwidget)
        self.activateButton.setGeometry(QtCore.QRect(190, 200, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        self.activateButton.setFont(font)
        self.activateButton.setStyleSheet("background: orange;")
        self.activateButton.setObjectName("activateButton")
        self.dirField = QtWidgets.QLineEdit(self.centralwidget)
        self.dirField.setEnabled(False)
        self.dirField.setGeometry(QtCore.QRect(340, 21, 161, 31))
        self.dirField.setObjectName("dirField")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 141, 31))
        self.label.setStyleSheet("color: #444;")
        self.label.setObjectName("label")
        self.chooseButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseButton.setGeometry(QtCore.QRect(510, 21, 61, 31))
        self.chooseButton.setObjectName("chooseButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 70, 141, 31))
        self.label_2.setStyleSheet("color: #444;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 110, 141, 31))
        self.label_3.setStyleSheet("color: #444;")
        self.label_3.setObjectName("label_3")
        self.durationField = QtWidgets.QSpinBox(self.centralwidget)
        self.durationField.setGeometry(QtCore.QRect(340, 71, 91, 26))
        self.durationField.setObjectName("durationField")
        self.durationDescriptionField = QtWidgets.QComboBox(self.centralwidget)
        self.durationDescriptionField.setGeometry(QtCore.QRect(440, 71, 61, 25))
        self.durationDescriptionField.setCurrentText("")
        self.durationDescriptionField.setObjectName("durationDescriptionField")
        self.accuracyField = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.accuracyField.setGeometry(QtCore.QRect(340, 111, 161, 26))
        self.accuracyField.setProperty("value", 1.0)
        self.accuracyField.setObjectName("accuracyField")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -10, 151, 471))
        self.frame.setStyleSheet("background: #1F1F1F;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: orange;\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #aaa;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 280, 81, 17))
        self.label_6.setStyleSheet("color: #444;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 300, 81, 17))
        self.label_7.setStyleSheet("color: #444;")
        self.label_7.setObjectName("label_7")
        self.startDateLabel = QtWidgets.QLabel(self.centralwidget)
        self.startDateLabel.setGeometry(QtCore.QRect(280, 280, 221, 17))
        self.startDateLabel.setObjectName("startDateLabel")
        self.endDateLabel = QtWidgets.QLabel(self.centralwidget)
        self.endDateLabel.setGeometry(QtCore.QRect(280, 300, 221, 17))
        self.endDateLabel.setObjectName("endDateLabel")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(190, 150, 141, 31))
        self.label_8.setStyleSheet("color: #444;")
        self.label_8.setObjectName("label_8")
        self.imagesRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.imagesRadioButton.setGeometry(QtCore.QRect(340, 150, 81, 23))
        self.imagesRadioButton.setChecked(True)
        self.imagesRadioButton.setAutoExclusive(True)
        self.imagesRadioButton.setObjectName("imagesRadioButton")
        self.videoRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.videoRadioButton.setGeometry(QtCore.QRect(440, 150, 81, 23))
        self.videoRadioButton.setChecked(False)
        self.videoRadioButton.setObjectName("videoRadioButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MotionsTracker"))
        self.activateButton.setText(_translate("MainWindow", "ACTIVATE"))
        self.label.setText(_translate("MainWindow", "Output Directory"))
        self.chooseButton.setText(_translate("MainWindow", "Choose"))
        self.label_2.setText(_translate("MainWindow", "Duration"))
        self.label_3.setText(_translate("MainWindow", "Accuracy"))
        self.label_4.setText(_translate("MainWindow", "MotionsTracker"))
        self.label_5.setText(_translate("MainWindow", "@RidoineEl"))
        self.label_6.setText(_translate("MainWindow", "start date :"))
        self.label_7.setText(_translate("MainWindow", "end date   :"))
        self.startDateLabel.setText(_translate("MainWindow", "..."))
        self.endDateLabel.setText(_translate("MainWindow", "..."))
        self.label_8.setText(_translate("MainWindow", "Format"))
        self.imagesRadioButton.setText(_translate("MainWindow", "Images"))
        self.videoRadioButton.setText(_translate("MainWindow", "Video"))
