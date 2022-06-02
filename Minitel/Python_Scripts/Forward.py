import os
import subprocess

def forward(register = None): 
    if register == None:   
        cmd = 'cat /proc/sys/net/ipv4/ip_forward'
        os.system(cmd)
    else : 
            p1 = subprocess.Popen(['cat /proc/sys/net/ipv4/ip_forward'],stdout = subprocess.PIPE, text = True, shell = True)
            output = str(p1.communicate())
            output = output.split("\n")
            output = output[0].split("None")
            output = output[0].split("\\")
            return output[0]+ " " + output[1] + " " 
forward()