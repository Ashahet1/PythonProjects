from flask import Flask, jsonify
import random

app = Flask(__name__)

fruits = ["apple", "banana", "cherry", "mango", "grape"]

@app.route("/fruit", methods=["GET"])
def get_random_fruit():
    fruit = random.choice(fruits)
    return jsonify({"fruit": fruit})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)