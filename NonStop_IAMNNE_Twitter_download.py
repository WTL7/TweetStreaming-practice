import sys
import subprocess
import os               
import time

def executeSomething():
    # This setting is very important to avoid errors 
    os.environ['PYTHONIOENCODING'] = 'utf-8'    #setting the sys environment, or we will get unicoden error
    
    file_2 = "TwitterDownloader_IA_MN_NE.py"   # put the file you want to run simultanously
   
    try:  
        proc = subprocess.Popen([sys.executable,file_2])
        proc.wait()   
    except AttributeError:
        pass 
    time.sleep(61)

while True:
    executeSomething()               