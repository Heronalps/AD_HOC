import json
from pprint import pprint

with open('newFULProject.json') as data_file:    
    data = json.load(data_file)

#pprint(data["changelog"]["histories"][1])
for issue in data["issues"]:
	for obj in issue["changelog"]["histories"]:
		if (obj["items"][0]["fromString"] == "Task") and (obj["items"][0]["toString"] == "Defect"):
		 	print issue["key"]
