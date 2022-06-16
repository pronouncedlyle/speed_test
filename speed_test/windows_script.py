import subprocess
import requests 
from sys import stdout

# Remnants of failed attempt to import api_url from speed_test_stack
#from speed_test_stack import api_url

# Command to run speedtest from local machine adn output JSON file
command = [r"speedtest-cli", "--json"]
output = subprocess.run(command, capture_output=True, text=True)
#print(output)
#print(output.stdout)

#TODO: grab relevant data from speedtest json results. Make variable or pare down JSON to relevant info. https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.LowLevelAPI.html

# POST request to API
# TODO: This will not work if deployed again. Need to update url with each deployment
# How to pass in url from stack? See note in speed_test_stack
apiurl= "https://dpjwnub3z5.execute-api.us-east-1.amazonaws.com/prod/"
#print(apiurl)
requests.post(apiurl) # add json={key: value} and other needed args later. 