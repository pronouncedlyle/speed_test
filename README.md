Speed Test:

This is a simple project I started to get familiar with CDK and some basic AWS services. 

The purpose is to run an internet connection speed test provided by the SpeedTest CLI from the user's local machine,
then send selected data to DynamoDB for the user's record. 

CURRENT STATE: The windows_script.py works as intended, but at this point the POST request will simply trigger 
the API gateway and lambda function, writing a hard-coded piece of text into the DynamoDB table. 
I still need to set up the API gateway, lambda function, and DDB table to correctly handle 
the JSON documents with the speed test data.

![Alt text](speed_test_diagram.jpg?raw=true "speed_test_diagram")