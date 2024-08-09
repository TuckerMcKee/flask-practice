# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/math/<operation>')
def maths(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(math_dict[operation](a,b))

@app.route('/<operation>')
def do_maths(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])

    return str(math_dict[operation](a,b))

