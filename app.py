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
@app.route("/")
def index():
    session['debug'] = True
    session['products'] = []
    session['urls'] = []
    data = rd.getProducts()
    session['products'].extend(list(map(parse, data["names"])))
    session['urls'].extend(data["urls"])
    return render_template("index.html",urls = data["urls"], names = data["names"], pictures = data["pictures"], descriptions = data['long-desc'])
@app.route("/<pid>")
def umbrella(pid):
    data = rd.getProduct(pid)
    return render_template("product.html", urls = data['product-urls'], products = data["product-names"], name = data["name"], pictures = data["product-pictures"], description = data['product-descriptions'])
@app.route("/gatherdata")
def gatherdata():
    gd.get_everything()
    return redirect("/")
if __name__ == '__main__':
    app.run(debug=True)