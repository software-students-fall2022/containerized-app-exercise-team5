from flask import Flask, render_template, request, redirect, url_for, make_response
from bson.objectid import ObjectId
from dotenv import dotenv_values
from utils import *

import pymongo

# instantiate the app
app = Flask(__name__, static_url_path='/static')

# add custom filter
app.jinja_env.filters['first_sentence'] = extract_first_sentence

cxn = pymongo.MongoClient("db",27017)
db = cxn['containerizedTest']


@app.route('/sentiment-list-view')
def show_sentiment_list_view():
	sentiments = db.sentiments.find()

	return render_template('sentimentListPage.html', sentiments=sentiments)

@app.route('/sentiment-result-view')
def show_sentiment_result_view():
	query = request.args
	sentiment = db.sentiments.find_one({'_id': ObjectId(query.get('id'))})

	return render_template('sentimentResultPage.html', sentiment=sentiment)

# run the app
if __name__ == "__main__":
	app.run()


# # load credentials and configuration options from .env file
# # if you do not yet have a file named .env, make one based on the template in env.example
# config = dotenv_values(".env")

# # turn on debugging if in development mode
# if config['FLASK_ENV'] == 'development':
# 	# turn on debugging, if in development
# 	app.debug = True # debug mnode

# cxn = pymongo.MongoClient(config['MONGO_URI'], serverSelectionTimeoutMS=5000)
# try:
# 	# verify the connection works by pinging the database
# 	cxn.admin.command('ping') # The ping command is cheap and does not require auth.
# 	db = cxn[config['MONGO_DBNAME']] # store a reference to the database
# 	print(' *', 'Connected to MongoDB!') # if we get here, the connection worked!
# except Exception as e:
# 	# the ping command failed, so the connection is not available.
# 	# render_template('error.html', error=e) # render the edit template
# 	print(' *', "Failed to connect to MongoDB at", config['MONGO_URI'])
# 	print('Database connection error:', e) # debug