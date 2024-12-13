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
import time

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

# Speech recognition
listener = sr.Recognizer()

def speechrecognition():
    command = ""
    try:
        with sr.Microphone() as source:
            print("You can start talking ...")
            listener.adjust_for_ambient_noise(source, duration=2)  # Adjust ambient noise
            voice = listener.listen(source, timeout=5, phrase_time_limit=10)
            command = listener.recognize_google(voice).lower()
            if 'jarvis' in command:
                command = command.replace("jarvis", "").strip()
    except sr.UnknownValueError:
        print("Sorry, I did not understand the command.")
        talk("Sorry, I did not understand the command.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        talk("There seems to be a network issue.")
    except Exception as e:
        print(f"An error occurred: {e}")
        talk("An error occurred. Please try again.")
    return command

# Main function
def main():
    sub.run("cls", shell=True)
    string = strftime('%H:%M %p')
    talk(f"Welcome back, sir. The time is {string}")
    print("=================================================================")
    print("Welcome back sir")
    print("=================================================================")
    print("Bot is running... (type 'quit' to exit or ctrl/cmd + c)")
    print("=================================================================")

    while True:
        command = speechrecognition()

        if command == "quit":
            print("Exiting the program...")
            break
        
        # Handle specific commands
        if 'server' in command:
            sub.run('npm start', shell=True)

        elif 'bandwidth' in command:
            bandwidth()

        elif 'minecraft' in command or 'game' in command:
            Minecraft()

        elif 'time' in command or 'whats the time' in command:
            Clock()

        elif 'interface' in command:
            sub.run('d:/NashBot/myenv/Scripts/python.exe d:/NashBot/Webchatbot.py', shell=True)

        elif 'url locator' in command:
            sub.run('cd search', shell=True)
            sub.run('d:/NashBot/myenv/Scripts/python.exe d:/NashBot/search/webCrawler.py', shell=True)

        elif 'youtube' in command:
            pwk.Search_on_Youtube()

        elif 'send email' in command:
            pwk.Mail()

        elif 'handwriting' in command:
            pwk.Handwritting()

        elif 'google' in command:
            pwk.search()

        elif 'whatsapp' in command:
            pwk.Whatsapp_msg()

        elif 'scan network' in command:
            NMAP()

        elif 'security tools' in command:
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

        elif 'start a dos attack' in command:
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

        elif 'start an encryption algorithm' in command:
            talk("Starting encryption algorithm")
            encrypted_message, Message = encrypt()
            print(f"Encrypted Message: {encrypted_message}")
            print(f"Original Message: {Message}")

        elif 'start the tcp scanner' in command:
            run()

        else:
            # Default response if no specific command is found
            if command:  
                ints = predict_class(command)
                res = get_response(ints, intents)
                talk(res)
                print(res)

        time.sleep(2)  # Delay between commands

# Entry point of the program
if __name__ == "__main__":
    main()
