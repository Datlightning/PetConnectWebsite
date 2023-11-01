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
    products = [
        "THIS IS A TEMPLATE FOR A PRODUCT BECAUSE I AM REALLY LAZY",
        "THIS IS A TEMPLATE FOR A PRODUCT BECAUSE I AM REALLY LAZY",
        "THIS IS A TEMPLATE FOR A PRODUCT BECAUSE I AM REALLY LAZY"
    ]
    description = [
        "MIGHT BE THE DUMBEST PRODUCT I HAVE EVER SEEN (RUTHVIK SAID THIS)",
        "the big BOX",
        "CHAT IS THIS REAL"
    ]
    names = [
        "PET UMBRELLA",
        "PET BOX",
        "PET SHOES"
    ]
    pictures = [
        "../static/images/petconnect_logo.png",
        "../static/images/petconnect_logo.png",
        "../static/images/petconnect_logo.png",
        "../static/images/petconnect_logo.png"
    ]


    return render_template("index.html", products = products, names = names, descriptions = description, pictures =pictures)

if __name__ == '__main__':
    app.run(debug=True)