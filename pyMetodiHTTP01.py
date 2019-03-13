'''
Created on 04 feb 2019

@author: mpasteri

https://www.tutorialspoint.com/flask/flask_http_methods.htm

http://127.0.0.1:5000/login

'''
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return 'Ciaooooooooooo'
        #return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return 'Bravvooooo'
        #return redirect(url_for('success',name = user))    


if __name__ == '__main__':
    app.run(debug = True)
