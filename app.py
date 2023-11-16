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

@app.route("/")
def index():
    session['debug'] = True
    session['products'] = []
    session['urls'] = []
    data = rd.getProducts()
    for i in range(len(data["names"])):
        session['products'].append(data["names"][i])
        session['urls'].append(data["urls"][i])
    return render_template("index.html",urls = data["urls"], names = data["names"], pictures = data["pictures"], descriptions = data['descriptions'])
@app.route("/petfeeder")
def petfeeder():
    return render_template("petfeeder.html")
@app.route("/gatherdata")
def gatherdata():
    gd.get_everything()
    return redirect("/")
if __name__ == '__main__':
    app.run(debug=True)