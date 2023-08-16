import tkinter as tk
from gui.homepage.__1_apply_home_page import apply_home
from gui.admin_window._1_login_page import login_menu


# Main Window Constructor

root = tk.Tk() # Make temporary window for app to start
root.withdraw() # Hide temporary window

if __name__ == "__main__":
    login_menu()
    root.mainloop() # Start main window