from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Connexion à MongoDB (le nom "mongo" sera le nom du conteneur)
client = MongoClient("mongodb://mongo:27017/")
db = client["testdb"]
collection = db["messages"]

@app.route("/")
def home():
    return "Hello depuis Flask + MongoDB 🎉"

@app.route("/add")
def add_message():
    collection.insert_one({"message": "Bonjour MongoDB"})
    return "Message ajouté dans MongoDB ✅"

@app.route("/all")
def get_all():
    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
