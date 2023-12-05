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
app.config['SECRET_KEY'] = "sdfsdfdfgdfgdsfgdfas"
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
    return render_template("index.html",cost = data["cost"], feature = data["feature"], sale = data["sale"], names = data["names"], pictures = data["pictures"], descriptions = data['descriptions'])

@app.route("/about")
def about_us():
    return render_template("about.html")

@app.route("/shop")
def shop():
    data = rd.get_all_products()
    return render_template("shop.html",urls = data["product-urls"],cost = data["cost"], feature = data["feature"], sale = data["sale"], names = data["product-names"], pictures = data["product-pictures"], descriptions = data['product-descriptions'])

@app.route("/contact")
def contact():
    return render_template("contact-us.html")
@app.route("/update")
def gatherdata():
    gd.get_everything(False)
    return redirect("/")

@app.route("/super-update")
def gatherpicturesanddata():
    gd.get_everything(True)
    return redirect("/")
if __name__ == '__main__':
    app.run(debug=True)