import sys
import subprocess
import os               
import time

def executeSomething():
    # This setting is very important to avoid errors 
    os.environ['PYTHONIOENCODING'] = 'utf-8'    #setting the sys environment, or we will get unicoden error
    
    file_1 = "TwitterDownloader_National.py"   # put the file you want to run simultanously
   
    try:  
        proc = subprocess.Popen([sys.executable,file_1])
        proc.wait()   
    except AttributeError:
        pass 
    time.sleep(61)   #Wait for 60 sec.

while True:
    executeSomething()               