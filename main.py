import Monitor
import JSONImporter
import Logging
import Cleanup
#import DBase
import threading
from time import sleep
import datetime
from colorama import Fore, Back, Style
import os
from random import randrange

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

	Logo = """

	==============================================

	 _   _           _ _____            _     
	| \\ | |         | |  __ \\          | |    
	|  \\| | ___   __| | |  | | __ _ ___| |__  
	| . ` |/ _ \\ / _` | |  | |/ _` / __| '_ \\ 
	| |\\  | (_) | (_| | |__| | (_| \\__ \\ | | |
	|_| \\_|\\___/ \\__,_|_____/ \\__,_|___/_| |_|
	                                          
	           Welcome to the unknown                           
	==============================================

	"""

	Exit = "To EXIT: Press CTRL + Z or CTRL + C"

	ascii_1 = """
here is a bunny

{\\__/}
( • - •)
 🖋< \\ ⠀⠀
	"""

	ascii_2 = """
 (\\  (\\
(„• ֊ •„)   <(Hello...)
━O━O━━━━━
	"""


	os.system('cls' if os.name == 'nt' else 'clear')
	print(Fore.BLUE + Logo)
	print(Fore.YELLOW + Exit + "\n")
	print(Style.RESET_ALL)

	while True:
		randomSleep = randrange(200)
		if randomSleep > 100: 
			print(Fore.WHITE + ascii_1)
		else: 
			print(Fore.WHITE + ascii_2)
		print(Style.RESET_ALL)
		sleep(randomSleep)

def main():

	thread4 = threading.Thread(target=GUIJob)
	thread1 = threading.Thread(target=MonitorJob)
	thread2 = threading.Thread(target=LogJob)
	thread3 = threading.Thread(target=DelJob)

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

