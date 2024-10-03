import json
import numpy as np  
import random
import pickle
import subprocess as sub
import nltk
from nltk.stem import WordNetLemmatizer
from time import strftime
from flask import Flask, request, jsonify, render_template
from keras.api.models import load_model
from Bandwidth import bandwidth
from webcam import face
import pyttsx3
from MiniGame import Minecraft
from clock import Clock
import speech_recognition as sr

app = Flask(__name__)

def talk(text):
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()

# Load necessary files
lemmatizer = WordNetLemmatizer()
# Load necessary files with utf-8 encoding
with open('data.json', encoding='utf-8') as f:
    intents = json.load(f)
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
    if not intents_list:  # Handle empty intents_list
        return "I'm not sure how to respond to that."

    tag = intents_list[0]['intent']
    for i in intents_json['intents']:
        if i['tag'] == tag:
            return random.choice(i['responses'])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_bot_response():
    user_input = request.json.get("message")  # Get user input from the front end
    
    if user_input:  
        if 'server' in user_input:
            sub.run('npm start', shell=True)
            return jsonify({"response": "Server started."})
        elif 'bandwidth' in user_input: 
            bandwidth()
            return jsonify({"response": "Bandwidth information retrieved."})
        elif any(word in user_input for word in ['game', 'minecraft']):
            Minecraft()
            return jsonify({"response": "Minecraft started."})
        elif any(word in user_input for word in ['time', 'show time', 'whats the time', 'tell the time']):
            Clock()
            return jsonify({"response": f"The time is {strftime('%H:%M %p')}"})
        else:
            ints = predict_class(user_input)

            # Check if no intents were predicted
            if not ints:
                return jsonify({"response": "Sorry, I did not understand that."})

            # Get response based on the predicted intent
            res = get_response(ints, intents)
            return jsonify({"response": res})
    
    return jsonify({"response": "Sorry, I did not understand that."})

if __name__ == "__main__":
    app.run(debug=True)
