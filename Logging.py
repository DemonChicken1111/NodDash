import yaml
import JSONImporter
import datetime
from time import sleep
from os import walk
import threading

	
#Opens Config file
with open("config.yaml", "r") as file:
	config = yaml.safe_load(file)

t = datetime.datetime.now()

class Logger():

	def __init__(self):
		self.logging = ""

		
	#Imports Data and attaches time stamp to file. Executes every x seconds
	def JSONStreamer(self):

		for i, obj in config.items():
			for y in obj:
				fileName = t.strftime("%c") + " " + obj[y]
				JSONImporter.ImportJSONFile(fileName, obj[y])
		
		self.logging = "File fetched"

	def Logging(self): #Still wont work :(

		logFile = open("log.txt", "a")
		logEntry = self.logging

		if logEntry != "":
			logFile.write(logEntry)
			print("logged")
		else:
			print(logEntry + "else")
			pass


def streamTask(lock):
	#Task for a thread, Calls JSONStreamer every 10 seconds

	while True:
		lock.acquire()
		Logger().JSONStreamer()
		lock.release()
		print("Sleeping..")
		sleep(10)
		

def logTask(lock):
	#Task for a thread, Calls Logging function

	while True:
		lock.acquire()
		Logger().Logging()
		lock.release()

def main():
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