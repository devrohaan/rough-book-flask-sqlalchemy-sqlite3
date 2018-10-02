#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 01:12:01 2018
@author: rohanbagwe

VERY BASIC FLASK LOGIN FORM 
"""


from flask import Flask, render_template,request
from user_model import User
from base import engine
from base import SessionMakerObj


# initializing a variable of Flask
app = Flask(__name__)


# decorating index function with the app.route
@app.route('/')
def index():
   return render_template('login.html')


'''
# decorating index function with the app.route with url as /login
@app.route('/login')
def index():
   return render_template('login.html')

Normally, Flask run in single-threaded mode, and can only handle one request at a time, 
and any parallel requests should wait until they can be handled. 

app.run(threaded=True)
app.run(host='0.0.0.0', port=5000)
app.run(debug=True)
app.run(threaded=True) to allow to access multiple requests

'''


@app.route('/login',  methods=['POST'])
def success():
   if request.method == 'POST':
       # Create ORM session object
       session = SessionMakerObj()
       uName = request.form['usrname']
       uPassword = request.form['password']
       #   
       user = session.query(User).filter_by(username=uName).first()
       if uPassword == user.password:
           
           return render_template('success.html', param=uName)
       else:
           return render_template('failure.html', param=uName)
   else:
       pass

      
      
if __name__ == "__main__":
   app.run()

   
