# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/<operation>')
def maths(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    return operation(a,b)

