import subprocess
from sys import stdout

#executes cd to the specified file. TODO: Do I need to do the cd first? This doesn't transfer well
#output = subprocess.run(['cd'], input= r'C:\Users\hmalisle\speed_test', capture_output=True, shell=True, text=True)
#prints what's going on behind the scenes
#print(output)
#prints specifically the output from the command
#print(output.stdout)

#this will correctly run the speedtest-cli but I can't seem to get follow-on arguments to work like --simple or --server
command = [r"speedtest-cli", "--json"]
output2 = subprocess.run(command, capture_output=True, text=True)
print(output2)
print(output2.stdout)

# command to execute: speedtest-cli --json

#TODO: grab relevant data from speedtest json results. Figure out which data type would be easiest to send to dynamodb https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.LowLevelAPI.html

#TODO: write a post method to API gateway https://github.com/aws-samples/aws-cdk-examples/tree/master/python/api-sqs-lambda