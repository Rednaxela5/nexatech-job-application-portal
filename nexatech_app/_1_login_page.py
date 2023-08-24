from pathlib import Path
import sys
import os
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from _2_main_menu import selection_main
from default_entry import DefaultTextEntry
from config import USERNAME, PASSWORD

def login_menu():
    # Get the script's directory path
    SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

    # Set the relative path to the assets directory
    ASSETS_PATH = SCRIPT_DIR / "assets" / "frame0"


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def login():
        username = username_entry.get()
        password = password_entry.get()

        if username == USERNAME and password == PASSWORD:
            # Close the login window
            window.destroy()

            # Open the main application window
            selection_main()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def return_home():
        window.destroy()
        from __1_apply_home_page import apply_home
        apply_home()

    def on_password_entry_enter(event):
        login()

    window = Tk()

    window.geometry("1024x568")
    window.configure(bg = "#0F2634")
    window.title("Nexatech System Administration")
    #window.iconbitmap(r"F:\Nexatech Application\test_run_4\build\assets\frame1\check_database.ico")


    canvas = Canvas(
        window,
        bg = "#0F2634",
        height = 568,
        width = 1024,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        266.0,
        207.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        267.0,
        123.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        266.0,
        166.0,
        image=image_image_3
    )

    canvas.create_rectangle(
        530.0,
        44.0,
        1024.0,
        568.0,
        fill="#CCD3D8",
        outline="")

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        777.0,
        161.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        659.0,
        295.0,
        image=image_image_5
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        777.0,
        251.0,
        image=entry_image_1
    )

    username_entry = DefaultTextEntry(
        default_text="Enter Username",
        font="Montserrat",
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    username_entry.place(
        x=642.0,
        y=230.0,
        width=270.0,
        height=40.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        777.0,
        325.0,
        image=entry_image_2
    )
    password_entry = DefaultTextEntry(
        # show="•",
        default_text="Enter Password",
        font="Montserrat",
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
    )

    password_entry.place(
        x=642.0,
        y=304.0,
        width=270.0,
        height=40.0
    )

    # Bind the <Return> event to the password_entry widget
    password_entry.bind("<Return>", on_password_entry_enter)

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        660.0,
        220.0,
        image=image_image_6
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=return_home,
        relief="flat"
    )
    button_1.place(
        x=166.0,
        y=491.0,
        width=178.0,
        height=33.0
)
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=login,
        relief="flat"
    )
    button_2.place(
        x=706.0,
        y=397.0,
        width=145.0,
        height=42.0
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        512.0,
        22.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        266.0,
        342.0,
        image=image_image_8
    )
    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    login_menu()