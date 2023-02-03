from flask import Flask, request
import database

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/track", methods=["POST"])
def track():
    data = request.get_json()
    database.save_data(data)
    return "Data saved."

if __name__ == "__main__":
    app.run()
