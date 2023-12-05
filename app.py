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
getProducts = rd.getProducts()
getAllProducts = rd.get_all_products()
# Fixing it UP

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
    # data = rd.getProducts() just use getProducts fool. 
    session['products'] = [].extend(list(map(parse, getProducts["names"])))
    session['urls'] = [].extend(getProducts["urls"])
    return render_template("index.html",cost = getProducts["cost"], feature = getProducts["feature"], sale = getProducts["sale"], names = getProducts["names"], pictures = getProducts["pictures"], descriptions = getProducts['descriptions'])

@app.route("/about")
def about_us():
    return render_template("about.html")

@app.route("/shop")
def shop():
    # data = rd.get_all_products() use getAllProducts Variable. 
    return render_template("shop.html",urls = getAllProducts["product-urls"],cost = getAllProducts["cost"], feature = getAllProducts["feature"], sale = getAllProducts["sale"], names = getAllProducts["product-names"], pictures = getAllProducts["product-pictures"], descriptions = getAllProducts['product-descriptions'])

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