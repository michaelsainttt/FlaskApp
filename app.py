from flask import Flask, jsonify, request

app = Flask(__name__)

BOOKS = [
    {"id": 1, "title":"Don Quixote", "author": "Cervantes"},
    {"id": 2, "title":"1984", "author": "George Orwell"},
    {"id": 3, "title":"The Great Gatsby", "author":"F.Scott Fitzgerald"}
]

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Welcome to my Flask App"}), 200
    
@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "GET":
        return jsonify({"books": BOOKS}), 200 

    if request.method == "POST":
        incoming = request.get_json()
        return jsonify({"status": "success", "received": incoming}), 201

