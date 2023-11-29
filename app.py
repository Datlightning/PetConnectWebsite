from flask import Flask, render_template, request, url_for, flash, redirect, session, send_from_directory, abort, \
    jsonify
import os
import hashlib
import readdata as rd
import accessspreadsheet as gd
from pathlib import Path
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath

app = Flask(__name__)
app.config['SECRET_KEY'] = "sfdlkfjsdvpc23402938fsdflkmasdlsfds"
def parse(string):
    try:
        out = string.split(" ")
        print(out)
        return str(out[0]) + str(out[1])
    except IndexError:
        return string
@app.route("/", methods = ["GET"])
def index():
    if request.method == "GET":
        data = rd.getProducts()
        return jsonify(data)
    return jsonify({"error": "some descriptive error that is useful for debugging"})

if __name__ == '__main__':
    app.run(debug=True)