import subprocess
import requests 
from sys import stdout
import json

# Remnants of failed attempt to import api_url from speed_test_stack
#from speed_test_stack import api_url

# Command to run speedtest from local machine and output JSON file
command = [r"speedtest-cli", "--json"]
output = subprocess.run(command, capture_output=True, text=True)

# Saves output to a string, then creates a dictionary. TODO: add in some error handling here. If error code or no valid output etc...
jsonResults = str(output.stdout)
results = json.loads(jsonResults)

dictResults = {
    "timestamp": (results['timestamp']),
    "download": (results['download']),
    "upload": (results['upload']),
    "ping": (results['ping']),
    "serverName": (results['server']['name']),
    "serverCountry": (results['server']['country'])
}

print(dictResults)
    

#TODO: grab relevant data from speedtest json results. Make variable or pare down JSON to relevant info. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.LowLevelAPI.html

# POST request to API
# TODO: See note in speed_test_stack
api_url= "https://dpjwnub3z5.execute-api.us-east-1.amazonaws.com/prod/"
requests.post(api_url, data=dictResults) # add json={key: value} and other needed args later. 
