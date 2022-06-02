# importing libraries
from curses import echo
import subprocess
import os

# a function to list the files in
# the current directory and
# parse the output.
def list_command(args = '-u'):

	cmd = 'ulimit'

	temp = subprocess.run([cmd, args], stdout = subprocess.PIPE,shell=True)
	
	

if __name__ == '__main__':
	list_command('-u')