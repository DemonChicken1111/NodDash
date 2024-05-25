import yaml
import JSONImporter
import datetime
from time import sleep
from os import walk

#Opens Config file
with open("config.yaml", "r") as file:
	config = yaml.safe_load(file)

x = datetime.datetime.now()

#Set in loop
	#Imports Data and attaches time stamp to file. Executes every x seconds
def JSONStreamer():

	for i, obj in config.items():
		for y in obj:
			fileName = x.strftime("%c") + " " + obj[y]
			JSONImporter.ImportJSONFile(fileName, obj[y])

#Creates human readable log of import
def Logger():

	logFile = open("log.txt", "a")
	fileNames = next(walk("JSON/"), (None, None, []))[2]

	with open("log.txt", "r") as log:
		readLog = log.read()

	#print(readLog.splitlines()[0])


	#Broken
	for i in range(len(fileNames)):
		for o in range(len(readLog.splitlines())):
			compare = fileNames[i][:25] + ": " + fileNames[i][25:] + " added "
			
			if compare == readLog.splitlines()[o]:
				print("Already exists")
				#logFile.write(fileNames[i][:25] + ": " + fileNames[i][25:] + " added \n")
			else:
				print("in else")

	logFile.close()
	readLog.close()

			

def main():
	Logger()

if __name__ == "__main__":
	main()