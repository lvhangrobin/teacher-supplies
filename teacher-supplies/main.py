from flask import Flask, render_template, redirect, request, url_for, session, flash, g
from random import shuffle
import os

# create the application object
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "Hello World!"

def shuffle(lst):
    shuffle(lst)
    return lst


if __name__ == '__main__':
    app.run()