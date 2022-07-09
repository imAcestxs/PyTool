import time, os, requests, string, random, string, ctypes, os.path, threading
from discord import Webhook, RequestsWebhookAdapter
from colorama import Fore

def menu():
    print("""
    /$$$$$$$         /$$$$$$$$                  /$$
    | $$__  $$       |__  $$__/                 | $$
    | $$  \ $$ /$$   /$$| $$  /$$$$$$   /$$$$$$ | $$
    | $$$$$$$/| $$  | $$| $$ /$$__  $$ /$$__  $$| $$
    | $$____/ | $$  | $$| $$| $$  \ $$| $$  \ $$| $$
    | $$      | $$  | $$| $$| $$  | $$| $$  | $$| $$
    | $$      |  $$$$$$$| $$|  $$$$$$/|  $$$$$$/| $$
    |__/       \____  $$|__/ \______/  \______/ |__/
            /$$  | $$                            
            |  $$$$$$/                            
            \______/                             
Made by ace!#0666 | Join our Discord: discord.gg/projectsoju
    """)
    time.sleep(0.5)
    print("[1] PyTalk : Talk as Webhook")
    print("[2] PySpammer : Spam as Webhook")
    print("[3] Close The Program")

menu()
option = int(input("\t\t\t\t\t\t\t\t\t   Select an option : "))

def pytalk():
    print("""
    /$$$$$$$         /$$$$$$$$        /$$ /$$      
    | $$__  $$       |__  $$__/       | $$| $$      
    | $$  \ $$ /$$   /$$| $$  /$$$$$$ | $$| $$   /$$
    | $$$$$$$/| $$  | $$| $$ |____  $$| $$| $$  /$$/
    | $$____/ | $$  | $$| $$  /$$$$$$$| $$| $$$$$$/ 
    | $$      | $$  | $$| $$ /$$__  $$| $$| $$_  $$ 
    | $$      |  $$$$$$$| $$|  $$$$$$$| $$| $$ \  $$
    |__/       \____  $$|__/ \_______/|__/|__/  \__/
            /$$  | $$                            
            |  $$$$$$/                            
            \______/                             
    """)
    actWeb = input("Webhook : ")
    webhook = Webhook.from_url(actWeb, adapter=RequestsWebhookAdapter())
    talk = input("Say : ")
    webhook.send(talk)

def pyspammer():
    print("""
    /$$$$$$$            /$$$$$$                                                                    
    | $$__  $$          /$$__  $$                                                                   
    | $$  \ $$/$$   /$$| $$  \__/  /$$$$$$  /$$$$$$  /$$$$$$/$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$ 
    | $$$$$$$/ $$  | $$|  $$$$$$  /$$__  $$|____  $$| $$_  $$_  $$| $$_  $$_  $$ /$$__  $$ /$$__  $$
    | $$____/| $$  | $$ \____  $$| $$  \ $$ /$$$$$$$| $$ \ $$ \ $$| $$ \ $$ \ $$| $$$$$$$$| $$  \__/
    | $$     | $$  | $$ /$$  \ $$| $$  | $$/$$__  $$| $$ | $$ | $$| $$ | $$ | $$| $$_____/| $$      
    | $$     |  $$$$$$$|  $$$$$$/| $$$$$$$/  $$$$$$$| $$ | $$ | $$| $$ | $$ | $$|  $$$$$$$| $$      
    |__/      \____  $$ \______/ | $$____/ \_______/|__/ |__/ |__/|__/ |__/ |__/ \_______/|__/      
            /$$  | $$          | $$                                                               
            |  $$$$$$/          | $$                                                               
            \______/           |__/                                                               
            """)
    webHooker = input("Webhook : ")
    talk = input("Say : ")
    webhook = Webhook.from_url(webHooker, adapter=RequestsWebhookAdapter())

    while True:
        time.sleep(0.5)
        webhook.send(talk)
        print("Sent spam\n")
    
while option != 0:
    if option == 1:
        # Option 1
        pytalk()
    elif option == 2:
        # Option 2
        pyspammer()
    elif option == 3:
        # Option 3
        quit()
    else:
        print("\t\t\t\t\t\t\t\t\t   Invalid option try again!")
    print("")
    menu()
    option = int(input("\t\t\t\t\t\t\t\t\t   Select an option : "))
    
print("\t\t\t\t\t\t\t\t\t   Thanks for using this program goodbye.")