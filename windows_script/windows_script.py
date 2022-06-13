import subprocess
from sys import stdout

#output = subprocess.run(['cd'], input= r'C:\Users\hmalisle\speed_test', capture_output=True, shell=True, text=True)
#print(output)
#print(output.stdout)

output2 = subprocess.run(['speedtest-cli'], capture_output=True, shell=True, text=True)
#print(output2)
print(output2.stdout)


#CLI to execute:
#