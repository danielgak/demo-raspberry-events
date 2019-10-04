from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/request', methods=['GET'])
def test():
    return "This is a succesfull get"