import os 
import subprocess

def version(register = None):
    if register == None:
        cmd = 'lsb_release -d'
        os.system(cmd)
    else :
            p1 = subprocess.Popen(['lsb_release', '-d'],stdout=subprocess.PIPE,text=True) 
            output = str(p1.communicate())
            output = output.split("\n")
            output = output[0].split("None")
            output = output[0].split("\\")
            return output[0]+ " " + output[1] + " " 
    

version()