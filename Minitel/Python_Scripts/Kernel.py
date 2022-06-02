import os 
import subprocess

def kernel(register = None):
    if register == None:
        cmd = 'uname -v'
        os.system(cmd)
    else :
            p1 = subprocess.Popen(['uname','-v'],stdout=subprocess.PIPE,text=True) 
            output = str(p1.communicate())
            output = output.split("\n")
            output = output[0].split("None")
            output = output[0].split("\\")
            return output[0]+ " " + output[1] + " " 

kernel()