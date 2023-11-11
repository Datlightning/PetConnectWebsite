from flask import Flask, render_template, request, url_for, flash, redirect, session, send_from_directory, abort, \
    jsonify
import os
import hashlib
import readdata as rd
from pathlib import Path
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath

app = Flask(__name__)

@app.route("/")
def index():
   
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
        "petconnect_logo.png",
        "petconnect_logo.png",
        "petconnect_logo.png",
        "petconnect_logo.png"
    ]
    

    data = rd.getProducts()
    return render_template("index.html",urls = data["urls"], names = data["names"], pictures = data["pictures"], descriptions = data['descriptions'])
@app.route("/petumbrella")
def umbrella():
    data = rd.getProducts()
    index = 0
    for i in data["names"]:
        if "umbrella" in i.lower():
            break
        index += 1
    return render_template("petumbrella.html", name = data["names"][index])
@app.route("/petshoes")
def shoes():
    data = rd.getProducts()
    index = 0
    for i in data["names"]:
        if "shoe" in i.lower():
            break
        index += 1
    return render_template("product.html", name = data["names"][index])
@app.route("/petfeeder")
def feeder():
    data = rd.getProducts()
    index = 0
    for i in data["names"]:
        if "feed" in i.lower():
            break
        index += 1
    return render_template("product.html", name = data["names"][index])
if __name__ == '__main__':
    app.run(debug=True)