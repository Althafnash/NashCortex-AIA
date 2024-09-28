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
from clock import Clock
import speech_recognition as sr
import time

def talk(text):
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()

# Load necessary files
lemmatizer = WordNetLemmatizer()
intents = json.loads(open('data.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence, words):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence, words)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    for i in intents_json['intents']:
        if i['tag'] == tag:
            return random.choice(i['responses'])

sub.run("cls", shell=True)
string = strftime('%H:%M %p')
talk("welcome back sir " + "the time is " + string)
print("=================================================================")
print("Welcome back sir")
print("=================================================================")
print("Bot is running... (type 'quit' to exit or ctrl/cmd + c)")
print("=================================================================")

listener = sr.Recognizer()

def speechrecogniction():
    command = ""
    try:
        with sr.Microphone() as source:
            print("You can start talking ...")
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source, timeout=5, phrase_time_limit=10)
            command = listener.recognize_google(voice)
            command = str(command)
            command = command.lower() 
            if 'jarvis' in command:
                command = command.replace("jarvis", "") 
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

def main():
    while True:
        command = speechrecogniction()
        
        if command == "quit":
            break
        
        if 'server' in command:
            sub.run('node web_server.js', check=True)
        elif 'bandwidth' in command: 
            bandwidth()
        elif any(word in command for word in ['game', 'minecraft']):
            Minecraft()
        elif any(word in command for word in ['time', 'show time', 'whats the time', 'tell the time']):
            Clock()
        else:
            if command:  
                ints = predict_class(command)
                res = get_response(ints, intents)
                talk(res)
                print(res)

        time.sleep(2)  

if __name__ == "__main__":
    main()