from flask import Flask
from pymongo import MongoClient
#from dotenv import load_dotenv
import os

#load_dotenv() 

client = MongoClient('mongodb://localhost:27017')
#client = MongoClient(os.getenv("AZURE_COSMOSDB_CONNECTION_STRING"))

db = client['ain3003']
bookstore = db['bookstore']

app = Flask(__name__)

from application import routes