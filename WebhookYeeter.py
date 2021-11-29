import discord
import requests

print(""" _  _  _       _     _                 _     
(_)(_)(_)     | |   | |               | |    
 _  _  _ _____| |__ | |__   ___   ___ | |  _ 
| || || | ___ |  _ \|  _ \ / _ \ / _ \| |_/ )
| || || | ____| |_) ) | | | |_| | |_| |  _ ( 
 \_____/|_____)____/|_| |_|\___/ \___/|_| \_)
                                             
 _     _                                     
| |   | |              _                     
| |___| |_____ _____ _| |_ _____  ____       
|_____  | ___ | ___ (_   _) ___ |/ ___)      
 _____| | ____| ____| | |_| ____| |          
(_______|_____)_____)  \__)_____)_|          
                                             """)
print('Special thanks to Din/Jhin scripter, for helping me with the code.')
webhook = input("Webhook que ira ser deletada: ")

def delete():
	requests.delete(webhook)

while True:
	delete()

