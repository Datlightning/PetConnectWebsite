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

UPLOADS_PATH = './static/images/'
ALLOWED_EXTENSIONS = {'jpg', 'png', 'webp'}

app = Flask(__name__)
app.config['SECRET_KEY'] = "verysecretkeyshhhh"
app.config['UPLOAD_FOLDER'] = UPLOADS_PATH

getPosts = rd.get_posts()
# Fixing it UP

@app.route("/", methods=["GET", "POST"])
def index():
    if(not session['creator']):
        return redirect("/post")
    getPosts = rd.get_posts()
    return render_template("index.html", posts=getPosts)


@app.route("/shop", methods=["GET", "POST"])
def shop():
    return render_template("shop.html")

@app.route("/signout")
def signout():
    session['logged_in'] = False
    session['user'] = None
    session["creator"] = None
    return redirect("/")

@app.route('/signup', methods=['GET', 'POST'])    
def account_creation():
    if session['logged_in']:
        return redirect("/")
    
    if request.method == 'POST':
        username = request.form.get('username')
        p1 = request.form.get("password")
        p2 = request.form.get("password2")
    
        if p1 != p2:
            return 'failure'
        else:
            rd.create_user(username, hashlib.sha256(p1.encode('utf-8')).hexdigest(), request.form.get("creator"))
            session['logged_in'] = True
            session['content'] = request.form.get("creator")
            session['user'] = username
            return 'success'
    else:
        return render_template('member-signup.html', error=False)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 
def extension(filename):
    return "." + filename.rsplit('.', 1)[1].lower() 

@app.route('/post', methods=['GET', 'POST'])
def post():
    if not session['logged_in']:
        return redirect("/signin")
    if request.method == "POST":
        post_name = request.form.get("label")
        if 'file' not in request.files:
            flash('No file part')
            return render_template('createpost.html')
        
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return render_template('createpost.html')
        if file and allowed_file(file.filename):
            file_extension = extension(file.filename)

            filename = secure_filename(file.filename)
            
            full_path = os.path.join(app.config['UPLOAD_FOLDER'], session['user'] + filename)
            file.save(full_path)
            rd.create_post(session['user'], post_name, session['user'] + filename)
            print(full_path)
    return render_template('createpost.html')

@app.route('/past', methods=["GET", "POST"])
def past():
    if not session['logged_in']:
        return redirect("/signin")
    specificPosts = rd.get_user_post(session['user'])
    return render_template("past.html", posts=specificPosts)

@app.route('/signin', methods=['GET', 'POST'])
def member_login():
    if session['logged_in']:
        return redirect("/")
    
    if request.method == 'POST':
        username = request.form.get('username')
        hash_pass = hashlib.sha256(request.form.get('password').encode('utf-8')).hexdigest()
        for name in rd.get_users():
            print(name)
            if username == name[0] and hash_pass == name[1]:
                session['logged_in'] = True
                session['user'] = username
                session['content'] = name[2]
                return 'success'
        else:
            return 'failure'
    else:
        return render_template('member-login.html', error=False)

@app.route('/<path:path>')
def catch_all(path):
        return render_template("404.html", back="Back to ParsippanyPointyApp", link = "/", text = "Page Not Found.")
if __name__ == '__main__':
    app.run(debug=True)