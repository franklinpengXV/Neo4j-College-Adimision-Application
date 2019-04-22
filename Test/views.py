import os
from json import dumps
from flask import Flask, render_template, g, Response,request, flash
from neo4jrestclient.client import GraphDatabase

app = Flask(__name__)
@app.route('/')
def get_ori():
    return render_template("index.html")

@app.route('/index.html')
def get_index():
    return render_template("index.html")

@app.route('/index/GRE.html')
def get_index_gre():
    return render_template("index/GRE.html")

@app.route('/index/TOEFL.html')
def get_index_toefl():
    return render_template("index/TOEFL.html")

@app.route('/index/CGPA.html')
def get_index_cgpa():
    return render_template("index/CGPA.html")

@app.route('/index/Research.html')
def get_index_research():
    return render_template("index/Research.html")

@app.route('/index/SOP.html')
def get_index_sop():
    return render_template("index/SOP.html")

@app.route('/index/LOR.html')
def get_index_lor():
    return render_template("index/LOR.html")

@app.route('/index_2.html')
def get_index_2():
    return render_template("index_2.html")

@app.route('/index_2/GRE.html')
def get_index_2_gre():
    return render_template("index_2/GRE.html")

@app.route('/index_2/TOEFL.html')
def get_index_2_toefl():
    return render_template("index_2/TOEFL.html")

@app.route('/index_2/CGPA.html')
def get_index_2_cgpa():
    return render_template("index_2/CGPA.html")

@app.route('/index_2/Research.html')
def get_index_2_research():
    return render_template("index_2/Research.html")

@app.route('/index_2/SOP.html')
def get_index_2_sop():
    return render_template("index_2/SOP.html")

@app.route('/index_2/LOR.html')
def get_index_2_lor():
    return render_template("index_2/LOR.html")


@app.route('/index_3.html')
def get_index_3():
    return render_template("index_3.html")

@app.route('/index_3/GRE.html')
def get_index_3_gre():
    return render_template("index_3/GRE.html")

@app.route('/index_3/TOEFL.html')
def get_index_3_toefl():
    return render_template("index_3/TOEFL.html")

@app.route('/index_3/CGPA.html')
def get_index_3_cgpa():
    return render_template("index_3/CGPA.html")

@app.route('/index_3/Research.html')
def get_index_3_research():
    return render_template("index_3/Research.html")

@app.route('/index_3/SOP.html')
def get_index_3_sop():
    return render_template("index_3/SOP.html")

@app.route('/index_3/LOR.html')
def get_index_3_lor():
    return render_template("index_3/LOR.html")


@app.route('/index_4.html')
def get_index_4():
    return render_template("index_4.html")

@app.route('/index_4/GRE.html')
def get_index_4_gre():
    return render_template("index_4/GRE.html")

@app.route('/index_4/TOEFL.html')
def get_index_4_toefl():
    return render_template("index_4/TOEFL.html")

@app.route('/index_4/CGPA.html')
def get_index_4_cgpa():
    return render_template("index_4/CGPA.html")

@app.route('/index_4/Research.html')
def get_index_4_research():
    return render_template("index_4/Research.html")

@app.route('/index_4/SOP.html')
def get_index_4_sop():
    return render_template("index_4/SOP.html")

@app.route('/index_4/LOR.html')
def get_index_4_lor():
    return render_template("index_4/LOR.html")

@app.route('/index_5.html')
def get_index_5():
    return render_template("index_5.html")

@app.route('/index_5/GRE.html')
def get_index_5_gre():
    return render_template("index_5/GRE.html")

@app.route('/index_5/TOEFL.html')
def get_index_5_toefl():
    return render_template("index_5/TOEFL.html")

@app.route('/index_5/CGPA.html')
def get_index_5_cgpa():
    return render_template("index_5/CGPA.html")

@app.route('/index_5/Research.html')
def get_index_5_research():
    return render_template("index_5/Research.html")

@app.route('/index_5/SOP.html')
def get_index_5_sop():
    return render_template("index_5/SOP.html")

@app.route('/index_5/LOR.html')
def get_index_5_lor():
    return render_template("index_5/LOR.html")
