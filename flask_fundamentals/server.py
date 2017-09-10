from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGES=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# string's color is so strange
app=Flask(__name__)
app.sercret_key="KeepItSecretKeepItSafe"

# does it really matter what string we put in sercret key?
# I failed. It says no secret is generated, but there is the key we set up at the beginning.
@app.route('/',method=['GET'])
# what's get method here for? Is it necessary? not other servers we build have that.
def index():
    return render_template('index.html')
app.sercret_key="afeafeagrewag/afe/af;eafok"
@app.route('/process',methods=['Post'])
def process():
    if len(request.form['name'])<1:
        flash("Name cannot be empty!")
    else:
        flash("Success! Your name is {}".format(request.form['name']))
    return redirect('/')
def submit():
    if len(request.form['email'])<1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('invalid Email Address!')
    else: 
        flash("Success")
    return redirect('/')
app.run(debug=True)