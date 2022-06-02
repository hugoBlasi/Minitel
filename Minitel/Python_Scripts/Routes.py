import os 
import subprocess

def route(register = None):
    if register == None:   
        cmd = 'ip route'
        os.system(cmd)
    else : 
            p1 = subprocess.Popen(['ip route '],stdout = subprocess.PIPE, text = True, shell = True)
            output = str(p1.communicate())
            output = output.split("\n")
            output = output[0].split("None")
            output = output[0].split("\\")
            return output[0]+ " " + output[1] + " " 
    
route()