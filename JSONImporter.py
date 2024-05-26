import json
import requests

#Define Base URLs to access blockchain data
baseURL = "https://blockchain-gateway-test.nursery.reitnorf.com/"
smartDeployableURL = "smartdeployables/"
typeURL = "types/"

def ImportJSONFile(FileName, ID):

	URLAddon = smartDeployableURL 
	#print("Getting:" + ID[:5])

	r = requests.get(baseURL+URLAddon+ID)
	request = r.json()
	
	with open("JSON/" + FileName + ".json", "w") as outfile:
		outfile.write(json.dumps(request, indent=4))

