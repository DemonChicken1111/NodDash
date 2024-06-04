import yaml
import JSONImporter
import datetime
from time import sleep
import threading

	
#Opens Config file
with open("config.yaml", "r") as file:
	config = yaml.safe_load(file)

t = datetime.datetime.now()
logging = ""

def currentTime():
		return t.strftime("%c")

class Logger():

	#Imports Data and attaches time stamp to file. Executes every x seconds
	def JSONStreamer():

		for i, obj in config.items():
			for y in obj:
				fileName = currentTime() + " " + obj[y]
				JSONImporter.ImportJSONFile(fileName, obj[y])
		
		global logging
		logging = "Smart Deployables Fetched"

	def LoggingJSONFetch(): 

		global logging
		logFile = open("log.txt", "a")
		logEntry = logging

		if logEntry != "":
			logFile.write(logEntry + ": " + t.strftime("%c") + "\n")
			#print("logged")
			pass
		else:
		#	print(logEntry + "else")
			pass

		logging = ""

def customLogging(thingToLog, newLine):

	logFile = open("log.txt", "a")
	logEntry = thingToLog

	if logEntry == "":
		pass
	if newLine == True:
		logFile.write(logEntry + "\n")
	else:
		logFile.write(logEntry)

def streamTask(lock):
	#Task for a thread, Calls JSONStreamer every 10 seconds

	while True:
		lock.acquire()
		Logger.JSONStreamer()
		lock.release()
		print("Sleeping..")
		sleep(30)
		print("Starting..")
		

def logTask(lock):
	#Task for a thread, Calls LoggingJSONFetch function
	
	while True:
		lock.acquire()

		if threading.current_thread().name != "thread1":
			Logger.LoggingJSONFetch()
			lock.release()

def main():

	global logging

	logging = ""

	Logs = Logger()
	lock = threading.Lock()

	thread1 = threading.Thread(target=streamTask, args=(lock,))
	thread2 = threading.Thread(target=logTask, args=(lock,))

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

if __name__ == "__main__":
	main()