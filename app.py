from flask import Flask, render_template, request, url_for, flash, redirect, session, send_from_directory, abort, \
    jsonify
import os
import hashlib
import readdata as rd
# import accessspreadsheet as gd
from pathlib import Path
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath

app = Flask(__name__)
app.config['SECRET_KEY'] = "sdfsdfdfgdfgdsfgdfas"
getProducts = rd.getProducts()
getAllProducts = rd.get_all_products()
blog_data = rd.get_blogs()
# Fixing it UP

def parse(string):
    try:
        out = string.split(" ")
        return str(out[0]) + str(out[1])
    except IndexError:
        return string
@app.route("/")
def index():
    session['debug'] = True
    # data = rd.getProducts() just use getProducts fool. 
    session['products'] = [].extend(list(map(parse, getProducts["names"])))
    return render_template("index.html",urls = getProducts["ve-urls"], cost = getProducts["cost"], feature = getProducts["feature"], sale = getProducts["sale"], names = getProducts["names"], pictures = getProducts["pictures"], descriptions = getProducts['descriptions'])

@app.route("/about")
def about_us():
    people = rd.get_names()
    return render_template("about.html", people=people)

@app.route("/shop", methods=["GET", "POST"])
def shop():
    if request.method == "POST":
        name = request.form.get("type")
        if name == "all":
            return jsonify(data = getAllProducts)
        url = ""
        for index, product_name in enumerate(getProducts["names"]):
            if product_name == name:
                url = getProducts["urls"][index]
        print(url)
        info = rd.getProduct(url[1:])
        print(info)
        return jsonify(data = info)
    # data = rd.get_all_products() use getAllProducts Variable. 
    return render_template("shop.html", count = getAllProducts["count"], models = getAllProducts["model"], urls = getAllProducts["product-urls"],cost = getAllProducts["cost"], feature = getAllProducts["feature"], sale = getAllProducts["sale"], names = getAllProducts["product-names"], pictures = getAllProducts["product-pictures"], descriptions = getAllProducts['product-descriptions'])

@app.route("/contact")
def contact():
    return render_template("contact-us.html")

@app.route('/blog')
def blog():
    return render_template("blog.html",authors = blog_data["authors"], blog_names = blog_data["names"], blog_descriptions = blog_data["descriptions"], blog_pictures = blog_data["pictures"])
# @app.route("/update")
# def gatherdata():
#     gd.get_everything(False)
#     return redirect("/")

# @app.route("/super-update")
# def gatherpicturesanddata():
#     gd.get_everything(True)
#     return redirect("/")
if __name__ == '__main__':
    app.run(debug=True)