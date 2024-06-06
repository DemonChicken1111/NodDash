import json
import yaml
import datetime
from time import sleep
import os
import Logging
from tinydb import TinyDB, Query

db = TinyDB('pingdb.json')
x = datetime.datetime.now()

#Opens Config file
with open("configMonitor.yaml", "r") as fileMon, open("config.yaml", "r") as file:
    configMonitor = yaml.safe_load(fileMon)
    config = yaml.safe_load(file)


def getFilesToCompare():

    #Get files, and apppend to outputList
    outputList = []
    for root, dirs, files in os.walk("JSON/"):
        for f in files:
            outputList.append(os.path.join(root, f))
            #print(f)
        break

    #Sort list so newest times in front
    outputList.sort()
    outputList = outputList[::-1]

    #Create cut off length for list so we can compare 2 newest files of same deployable.
    cutOffLength = len(config["deployables"]) * 2

    return outputList[:cutOffLength]

def getFileValues():

    outputList = []
    outputDict = {}
    count = 0
    for i in range(len(getFilesToCompare())):
        for j in range(i+1, len(getFilesToCompare())):
            if getFilesToCompare()[i][24:] == getFilesToCompare()[j][24:]:
                count += 1
                outputList.append(getFilesToCompare()[i])
                outputList.append(getFilesToCompare()[j])
                outputDict[str(count)] = outputList
                outputList = []

    #print(outputDict)

    return outputDict


#Generic implementation. Will specialize and utilize later
def compareJSONFilesWithKeys(fileOnePath, fileTwoPath, keysToCompare):

    with open(fileOnePath, 'r') as file1, open(fileTwoPath, 'r') as file2:
        json1 = json.load(file1)
        json2 = json.load(file2)

    differences = {}
    for key in keysToCompare:
        if json1.get(key) != json2.get(key):
            differences[key] = {"file1": json1.get(key), "file2": json2.get(key)}

    if differences:
        Logging.customLogging("Differences found in the following keys:", False)
        for key, values in differences.items():
            Logging.customLogging(f" {key}: {fileOnePath[30:37]}, {fileTwoPath[30:37]}", True)

            location = json1.get("solarSystem").get("solarSystemName")
            time = x.strftime("%c")
            amount = 1

            #Could be issue if multiple empheralInventories are opened between intervals
            #Seems to be edge case though and willing to allow it for sake of time
            db.insert({'time': time, 'location': location, 'key': key, 'amount': amount})


    else:
        Logging.customLogging(f"No differences found in the specified keys. {fileOnePath[30:37]}", True)

def main():

    keysToCompare = [] 
    for i, obj in configMonitor['keyvalues'].items():
        keysToCompare.append(obj)

    inputDict = getFileValues()

    for key, val in inputDict.items():
        compareJSONFilesWithKeys(val[0], val[1], keysToCompare)

if __name__ == "__main__":
    main()