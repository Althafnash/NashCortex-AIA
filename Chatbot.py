import json
import numpy as np
import random
import pickle
import subprocess as sub
import nltk
from nltk.stem import WordNetLemmatizer
from time import strftime
from keras.api.models import load_model
from Bandwidth import bandwidth
from webcam import face
import pyttsx3
from MiniGame import Minecraft
import pywhatkit_utils as pwk
from clock import Clock
from WSL import NMAP
import speech_recognition as sr
from OTXCLI.OTXCLI import OTXCLI_App
from DOS import SISP, SIMP, MISP, MIMP
from Encryption import encrypt
from TCPScanner import run
from PortScanner import port_scanner,Live_port_scanner,Detailed_port_scanner
from termcolor import colored
from Repo_modules import engine,Security
import time

nltk.download('punkt_tab')
nltk.download('wordnet')

# Initialize text-to-speech
def talk(text):
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()

# Load necessary files for chatbot
lemmatizer = WordNetLemmatizer()
with open('data.json', encoding='utf-8') as file:
    intents = json.load(file)
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')

# Helper functions for NLP processing
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    return [lemmatizer.lemmatize(word.lower()) for word in sentence_words]

def bag_of_words(sentence, words):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        if w in words:
            bag[words.index(w)] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence, words)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return [{"intent": classes[r[0]], "probability": str(r[1])} for r in results]

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    for i in intents_json['intents']:
        if i['tag'] == tag:
            return random.choice(i['responses'])
    return "Sorry, I didn't get that."

listener = sr.Recognizer()
def speechrecognition():
    command = ""
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print(colored("Adjusting for ambient noise, please wait...","blue"))
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print(colored("You can start talking...","green"))

            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print(colored("Processing your input...","blue"))

            command = recognizer.recognize_google(audio).lower()
            print(colored(f"Recognized Command: {command}","blue"))

            if 'jarvis' in command:
                command = command.replace("jarvis", "").strip()

    except sr.UnknownValueError:
        print(colored("Sorry, I didn't catch that. Please repeat.","yellow"))
        talk("Sorry, I didn't catch that. Please repeat.")
    except sr.RequestError as e:
        print(colored(f"Could not request results from Google Speech Recognition; {e}","yellow"))
        talk("It seems there is a network issue. Please check your connection.")
    except sr.WaitTimeoutError:
        print(colored("I didn't hear anything. Please speak again.","yellow"))
        talk("I didn't hear anything. Please speak again.")
    except Exception as e:
        print(colored(f"An unexpected error occurred: {e}","red"))
        talk("An unexpected error occurred. Please try again.")

    return command

def main():
    sub.run("cls", shell=True)
    string = strftime('%H:%M %p')
    print("=================================================================")
    talk(f"Welcome back, sir. The time is {string}")
    print("=================================================================")
    print(colored("Welcome back sir","blue"))
    print("=================================================================")
    print(colored("Bot is running... (type 'quit' to exit or ctrl/cmd + c)","blue"))
    print("=================================================================")

    while True:
        command = speechrecognition()

        if command == "quit":
            print("Exiting the program...")
            break
        
        # Handle specific commands
        if 'server' in command:
            try:
                sub.run('npm start', shell=True)
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()

        elif 'bandwidth' in command:
            try:
                bandwidth()
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()

        elif 'minecraft' in command or 'game' in command:
            try:
                Minecraft()
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()

        elif 'time' in command or 'whats the time' in command:
            try:
                Clock()
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()

        elif 'interface' in command:
            try:
                sub.run('d:/NashBot/myenv/Scripts/python.exe d:/NashBot/Webchatbot.py', shell=True)
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()    

        elif 'url locator' in command:
            try:
                sub.run('cd search', shell=True)
                sub.run('d:/NashBot/myenv/Scripts/python.exe d:/NashBot/search/webCrawler.py', shell=True)
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()

        elif 'youtube' in command:
            try:
                pwk.Search_on_Youtube()
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()

        elif 'send email' in command:
            try:
                pwk.Mail()
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()

        elif 'handwriting' in command:
            try:
                pwk.Handwritting()
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()

        elif 'google' in command:
            try:
                pwk.search()
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()

        elif 'whatsapp' in command:
            try:
                pwk.Whatsapp_msg()
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()

        elif 'scan network' in command:
            try:
                NMAP()
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()

        elif 'security tools' in command:
            try:
                talk("Starting OTXCLI")
                cli = OTXCLI_App()
                print('1. Ip Addresses 2. Domain Name 3. URL 4. Hostname')
                Input = input("What do you want to scan/search: ")
                if 'ip' in Input:
                    IP = input('Enter the IP Address: ')
                    cli.process_ip(IP)
                elif 'domain' in Input:
                    Domain_name = input('Enter the Domain Name: ')
                    cli.process_ip(Domain_name)
                elif 'url' in Input:
                    URL = input('Enter the URL: ')
                    cli.process_ip(URL)
                elif 'hostname' in Input:
                    Hostname = input('Enter the Hostname: ')
                    cli.process_ip(Hostname)
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()

        elif 'start a dos attack' in command:
            try:
                talk("Starting DOS")
                cli = OTXCLI_App()
                print('1. SISP - Single IP Source Port Flood')
                print('2. SIMP - Single IP Source Ports Flood')
                print('3. MISP - Multiple Random Source IPs Flood')
                print('4. MIMP - Multiple Random Source IPs and Source Ports Flood')
                Input = input("What do you want to scan/search: ")
                if 'SISP' in Input:
                    SISP()
                elif 'SIMP' in Input:
                    SIMP()
                elif 'MISP' in Input:
                    MISP()
                elif 'MIMP' in Input:
                    MIMP()
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()

        elif 'start an encryption algorithm' in command:
            try:
                talk("Starting encryption algorithm")
                encrypted_message, Message = encrypt()
                print(f"Encrypted Message: {encrypted_message}")
                print(f"Original Message: {Message}")
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()

        elif 'scan tcp packet' in command:
            try:
                talk("Starting TCP scanner")
                run()
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()
            
        elif 'Scan ports' in command:
            try:
                talk("Starting port scanner")
                print('''
                    1. PortScanner - Normal Port scanner 
                    2. DetailedPortScaner - A detailed Port scanner which scans everything 
                    3. LivePortScanner - This scans the port live 
                ''')
                Input = input('Which port should I use : ')
                if 'PortScanner' in command:
                    port_scanner()
                elif 'DetailedPortScaner' in command:
                    Detailed_port_scanner()
                elif 'LivePortScanner' in  command:
                    Live_port_scanner()
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()

        elif 'start physics engine' in command:
            try:
                engine()
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()

        elif 'start script' in command:
            try:
                Security()
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()

        elif 'restart' in command:
            main()
        elif 'exit' in command:
            break
        else:
            try:
                if command:  
                    ints = predict_class(command)
                    res = get_response(ints, intents)
                    talk(res)
                    print(res)
            except Exception as e:
                print(f'an error occured :: {e}')
                talk('Restarting systems')
                main()

        time.sleep(10)  

if __name__ == "__main__":
    main()
