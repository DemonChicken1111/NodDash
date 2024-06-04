from tinydb import TinyDB, Query
import json 
import yaml
import JSONImporter

db = TinyDB('db.json')

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# What does this need to do?
# Take in user supplied key values from config
# For every file, find the values, and insert into db (Checks if exists already)

def databaseWrite():

