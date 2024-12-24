import json
import numpy as np
import random
import pickle
import subprocess as sub
import nltk
from nltk.stem import WordNetLemmatizer
from time import strftime
from keras.api.models import load_model
from termcolor import colored
import speech_recognition as sr
import pyttsx3
import time

# Importing custom modules
from Bandwidth import bandwidth
from webcam import face
from MiniGame import Minecraft
from clock import Clock
from WSL import NMAP
from OTXCLI.OTXCLI import OTXCLI_App
from DOS import SISP, SIMP, MISP, MIMP
from Encryption import encrypt
from TCPScanner import run
from PortScanner import port_scanner, Live_port_scanner, Detailed_port_scanner
from Repo_modules import engine, Security
import pywhatkit_utils as pwk

# Initializing necessary components
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

# NLP Processing
lemmatizer = WordNetLemmatizer()
with open('data.json', encoding='utf-8') as file:
    intents = json.load(file)
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')

# Text-to-speech initialization
def talk(text):
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()

# Helper Functions
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

def recognize_speech():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print(colored("Adjusting for ambient noise, please wait...", "blue"))
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print(colored("You can start talking...", "green"))
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print(colored("Processing your input...", "blue"))
            command = recognizer.recognize_google(audio).lower()
            print(colored(f"Recognized Command: {command}", "blue"))
            if 'jarvis' in command:
                command = command.replace("jarvis", "").strip()
            return command
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that. Please repeat.")
    except sr.RequestError:
        talk("It seems there is a network issue. Please check your connection.")
    except sr.WaitTimeoutError:
        talk("I didn't hear anything. Please speak again.")
    return ""

def handle_command(command):
    try:
        if 'server' in command:
            sub.run('npm start', shell=True)
        elif 'bandwidth' in command:
            bandwidth()
        elif 'minecraft' in command or 'game' in command:
            Minecraft()
        elif 'time' in command or 'whats the time' in command:
            Clock()
        elif 'interface' in command:
            sub.run('python Webchatbot.py', shell=True)
        elif 'url locator' in command:
            sub.run('python search/webCrawler.py', shell=True)
        elif 'youtube' in command:
            pwk.Search_on_Youtube()
        elif 'send email' in command:
            pwk.Mail()
        elif 'google' in command:
            pwk.search()
        elif 'whatsapp' in command:
            pwk.Whatsapp_msg()
        elif 'scan network' in command:
            NMAP()
        elif 'security tools' in command:
            handle_security_tools()
        elif 'start a dos attack' in command:
            handle_dos_tools()
        elif 'start an encryption algorithm' in command:
            encrypted_message, Message = encrypt()
            print(f"Encrypted Message: {encrypted_message}")
            print(f"Original Message: {Message}")
        elif 'scan tcp packet' in command:
            run()
        elif 'scan ports' in command:
            handle_port_scanning()
        elif 'start physics engine' in command:
            engine()
        elif 'start script' in command:
            Security()
        elif 'restart' in command:
            main()
        elif 'exit' in command:
            exit_program()
        else:
            handle_chatbot_response(command)
    except Exception as e:
        print(f"An error occurred: {e}")
        talk("Restarting systems")
        main()

def handle_security_tools():
    talk("Starting OTXCLI")
    cli = OTXCLI_App()
    print('1. IP Addresses 2. Domain Name 3. URL 4. Hostname')
    Input = input("What do you want to scan/search: ")
    if 'ip' in Input:
        cli.process_ip(input('Enter the IP Address: '))
    elif 'domain' in Input:
        cli.process_ip(input('Enter the Domain Name: '))
    elif 'url' in Input:
        cli.process_ip(input('Enter the URL: '))
    elif 'hostname' in Input:
        cli.process_ip(input('Enter the Hostname: '))

def handle_dos_tools():
    print('1. SISP 2. SIMP 3. MISP 4. MIMP')
    Input = input("Select a DOS attack type: ")
    if 'SISP' in Input:
        SISP()
    elif 'SIMP' in Input:
        SIMP()
    elif 'MISP' in Input:
        MISP()
    elif 'MIMP' in Input:
        MIMP()

def handle_port_scanning():
    print('1. Normal Scanner 2. Detailed Scanner 3. Live Scanner')
    Input = input('Choose a port scan type: ')
    if 'Normal' in Input:
        port_scanner()
    elif 'Detailed' in Input:
        Detailed_port_scanner()
    elif 'Live' in Input:
        Live_port_scanner()

def handle_chatbot_response(command):
    if command:
        intents = predict_class(command)
        response = get_response(intents, intents)
        talk(response)
        print(response)

def exit_program():
    print("Exiting the program...")
    talk("Goodbye!")
    exit()

def main():
    sub.run("cls", shell=True)
    print("=" * 65)
    print(colored("Welcome back, sir", "blue"))
    talk(f"Welcome back, sir. The time is {strftime('%H:%M %p')}")
    print("=" * 65)
    while True:
        command = recognize_speech()
        handle_command(command)
        time.sleep(1)

if __name__ == "__main__":
    main()
