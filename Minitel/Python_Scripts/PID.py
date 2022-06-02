import os 

def pidof():
    cmd = 'ps aux'
    os.system(cmd)

pidof()