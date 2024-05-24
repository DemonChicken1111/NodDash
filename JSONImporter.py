import json
import requests

BaseURL = "https://blockchain-gateway-test.nursery.reitnorf.com/"
SmartDeployableURL = "smartdeployables/"
TypeURL = "types/"

def ImportJSONFile(FileName, URLParam, ID):

	if URLParam == "-S":
		URLAddon = SmartDeployableURL 
	if URLParam == "-T":
		URLAddon = TypeURL 	
	else:
		print(URLParam + " is not a vaild parameter.")

	r = requests.get(BaseURL+URLAddon+ID)
	request = r.json()
	
	with open(FileName, "w") as outfile:
		outfile.write(json.dumps(request, indent=4))

