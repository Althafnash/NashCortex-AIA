import pywhatkit as kit
import time

def Whatsapp_msg():
    Phone_number = input("Enetr Phone number of the person : ")
    Message = input("Enter the message : ")

    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min + 1  

    if minute >= 60:
        minute -= 60
        hour += 1
        if hour >= 24: 
            hour -= 24

    kit.sendwhatmsg(f'{Phone_number}', f'{Message}', hour, minute)

def search():
    Search_Term = input("Enetr the search term : ")
    kit.search(f"{Search_Term}")

def Search_on_Youtube():
    search_term = input("Eneter teh term you want to search : ")
    kit.playonyt(f"{search_term}")

def Handwritting():
    Text = input("Enetr the text : ")
    kit.text_to_handwriting(f"{Text}")

def Mail():
    Email = input("Eneter the sender Email  : ")
    Password = input("Enetr password  : " )
    Subject = input("Enetr the subject : ")
    Message_Body = input("Enter the Meassage : ") 
    Reciver_email = input("Enetr recivers email  : ")
    kit.send_mail(Email,Password,Subject,Message_Body,Reciver_email)

