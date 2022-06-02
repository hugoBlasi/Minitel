import os
import sys
import subprocess
import Kill
import platform
import Version
import Uptime
import Kernel
import Hardware
import Open_file
import AdresseIP
import Interfaces
import Routes
import Forward
import json
import ToJson
import ToTar

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    REPONSE = '\033[96m' #BLUE



def Menu(condition = 0):      
        if (condition == 0):
            clearConsole()
        if(condition == 1):
            print(bcolors.OK+'Tar file creation succeed'+bcolors.RESET)   
        print("\n")
        print(bcolors.OK+"[1] User info"+bcolors.RESET)
        print(bcolors.OK+"[2] Network info"+bcolors.RESET)
        print(bcolors.OK+"[3] Processus info"+bcolors.RESET)
        print(bcolors.OK+"[4] Generate Tar File"+bcolors.RESET)
        print(bcolors.WARNING+"[5] Exit"+bcolors.RESET)
        print("\n")
        answer = input(bcolors.REPONSE+"reponse :")

        if answer == "1":
            clearConsole()
            user_info()
        elif answer == "2":
            clearConsole()
            network_info()
        elif answer == "3":
            clearConsole()
            processus_info()
        elif answer == "4":
            clearConsole()
            ToJson.ToJson(1)
            ToJson.ToJson(2)
            ToTar.CreateTar()
            Menu(1)
        elif answer == "5":
            print(bcolors.RESET)
            clearConsole()
            exit
        else :
            clearConsole()
            print(bcolors.FAIL+"Uncorect answer"+bcolors.RESET)
            Menu(2)

def user_info():
    


    print("\n")
    print(bcolors.RESET)
    print("Version système d'exploitation :")
    exec(open("Version.py").read())
    print("\n")
    print("Uptime :")
    exec(open("Uptime.py").read())
    print("\n")
    print("Kernel :")
    exec(open("Kernel.py").read())
    print("\n")
    print("Informations Hardware :")
    exec(open("Hardware.py").read())
    print("\n")
    print("Limite de fichiers ouverts :")
    exec(open("Open_file.py").read())
    exec(open("Open_Processus.py").read())
    print("\n")
    print(bcolors.OK+"[1] Return to main menu"+bcolors.RESET)
    print("\n")
    answer = input(bcolors.REPONSE+"reponse :")

    if answer == "1":
        clearConsole()
        Menu()
    else:
        clearConsole()
        print(bcolors.FAIL+"Uncorect answer"+bcolors.RESET)
        user_info()


    
def network_info():
    
    print("\n")
    print(bcolors.RESET)
    print("Adresse IP :")
    exec(open("AdresseIP.py").read())
    print("\n")
    print("Interfaces existantes :")
    exec(open("Interfaces.py").read())
    print("\n")
    print("Nombre de paquets transmis/reçus :")
    exec(open("Ping.py").read())
    print("\n")
    print("Routes :")
    exec(open("Routes.py").read())
    print("\n")
    print("Forward paquet :")
    exec(open("Forward.py").read())
    print("\n")
    print(bcolors.OK+"[1] Return to main menu"+bcolors.RESET)
    print("\n")
    answer = input(bcolors.REPONSE+"reponse :")

    if answer == "1":
        clearConsole()
        Menu()
    elif answer == "2":
        ToJson.ToJson(2)
        Menu()
    else:
        clearConsole()
        print(bcolors.FAIL+"Uncorect answer"+bcolors.RESET)
        user_info()

def processus_info():
    
    print("\n")
    print(bcolors.OK+"[1] Return to main menu"+bcolors.RESET)
    print(bcolors.OK+"[2] PID"+bcolors.RESET)
    print(bcolors.OK+"[3] KILL process"+bcolors.RESET)
    print("\n")
    answer = input(bcolors.REPONSE+"reponse :")
    print(bcolors.RESET)

    if answer == "1":
        clearConsole()
        Menu()
    elif answer == "2":
        exec(open("PID.py").read())
        answer = input(bcolors.REPONSE+"Enter 1 to return :")
        if answer == "1":
            clearConsole()
            processus_info()
        else:
            clearConsole()
            print(bcolors.FAIL+"Uncorect answer"+bcolors.RESET)
    elif answer == "3":
        clearConsole()
        answer = input(bcolors.REPONSE+"Enter process to kill || Enter cancel to return : ")
        
        if answer == "cancel":
            clearConsole()
            print(bcolors.FAIL+"Kill canceled"+bcolors.RESET)
            processus_info()
        else:
            clearConsole()
            Kill.tuer(answer)
            print(bcolors.FAIL+answer+" Killed"+bcolors.RESET)
            processus_info()

    else:
        clearConsole()
        print(bcolors.FAIL+"Uncorect answer"+bcolors.RESET)
        processus_info()


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def register (error = None):
    clearConsole()
    if error == 1:
        print(bcolors.FAIL+"Password don't match, retry"+bcolors.RESET)
    elif error == 2:
        print(bcolors.FAIL+"Password too short, retry"+bcolors.RESET)
    elif error == 3:
        print(bcolors.FAIL+"Username exist, retry"+bcolors.RESET)

    db = open("Database.txt","r")
    Username = input(bcolors.REPONSE+"Enter Username: ")
    Password = input(bcolors.REPONSE+"Enter Password: ")
    PasswordConfirm = input(bcolors.REPONSE+"Confirm Password: ")
    print(bcolors.RESET)
    U = []
    P = []

    if PasswordConfirm != Password:
        register(1)
    else:
        if len(Password)< 6:  
            register(2)
        elif Username in db:
            register(3)
        else:
            db = open("Database.txt","a")
            db.write(Username+", "+Password+"\n")
            db.close()
            Home()
    for i in db:
        u,p = i.split(", ")
        p = p.strip()
        U.append(u)
        P.append(p)
    data = dict(zip(U, P))  

def Login(error = None):
    clearConsole()
    if error == 1:
        print(bcolors.FAIL+"Password or Username incorect"+bcolors.RESET)
    elif error == 2:
        print(bcolors.FAIL+"Username or Password doesn't exist"+bcolors.RESET)
    db = open("Database.txt","r")
    Username = input(bcolors.REPONSE+"Enter Username: ")
    Password = input(bcolors.REPONSE+"Enter Password: ")

    if not len (Username or Password)<1:
        U = []
        P = []
        for i in db:
            u,p = i.split(", ")
            p = p.strip()
            U.append(u)
            P.append(p)
        data = dict(zip(U, P))

        try: 
            if data[Username]:
                try:
                    if Password == data[Username]:
                        print(bcolors.OK+"Login sucess"+bcolors.RESET)
                        print(bcolors.OK+"Hi, "+Username+bcolors.RESET)
                        Menu()
                    else:
                        Login(1)
                except:
                    Login(1)
            else:

                Login(2)
        except: 
            Login(2)

def Home(option = None, error = None ):
    clearConsole()
    if error == 1:
        print(bcolors.FAIL+"Uncorect answer"+bcolors.RESET+"\n")
    print(bcolors.OK+"[1] Register"+bcolors.RESET)
    print(bcolors.OK+"[2] Login"+bcolors.RESET)
    print(bcolors.WARNING+"[3] Exit"+bcolors.RESET+"\n")
    option = input(bcolors.REPONSE+"answer :")
    if option == "1":
        register()
    elif option == "2":
        Login()
    elif option == "3":
        print(bcolors.RESET)
        clearConsole()
        exit
    else:
        
        Home(None,1)

Home()
