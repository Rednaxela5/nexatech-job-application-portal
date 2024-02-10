
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alexa\Documents\GitHub\nexatech-job-application-form\tkintersample\build\assets\frame0")


def dash_main():
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("816x501")
    window.configure(bg = "#CCD4D9")


    canvas = Canvas(
        window,
        bg = "#CCD4D9",
        height = 501,
        width = 816,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        86.0,
        42.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        207.0,
        341.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        599.0,
        341.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        119.0,
        115.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        300.0,
        115.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        467.0,
        115.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        672.0,
        115.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        408.0,
        187.99999999999983,
        image=image_image_8
    )

    canvas.create_text(
        124.0,
        108.0,
        anchor="nw",
        text="120",
        fill="#0F2634",
        font=("Montserrat Bold", 40 * -1)
    )

    canvas.create_text(
        307.0,
        108.0,
        anchor="nw",
        text="58",
        fill="#0F2634",
        font=("Montserrat Bold", 40 * -1)
    )

    canvas.create_text(
        476.0,
        108.0,
        anchor="nw",
        text="62",
        fill="#0F2634",
        font=("Montserrat Bold", 40 * -1)
    )

    canvas.create_text(
        585.0,
        108.0,
        anchor="nw",
        text="₱ 62,300",
        fill="#0F2634",
        font=("Montserrat Bold", 40 * -1)
    )
    window.resizable(False, False)
    window.mainloop()