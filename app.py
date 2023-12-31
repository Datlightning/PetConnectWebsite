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
@app.route("/", methods=["GET", "POST"])
def index():
    session['debug'] = True
    if request.method == "POST":
        id = request.form.get("id")
        print(id)
        return redirect(f"/blog/{id}")


    session['products'] = [].extend(list(map(parse, getProducts["names"])))
    return render_template("index.html",ids = blog_data["ids"][:3], authors = blog_data["authors"][:3], blog_names = blog_data["names"][:3], blog_descriptions = blog_data["descriptions"][:3], blog_pictures = blog_data["pictures"][:3],urls = getProducts["ve-urls"], cost = getProducts["cost"], feature = getProducts["feature"], sale = getProducts["sale"], names = getProducts["names"], pictures = getProducts["pictures"], descriptions = getProducts['descriptions'])

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
        else:
            info = rd.getProductByType(name)
            print(info)
            return jsonify(data = info)
    # data = rd.get_all_products() use getAllProducts Variable. 
    return render_template("shop.html", models = getAllProducts["model"], urls = getAllProducts["product-urls"],cost = getAllProducts["cost"], feature = getAllProducts["feature"], sale = getAllProducts["sale"], names = getAllProducts["product-names"], pictures = getAllProducts["product-pictures"], descriptions = getAllProducts['product-descriptions'])

@app.route("/contact", methods=["POST","GET"])
def contact():
    return render_template("contact-us.html")

@app.route('/blog/<blogid>')
def blog_specific(blogid):
    return render_template("blog.html", focus_id = blogid, ids = blog_data["ids"], authors = blog_data["authors"], blog_names = blog_data["names"], blog_descriptions = blog_data["descriptions"], blog_pictures = blog_data["pictures"])

@app.route('/blog')
def blog():
    return render_template("blog.html", focus_id = "1", ids = blog_data["ids"], authors = blog_data["authors"], blog_names = blog_data["names"], blog_descriptions = blog_data["descriptions"], blog_pictures = blog_data["pictures"])


@app.route("/shop/<product>", methods  = ["GET", "POST"])
def shop_specific(product):
    for index, product_name in enumerate(getProducts["names"]):
            if product_name == product:
                url = getProducts["urls"][index]
    info = rd.getProduct(url[1:])

    if request.method == "POST":
        name = int(request.form.get("type"))
        
        
        cost = info["cost"][name]
        description = info["product-descriptions"][name]
        picture = info["product-pictures"][name]
        url = info['product-urls'][name]
        name = info["product-names"][name]

        output = {
            "cost":cost,
            "description":description,
            "name":name,
            "picture":picture,
            "url":url
        }
        print(output)
        return jsonify(output)
                
    print(info)
    return render_template("shop-detail.html", product_options = info["options"], name = product, product_names = info["product-names"], product_pictures = info["product-pictures"], product_urls = info["product-urls"], product_descriptions = info["product-descriptions"], product_costs = info["cost"])
@app.route("/social")
def social():
    return render_template("social.html")
@app.route("/<idk>")
def unknown(idk):
    return render_template("404.html")
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