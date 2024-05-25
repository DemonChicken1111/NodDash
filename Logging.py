import yaml
import JSONImporter
import datetime
from time import sleep
from os import walk
import functools
from itertools import zip_longest
import threading

#Opens Config file
with open("config.yaml", "r") as file:
	config = yaml.safe_load(file)

t = datetime.datetime.now()

#Set in loop
	#Imports Data and attaches time stamp to file. Executes every x seconds
def JSONStreamer():

	for i, obj in config.items():
		for y in obj:
			fileName = t.strftime("%c") + " " + obj[y]
			JSONImporter.ImportJSONFile(fileName, obj[y])

#Creates human readable log of import
def Logger():

	logFile = open("log.txt", "a")
	fileNames = next(walk("JSON/"), (None, None, []))[2]

	with open("log.txt", "r") as log:
		readLog = log.read()

	logList = readLog.splitlines()

	fileNames.sort()
	logList.sort()

	#print(logList)
	#print(fileNames)

	#Broken
	for i,(f, l) in enumerate(zip_longest(fileNames, logList)):
		
		if (f[i][:25] + ": " + f[i][25:] + " added ") != l[i]:
			print("writing new file")
			#logFile.write(fileNames[i][:25] + ": " + fileNames[i][25:] + " added \n")
		if (f[i][:25] + ": " + f[i][25:] + " added ") == l[i]:
			print("Already exists")
				

	logFile.close()
	readLog.close()

			

def main():
	
	thread1 = threading.Thread(target=Logger)
	thread2 = threading.Thread()

	t1.start()
	t1.join()

if __name__ == "__main__":
	main()