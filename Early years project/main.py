from flask import Flask, render_template, request, flash, redirect
import requests

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/page1', methods=['GET','POST'])
def page1():
    return render_template('page1.html')

if __name__=='__main__':
    app.run(debug=True)
