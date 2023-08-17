import tkinter as tk
from gui.homepage.main import apply_home
from gui.admin_window.main import login_menu
from tkinter import *
from pathlib import Path
import threading
# Main Window Constructor

root = tk.Tk() # Make temporary window for app to start
root.withdraw() # Hide temporary window

if __name__ == "__main__":
    apply_home()
    root.mainloop() # Start main window   