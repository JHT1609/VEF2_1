import os
from bottle import route, run

@route('/')
def index():
    return "<a href='/about'>About us</a>" \
            "<a href='/contact'>Contact</a>" \
            "<a href='/user'>Users</a>"

@route('/about')
def about():
    return "<h2>About us</h2>"

@route('/contact')
def about():
    return "<h2>Contact us</h2>"

@route('/users')
def about():
    return "<h2>Users</h2>"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
