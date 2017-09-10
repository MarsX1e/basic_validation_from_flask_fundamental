from flask import Flask, render_template, redirect, request, session
app=Flask(__name__)
app.sercret_key="KeepItSecretKeepItSafe"
# does it really matter what string we put in sercret key?
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process',methods=['Post'])
def process():
    return redirect('/')
app.run(debug=True)