from flask import Flask, render_template, request, redirect, url_for, make_response
from markupsafe import escape
import pymongo
# import datetime
from datetime import date
from bson.objectid import ObjectId
import os
import subprocess
from speech import *
from sentiment_analysis import *
import speech_recognition as sr
import random as rand
import speech_recognition as sr
import pyttsx3
import sys

app = Flask(__name__)

cxn = pymongo.MongoClient("db", 27017)
db = cxn["containerizedTest"]


@app.route('/')
def record():
    return render_template('record.html')


@app.route('/recorded', methods=['POST'])
def recorded():

    recording = request.files['frecording']

    r = sr.Recognizer()

    with sr.AudioFile(recording) as source:
        audio = r.record(source)

    MyText = r.recognize_google(audio)
    MyText = MyText.lower()

    return render_template('record.html', speechText = MyText)


@app.route('/submit/<recording>', methods=['POST']) # 
def submit_record(recording):

    r = SentimentAnalysis(recording)

    sent = r.sentiment()
    pos = r.positiveWords()
    neg = r.negative_words()

    doc = {
        "text": recording,
        "isPositive": sent,
        "positive_words": pos,
        "negative_words": neg,
        # "createdDate": date.today()
    }
    db.sentiments.insert_one(doc)

    return render_template('success.html')


@app.errorhandler(Exception)
def handle_error(e):
    return render_template('error.html', error=e)


if __name__ == "__main__":
    app.run(debug=True)
