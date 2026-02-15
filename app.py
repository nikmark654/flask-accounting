from pystray import Icon, Menu, MenuItem
from PIL import Image
from threading import Thread, Event
from flask import render_template

import os

from myproject import server

@server.route('/')
def index():
    return render_template('home.html')

def bootstrap_subthreads(icon):
    global server_thread
    server_thread = Thread(target=server.run)
    server_thread.start()

def create_image():
    """Create a simple icon image"""
    return Image.new('RGB', (64, 64), color='red')

def quit_app(icon, item):
    icon.stop()
    os._exit(0)

if __name__ == '__main__':
    app_menu = Menu(
        MenuItem('Quit', quit_app)
    )
    app = Icon('Accounting', create_image(), menu = app_menu)
    app.visible = True  # Add this
    app.run(setup = bootstrap_subthreads)