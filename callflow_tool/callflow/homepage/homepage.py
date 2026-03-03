from flask import render_template, Flask, request, jsonify, redirect
from flask_cors import CORS
import  re
import json
import paramiko
import random
import time
import os


import requests
app = Flask(__name__, static_folder="/home/pgokhe/venv/callflow/homepage/template", template_folder="/home/pgokhe/venv/callflow/homepage/template")

@app.route('/', methods=["GET", "POST"])
def homepage():
    print("HELLO")
    return render_template("homepage.html")


if __name__ == '__main__':
	app.run(host="10.133.99.221", port=6509)
