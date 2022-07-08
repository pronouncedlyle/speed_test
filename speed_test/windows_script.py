import subprocess
import requests 
from sys import stdout
import json

# Remnants of failed attempt to import api_url from speed_test_stack
#from speed_test_stack import api_url

# Command to run speedtest from local machine and output JSON file
command = [r"speedtest-cli", "--json"]
output = subprocess.run(command, capture_output=True, text=True)

# Saves output to a string TODO: add in some error handling here. If error code or no valid output etc...
jsonRawResults = str(output.stdout)
# creates python dictionary from json string to pull and format relevant data
results = json.loads(jsonRawResults)

# Creates new python dictionary with only relevant data TODO: this is possibly the best place to format the upload / download speed numbers from bits to mb/s.
dictResults = {
    "timestamp": (results['timestamp']),
    "download": (results['download']),
    "upload": (results['upload']),
    "ping": (results['ping']),
    "serverName": (results['server']['name']),
    "serverCountry": (results['server']['country'])
}

# takes cleaned-up python dictionary and puts it back in json string format (redundant?)
jsonResults = json.dumps(dictResults)
print(jsonResults)
    
# POST request to API
# TODO: 1. Dynamically populate API url without hard-coding it in. See note in speed_test_stack
api_url= "https://dpjwnub3z5.execute-api.us-east-1.amazonaws.com/prod/"
# TODO: How to correctly pass jsonResults to API GW so lambda function can consume it?
requests.post(api_url, data=jsonResults)
