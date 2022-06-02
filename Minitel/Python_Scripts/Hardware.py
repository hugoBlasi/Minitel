# importing libraries
from curses import echo
import subprocess
import os


def hardware(register=None):

	if register == None:
		cmd = 'lshw'
		args = '-short'

		temp = subprocess.Popen([cmd, args], stdout = subprocess.PIPE)
	
		print(temp)
	
		output = str(temp.communicate())
	
		output = output.split("\n")
	
		output = output[0].split('\\')

		res = []
	
		for line in output:
			res.append(line)
	
		for i in range(1, len(res) - 1):
    			if(i == 4):
		    		print(res[0]),print(res[4]),print(res[5])
			
		
	else :
		temp = subprocess.Popen(['lshw', '-short'], stdout = subprocess.PIPE)
	
		print(temp)
	
		output = str(temp.communicate())
	
		output = output.split("\n")
	
		output = output[0].split('\\')

		res = []
	
		for line in output:
			res.append(line)
	
		for i in range(1, len(res) - 1):
                    if(i == 4):
                        with open('user_info.txt', 'a') as f:
                            f.write(res[0])
                            f.write("\n")
                            f.write(res[4])
                            f.write("\n")
                            f.write(res[5])
                            f.write("\n")
                        return res[0] + " " + res[4] + " " + res[5]

		    														




    # if (register == None):
    # 	cmd = 'lshw'
    # 	args = '-short'
    # else:
    # 	with open('user_info.txt', 'a') as f:

    # 		temp = subprocess.Popen(['lshw', '-short'],stdout = subprocess.PIPE)
    # 		output = str(temp.communicate())
    # 		output = output.split("\n")
    # 		output = output[0].split('\\')
    # 		res = []
    # 		for line in output:
    # 			print(len(output))
    # 			res.append(line)
    # 			f.write(res[0])

    # for i in range(1, len(res) - 1):

    # 	if(i == 4):

    #     	print(res[0]),print(res[4]),print(res[5])

    # return res


hardware()
# if __name__ == '__main__':
# 	list_command('-short')
