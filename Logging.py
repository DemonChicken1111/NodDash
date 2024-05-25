import yaml
import requests
import JSONImporter
import threading
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

	for i in range(len(fileNames)):
		logFile.write(fileNames[i][:25] + ": " + fileNames[i][25:] + " added \n")


def main():
	
	Logger()`

if __name__ == "__main__":
	main()