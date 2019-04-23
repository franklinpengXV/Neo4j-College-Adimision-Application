from py2neo import Graph, Node, Relationship
from passlib.hash import bcrypt
from datetime import datetime
import uuid
import os

url = os.environ.get("GRAPHENEDB_URL","http://localhost:7474")
graph = Graph(url + "/db/data/")