import json
import yaml
import datetime
from time import sleep

def getFilesToCompare():
	
#Generic implementation. Will specialize and utilize later

def compareJSONFilesWithKeys(file1_path, file2_path, keys_to_compare):

    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        json1 = json.load(file1)
        json2 = json.load(file2)

    differences = {}
    for key in keys_to_compare:
        if json1.get(key) != json2.get(key):
            differences[key] = {"file1": json1.get(key), "file2": json2.get(key)}

    if differences:
        print("Differences found in the following keys:")
        for key, values in differences.items():
            print(f"{key}: File 1 - {values['file1']}, File 2 - {values['file2']}")
    else:
        print("No differences found in the specified keys.")

# Example usage:
keys_to_compare = ["key1", "key2", "key3"]  # Add the keys you want to compare
compareJSONFilesWithKeys("file1.json", "file2.json", keys_to_compare)