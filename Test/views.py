import os
from json import dumps
from flask import Flask, render_template, g, Response,request
from neo4jrestclient.client import GraphDatabase
app = Flask(__name__)

@app.route('/')
def get_ori():
    return render_template("index.html")

@app.route('/index.html')
def get_index():
    return render_template("index.html")

@app.route('/1.html')
def get_1():
    return render_template("1.html")

@app.route('/2.html')
def get_2():
    return render_template("2.html")

@app.route('/3.html')
def get_3():
    return render_template("3.html")

@app.route('/4.html')
def get_4():
    return render_template("4.html")

@app.route('/5.html')
def get_5():
    return render_template("5.html")