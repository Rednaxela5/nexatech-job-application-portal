from pathlib import Path
import sys
import os
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from _5_0_hard_window import hard_main

def medium_main():
    # Get the script's directory path
    SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

    # Set the relative path to the assets directory
    ASSETS_PATH = SCRIPT_DIR / "assets" / "frame18"

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def easy_clicked():
        window.destroy()
        from _3_0_easy_window import easy_main
        easy_main()

    def hard_clicked():
        window.destroy()
        hard_main()
    window = Tk()

    def medium_1_clicked():
        window.destroy()
        from _4_1_mediumprob import medium_1_main
        medium_1_main()

    def medium_2_clicked():
        window.destroy()
        from _4_2_mediumprob import medium_2_main
        medium_2_main()

    def medium_3_clicked():
        window.destroy()
        from _4_3_mediumprob import medium_3_main
        medium_3_main()

    def medium_4_clicked():
        window.destroy()
        from _4_4_mediumprob import medium_4_main
        medium_4_main()

    def medium_5_clicked():
        window.destroy()
        from _4_5_mediumprob import medium_5_main
        medium_5_main()

    window.geometry("1024x568")
    window.configure(bg = "#CCD4D9")
    window.title("Nexatech System Administration")


    canvas = Canvas(
        window,
        bg = "#CCD4D9",
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
        512.0,
        22.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=easy_clicked,
        relief="flat"
    )
    button_1.place(
        x=31.0,
        y=72.0,
        width=113.0,
        height=44.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=hard_clicked,
        relief="flat"
    )
    button_2.place(
        x=861.0,
        y=72.0,
        width=114.0,
        height=44.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=medium_1_clicked,
        relief="flat"
    )
    button_3.place(
        x=196.0,
        y=192.0,
        width=280.0,
        height=70.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=medium_2_clicked,
        relief="flat"
    )
    button_4.place(
        x=548.0,
        y=192.0,
        width=280.0,
        height=70.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=medium_4_clicked,
        relief="flat"
    )
    button_5.place(
        x=548.0,
        y=290.0,
        width=280.0,
        height=70.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=medium_5_clicked,
        relief="flat"
    )
    button_6.place(
        x=372.0,
        y=394.0,
        width=280.0,
        height=70.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=medium_3_clicked,
        relief="flat"
    )
    button_7.place(
        x=196.0,
        y=290.0,
        width=280.0,
        height=70.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        532.0,
        96.0,
        image=image_image_2
    )
    window.resizable(False, False)
    window.mainloop()

# medium_main()