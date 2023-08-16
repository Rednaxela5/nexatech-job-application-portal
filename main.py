import tkinter as tk
from gui.homepage.main import apply_home
from gui.admin_window.login import login_menu


# Main Window Constructor

root = tk.Tk() # Make temporary window for app to start
root.withdraw() # Hide temporary window

if __name__ == "__main__":
    login_menu()
    root.mainloop() # Start main window