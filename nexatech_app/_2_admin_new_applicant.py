from pathlib import Path
import sys
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, Label, Frame, ttk, messagebox
from storage import applicant_data as ad

# Get the script's directory path
SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

# Set the relative path to the assets directory
ASSETS_PATH = SCRIPT_DIR / "assets" / "dash_frame2"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def new_app(parent):


    def apply_now_clicked(parent):
        global current_window
        confirmation_message = "Do you want to go to Apply Now section?"

        confirm = messagebox.askyesno("Confirmation", confirmation_message)
        if confirm:
            from __2_apply_personal_info import personal_main
            ad.reset_values()
            personal_main(parent)
        else:
            pass

    canvas = Canvas(
        parent,
        bg = "#CCD4D9",
        height = 501,
        width = 816,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 209, y = 67)

    global image_image_1
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        105.0,
        35.0,
        image=image_image_1
    )

    global image_image_2
    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        408.0,
        270.0,
        image=image_image_2
    )

    global image_image_3
    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        408.0,
        360.0,
        image=image_image_3
    )

    global image_image_4
    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        408.0,
        292.0,
        image=image_image_4
    )

    global button_image_1
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: apply_now_clicked(parent),
        activebackground="#ffffff",
        cursor='hand2',
        relief="flat"
    )
    button_1.place(
        x=510.0,
        y=465.0,
        width=215.0,
        height=54.0
    )

    global button_image_hover_1
    button_image_hover_1 = PhotoImage(
        file=relative_to_assets("button_hover_1.png"))

    def button_1_hover(e):
        button_1.config(
            image=button_image_hover_1
        )
    def button_1_leave(e):
        button_1.config(
            image=button_image_1
        )

    button_1.bind('<Enter>', button_1_hover)
    button_1.bind('<Leave>', button_1_leave)


    global image_image_5
    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        408.0,
        187.0,
        image=image_image_5
    )

