from flask import Flask, render_template, request, url_for, flash, redirect, session, send_from_directory, abort, \
    jsonify
import os
import hashlib
from pathlib import Path
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/products")
def productsPage(): 
    return render_template("products.html")


if __name__ == '__main__':
    app.run(debug=True)