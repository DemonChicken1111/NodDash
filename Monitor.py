import json
import yaml
import datetime
from time import sleep
import os

def getFilesToCompare():

    #Opens Config file
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

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
        print("Differences found in the following keys:")
        for key, values in differences.items():
            print(f"{key}: File 1 - {values['file1']}, File 2 - {values['file2']}")
    else:
        print("No differences found in the specified keys.")

#keysToCompare = ["key1", "key2", "key3"]  # Add the keys you want to compare
def main():

    #for i in range(len(getFileValues())):
    compareJSONFilesWithKeys(getFileValues()['1'][0], getFileValues()['1'][1], "ephemeralInventoryList")

if __name__ == "__main__":
    main()