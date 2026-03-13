import requests
from flask import Flask, jsonify, request


app = Flask(__name__)

crowd_data = {
    "people_count": 0,
    "crowd_level": "LOW",
    "queue_detected": False
    
}

@app.route("/crowd", methods=["GET"])
def get_crowd():
    return jsonify(crowd_data)

@app.route("/update", methods=["POST"])
def update_data():
    global crowd_data
    crowd_data = request.json
    return {"status": "updated"}

if __name__ == "__main__":
    app.run(port=5000)