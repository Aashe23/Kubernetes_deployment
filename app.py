
from flask import Flask

app = Flask(__name__)

@app.route("/wish")
def pleaseWish():
    return "Good Evening from Kubernetes!"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)#run our flask application
