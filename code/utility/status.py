
from flask import Flask

app = Flask(__name__)

serverName ="my server"

@app.route("/")
def index():
    return "This server is UP"
@app.route("/info")
def info():
    return "This is " + serverName

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0",port=5000)
