from flask import Flask, session, redirect, url_for, request, render_template, g

import storage

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["TESTING"] = True
app.config["DEVELOPMENT"] = True
app.config["CSRF_ENABLED"] = True
app.config["SECRET_KEY"] = b'\xdf\x8a\xf9@,\xe6\xc4\xe2\xfef\xf7\x17\xa7M\x0e9\xc0\xefj\xde\x96A\x96\x93p\x03~\x0b,\x85]~'

@app.route('/')
def hello():
    g.session = session
    return render_template("base.html")

@app.route('/login')
def login():
    session["username"] = "bepis"
    return "OK"

@app.route('/bepis')
def bepis():
    return "bepis"

if __name__ == '__main__':
    app.run()