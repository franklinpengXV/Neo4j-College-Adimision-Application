# Neo4j Databse online predictor Application
This is an Neo4j project developed for DS220.

The Main goal is to develop a application to help student understand their chance of getting in to the top Graduate schools.

The data is anonymized by withdraw the Grad School's name and rank them from top to bottom from 1 to 5 (1 is the best Grad School).

Next Using Html5 + Neo4j to develop the online graph application that, taks user's GPA, GRE Score, TOEFL Score etc. Then track the dataset to find the set of data that have the simliar score to the input and return a predicted Grad School ranking for Student. 


Make Sure the Neo4j local browser (localhost:7474) is accessible before using the admission file, 
The Admission Prediction will allow you to develop and import admission.txt as node and relationship to Neo4j database. 
then using pycharm to access the rest of code. library include py2neo, Flask, flask_wtf and neo4jrestclient.

Test Folder contain all the code for development.
neo4j-flask contain all the files in test folder + the git/heroku upload file.

live demo url
https://enigmatic-oasis-14339.herokuapp.com/

For the live demo url to work, 
Start your local Neo4j Server (Download & Install), open the Neo4j Browser. Then go to github url and download the admission folder, use python idle to run AdmissionPrediction.py and follow the step, when asking for create database, select admission.txt, wait until the program finish. Last open the Live Demo url link, you will able to run it local on your computer.

