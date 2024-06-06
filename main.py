import Monitor
import JSONImporter
import Logging
import Cleanup
#import DBase
import threading
from time import sleep
import datetime


def current24HrTime():
	t = datetime.datetime.now()
	return t.strftime("%H:%M")

def MonitorJob():

	while True:
		Monitor.main()
		sleep(30)

def LogJob():

	while True:
		Logging.main()

#def DBaseJob():
#
#	while True:		
#		DBase.main():

def DelJob():

	if current24HrTime() == "00:00":
		sleept(30)
		Cleanup.Clean()

def GUIJob():

	print("Add the GUI")

def main():

	thread1 = threading.Thread(target=MonitorJob)
	thread2 = threading.Thread(target=LogJob)
	thread3 = threading.Thread(target=DelJob)
	thread4 = threading.Thread(target=GUIJob)

	thread1.start()
	thread2.start()
	thread3.start()
	thread4.start()

	thread1.join()
	thread2.join()
	thread3.join()
	thread4.join()

if __name__ == "__main__":
	main()

