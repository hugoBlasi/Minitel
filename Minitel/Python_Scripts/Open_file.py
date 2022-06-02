import os 
import subprocess

def open_file(register = None):
    if register == None:
        cmd = 'ulimit -n'
        os.system(cmd)
    else :
            p1 = subprocess.Popen(['ulimit -n'],stdout=subprocess.PIPE,text=True,shell = True) 
            output = str(p1.communicate())
            output = output.split("\n")
            output = output[0].split("None")
            output = output[0].split("\\")
            return output[0]+ " " + output[1] + " " 
    
open_file()