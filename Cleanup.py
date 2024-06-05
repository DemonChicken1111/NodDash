import os
import Logging
import datetime

t = datetime.datetime.now()

def currentTime():
		return t.strftime("%c")

def Clean():

	#os.walk and search for yesterdays files
	filePath = []
	for root, dirs, files in os.walk("JSON/"):
		for f in files:
			filePath.append(os.path.join(root, f))
		break

	#print(filePath)

	cleaned = False
	cT = currentTime()

	for i in range(len(filePath)):
		if filePath[i][5:15] != cT[:10]:
			if os.path.exists(filePath[i]):
				os.remove(filePath[i])
				cleaned = True
			else:
				Logging.customLogging(f"{filePath[i]} doesn't exist", True)
		else: 
			pass

	if cleaned == True:
		Logging.customLogging("Files cleaned", True)
		cleaned = False

	#For every file from yesterday
	#for 
	#	if os.path.exists(filePath):
	#		os.remove(filePath)
	#		Logging.customLogging("Files cleaned up")


Clean()
