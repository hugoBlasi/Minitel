from curses import echo
import time
import subprocess
import os


def list_command(args = '-c 5 0'):

	cmd = 'ping'

	temp = subprocess.Popen([cmd, args], stdout = subprocess.PIPE)
	
	output = str(temp.communicate())
	
	output = output.split("\n")
	
	output = output[0].split('\\')

	res = []
	
	for line in output:
		res.append(line)
	
	for i in range(1, len(res) - 1):
    	    if(i == 4):
		        time.sleep(5),print(res[9])
        
	return res	

if __name__ == '__main__':
	list_command('-c 5 0')
