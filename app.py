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
    data = rd.getProduct("umbrella")
  
    return render_template("product.html", products = data["product-names"], name = data["name"], pictures = data["product-pictures"], description = data['product-descriptions'])
@app.route("/petshoes")
def shoes():
    data = rd.getProduct("shoe")
  
    return render_template("product.html", products = data["product-names"], name = data["name"], pictures = data["product-pictures"], description = data['product-descriptions'])
@app.route("/petfeeder")
def feeder():
    data = rd.getProduct("feed")
  
    return render_template("product.html", products = data["product-names"], name = data["name"], pictures = data["product-pictures"], description = data['product-descriptions'])
if __name__ == '__main__':
    app.run(debug=True)