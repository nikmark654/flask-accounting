from pystray import Icon, Menu, MenuItem
from threading import Thread, Event
from flask import render_template

from myproject import server

@server.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    server.run(debug=True)