import sys
import subprocess
import os               
import time

def executeSomething():
    # This setting is very important to avoid errors 
    os.environ['PYTHONIOENCODING'] = 'utf-8'    #setting the sys environment, or we will get unicoden error
    
    procs = []
    files = ["TwitterDownloader_IL_IN_OH.py","TwitterDownloader_IA_MN_NE.py"]   # put the file you want to run simultanously
    try:
        for i in files:
            proc = subprocess.Popen([sys.executable,i])
            procs.append(proc)
        
        for proc in procs:
            proc.wait() 
    except AttributeError:
        pass 
    time.sleep(61)

while True:
    executeSomething()               