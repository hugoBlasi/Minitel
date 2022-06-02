import os 
import subprocess

def uptime(register = None):
    if register == None:
        cmd = 'uptime'
        os.system(cmd)
    else :
            p1 = subprocess.Popen(['uptime'],stdout=subprocess.PIPE,text=True) 
            output = str(p1.communicate())
            output = output.split("\n")
            output = output[0].split("None")
            output = output[0].split("\\")
            return output[0] + " " + output[1]

uptime()