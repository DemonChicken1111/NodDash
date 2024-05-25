import yaml
import requests
import JSONImporter
import threading
import datetime
from time import sleep


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



JSONStreamer()