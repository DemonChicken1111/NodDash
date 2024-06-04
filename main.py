import Monitor
import JSONImporter
import Logging
#import DBase
import threading
from time import sleep


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

def main():

	thread1 = threading.Thread(target=MonitorJob)
	thread2 = threading.Thread(target=LogJob)

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

if __name__ == "__main__":
	main()

