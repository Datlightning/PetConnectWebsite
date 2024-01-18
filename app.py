import re
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
app.config['SECRET_KEY'] = "verysecretkeyshhhh"
getSignatureProducts = rd.getSignatureProducts()
getAllProducts = rd.get_all_products()
individualProducts = rd.getProductByType("individual")
product_lock = False
blog_data = rd.get_blogs()
# Fixing it UP

def parse(string):
    try:
        out = string.split(" ")
        return str(out[0]) + str(out[1])
    except IndexError:
        return string
def set_session():
    global product_lock
    if not product_lock:
        product_lock = True
@app.context_processor
def utility_processor():
    def get_session():
        return list(map(parse, getSignatureProducts["names"]))

    return dict(get_session=get_session)

@app.route("/", methods=["GET", "POST"])
def index():
    blog_data = rd.get_blogs()

    if request.method == "POST":
        id = request.form.get("id")
        return redirect(f"/blog/{id}")

    return render_template("index.html",ids = blog_data["recents"][:3] , blog_data = blog_data,urls = individualProducts["product-urls"], cost = individualProducts["cost"], feature = individualProducts["feature"], sale = individualProducts["sale"], names = individualProducts["product-names"], pictures = individualProducts["product-pictures"], descriptions = individualProducts['product-descriptions'])

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
            return jsonify(data = info)
    # data = rd.get_all_products() use getAllProducts Variable. 
    return render_template("shop.html", models = getAllProducts["model"], urls = getAllProducts["product-urls"],cost = getAllProducts["cost"], feature = getAllProducts["feature"], sale = getAllProducts["sale"], names = getAllProducts["product-names"], pictures = getAllProducts["product-pictures"], descriptions = getAllProducts['product-descriptions'])

@app.route("/contact", methods=["POST","GET"])
def contact():
    return render_template("contact-us.html")

@app.route('/blog/<blogid>')
def blog_specific(blogid):
    blog_data = rd.get_blogs()
    if blogid not in blog_data["ids"]:
        return render_template("404.html", text="Blog Not Found.", link="/blog", back="Back to Blogs")
    views = blog_data["views"][blogid]
    rd.add_view(blogid)
    if views == 1:
        text = "1 View."
    else:
        text = f"{views} Views."
    return render_template("blog-specific.html",type = blog_data["type"][blogid], picture_description = blog_data["picture-descriptions"][blogid], view_text = text, focus_id = blogid, id = blog_data["ids"][blogid], author = blog_data["authors"][blogid], blog_name = blog_data["names"][blogid], blog_description = blog_data["descriptions"][blogid], blog_picture = blog_data["pictures"][blogid])

@app.route('/blog')
def blog():
    blog_data = rd.get_blogs()

    return render_template("blog.html", focus_id = "1", ids = blog_data["recents"], blog_data = blog_data)


@app.route("/shop/<product>", methods  = ["GET", "POST"])
def shop_specific(product):
    for index, product_name in enumerate(getSignatureProducts["names"]):
            if product_name == product:
                url = getSignatureProducts["urls"][index]
                break
    else:
        return render_template("404.html", text="Item Not Found.", link="/shop", back="Back to Shop")

    info = rd.getProduct(url[1:])

    if request.method == "POST":
        name = int(request.form.get("type"))
        if name >= len(info["cost"]):
            data = {"redirect":f"/shop/{product}/{index}"}
            return jsonify(data)
        
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
            "url":url,
            "redirect":""
        }
        return jsonify(output)
                
    return render_template("shop-detail.html", product_options = info["options"], name = product, product_names = info["product-names"], product_pictures = info["product-pictures"], product_urls = info["product-urls"], product_descriptions = info["product-descriptions"], product_costs = info["cost"])
@app.route("/social")
def social():
    return render_template("social.html")
@app.route('/<path:path>')
def catch_all(path):
        return render_template("404.html", back="Back to PetConnect", link = "/", text = "Page Not Found.")
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