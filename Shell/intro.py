import os 
import subprocess

x = subprocess.Popen(['xyz']) 

print(x) 
print(x.poll()) 
print(x.returncode) 

