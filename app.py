from pystray import Icon, Menu, MenuItem
from PIL import Image
from threading import Thread
import webbrowser

import os

from myproject import server

def bootstrap_subthreads(icon):
    global server_thread
    server_thread = Thread(target=server.run, kwargs={"debug": False})
    server_thread.start()

def create_image():
    """Create a simple icon image"""
    return Image.new('RGB', (64, 64), color='red')

def quit_app(icon, item):
    icon.stop()
    os._exit(0)

if __name__ == '__main__':
    
    app_menu = Menu(
        MenuItem('Open Interface', lambda: webbrowser.open("http://127.0.0.1:5000/")),
        MenuItem('Quit', quit_app)
    )

    app = Icon('Accounting', create_image(), menu = app_menu)
    app.visible = True
    app.run(setup = bootstrap_subthreads)