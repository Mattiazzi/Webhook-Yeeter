import requests
import os

#limpa terminal
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
         os.system('clear')
        
#Retorna se o status da URL eh igual a 200
def webhook_exists(webhookUrl):
    return requests.get(webhookUrl).status_code == 200

#Deleta duh
def delete():
	requests.delete(webhookUrl)


clear_screen()

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
print('Salve pro Din/Jhin scripter')
print(' ')

webhookUrl = input("Insert the WebHook you want to delete: ")

#Checa se webhook existe, se sim, deleta
if webhook_exists(webhookUrl):
      print("WebHook Exists!.")
      delete()
      print("...")
      print("Webhook deleted.")
else:
      print("WebHook doesn't exist.")
