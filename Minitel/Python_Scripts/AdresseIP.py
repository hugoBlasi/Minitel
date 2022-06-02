import os
import subprocess

def list_command(register = None):
	if register == None:
		cmd = 'hostname -i'
		os.system(cmd)
	else :
			p1 = subprocess.Popen(['hostname -i'],stdout=subprocess.PIPE,text=True,shell=True) 
			output = str(p1.communicate())
			output = output.split("\n")
			output = output[0].split("None")
			output = output[0].split("\\")
			return output[0]+ " " + output[1] + " "			

list_command()
	
