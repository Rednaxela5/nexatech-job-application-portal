from pathlib import Path
import sys
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, Label, Frame, ttk, messagebox







def dash(parent):
    # Get the script's directory path
    SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

    # Set the relative path to the assets directory
    ASSETS_PATH = SCRIPT_DIR / "assets" / "dash_frame1"


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    canvas = Canvas(
        parent,
        bg = "#ccd4d9",
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
        86.0,
        35.0,
        image=image_image_1
    )

    global image_image_2
    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        207.0,
        341.0,
        image=image_image_2
    )

    global image_image_3
    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        599.0,
        341.0,
        image=image_image_3
    )

    global image_image_4
    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        119.0,
        115.0,
        image=image_image_4
    )

    global image_image_5
    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        300.0,
        115.0,
        image=image_image_5
    )

    global image_image_6
    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        467.0,
        115.0,
        image=image_image_6
    )

    global image_image_7
    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        672.0,
        115.0,
        image=image_image_7
    )

    global image_image_8
    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        408.0,
        187.99999999999983,
        image=image_image_8
    )


    canvas.create_text(
        124.0,
        100.0,
        anchor="nw",
        text="120",
        fill="#0F2634",
        font=("Montserrat", 30, "bold")
    )

    canvas.create_text(
        307.0,
        100.0,
        anchor="nw",
        text="58",
        fill="#0F2634",
        font=("Montserrat", 30, "bold")
    )

    canvas.create_text(
        476.0,
        100.0,
        anchor="nw",
        text="62",
        fill="#0F2634",
        font=("Montserrat", 30, "bold")
    )

    canvas.create_text(
        585.0,
        100.0,
        anchor="nw",
        text="₱ 62,300",
        fill="#0F2634",
        font=("Montserrat", 30, "bold")
    )

