import os
from app import app
from flask import render_template, request, redirect, session, url_for

app.secret_key = b'\xd9\x87r\xab\xf3\xb0Uz\xf7\x10(\xe2M@\xd5\x07'
# events = [
#       {"event":"First Day of Classes", "date":"2019-08-21"},
#       {"event":"Winter Break", "date":"2019-12-20"},
#       {"event":"Finals Begin", "date":"2019-12-01"},
#       {"event":"Marcos' Berfday", "date":"2004-04-20"}
#   ]
from flask_pymongo import PyMongo
# name of database
app.config['MONGO_DBNAME'] = 'project'
# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://username:fTf3Opfruo3pz25x@cluster0-s1y61.mongodb.net/project?retryWrites=true&w=majority'
mongo = PyMongo(app)
# INDEX
@app.route('/')
@app.route('/index')
def index():
   # connect to the database
   collection = mongo.db.henna
   # pull data from database
   henna = collection.find({})
   #In quotation marks, the above method finds an item in a list. EX: "event":"My Birthday". Put .find and .sort to sort alphabetically. Sorting by -1 reverses the order
   #use the pulled data
   return render_template('index.html', henna = henna)
# CONNECT TO DB, ADD DATA
@app.route('/add')
def add():
   # connect to the database
   henna = mongo.db.henna
   # insert new data
    
   # return a message to the user
    
@app.route('/products',methods=['GET','POST'])
def products():
   return render_template('signedin.html')
    
@app.route('/scheduling',methods=['GET','POST'])
def signup_and_scheduling():
   if request.method =='POST':
      # take in the info they gave us, check if username is taken, if not, put in list of users on database
      users = mongo.db.users
      existing_user = users.find_one({"username":request.form['username']})
      if existing_user is None:
         users.insert({"username": request.form['username'],'password':request.form['password']})
         return redirect(url_for('index'))
      else:
         return "Try again Jimmy"
   else:
      return render_template('scheduling.html')



@app.route('/login', methods=['POST','GET'])
def login(): 
   users = mongo.db.users
   existing_user = users.find_one({"username":request.form['username']})
   if existing_user:
      if existing_user['password'] == request.form['password']:
         session['username'] =request.form['username']
         return redirect(url_for('/signedin'))
      else:
         return "Fake Jimmy alert"
   else:
      return "There is no user with that username Jimmy"
      
@app.route('/logout')
def logout():
   session.clear()
   return redirect('/')

   