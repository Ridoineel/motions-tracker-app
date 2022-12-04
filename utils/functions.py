import json

def loadJsonFile(file_path):
	content = ""

	with open(file_path, "r") as file:
		content = json.load(file)

	return content

def createJsonFile(file_path, content):

	with open(file_path, "w") as file:
		json.dump(content, file)

	return content

def updateJsonFile(file_path, content):
	return createJsonFile(file_path, content)
