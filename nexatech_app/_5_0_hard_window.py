from pathlib import Path
import sys
import os
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def hard_main():
    # Get the script's directory path
    SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

    # Set the relative path to the assets directory
    ASSETS_PATH = SCRIPT_DIR / "assets" / "frame19"

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def medium_clicked():
        window.destroy()
        from _4_0_medium_window import medium_main
        medium_main()

    def menu_clicked():
        window.destroy()
        from _2_main_menu import selection_main
        selection_main()
        
    def hard_1_clicked():
        window.destroy()
        from _5_1_hardprob import hard_1_main
        hard_1_main()
    
    def hard_2_clicked():
        window.destroy()
        from _5_2_hardprob import hard_2_main
        hard_2_main()
    
    def hard_3_clicked():
        window.destroy()
        from _5_3_hardprob import hard_3_main
        hard_3_main()
    
    def hard_4_clicked():
        window.destroy()
        from _5_4_hardprob import hard_4_main
        hard_4_main()
    
    def hard_5_clicked():
        window.destroy()
        from _5_5_hardprob import hard_5_main
        hard_5_main()
    
    window = Tk()

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
        command=hard_1_clicked,
        relief="flat"
    )
    button_1.place(
        x=209.0,
        y=177.0,
        width=249.0,
        height=70.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=hard_3_clicked,
        relief="flat"
    )
    button_2.place(
        x=209.0,
        y=275.0,
        width=249.0,
        height=70.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=hard_5_clicked,
        relief="flat"
    )
    button_3.place(
        x=387.0,
        y=390.0,
        width=249.0,
        height=70.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=hard_2_clicked,
        relief="flat"
    )
    button_4.place(
        x=567.0,
        y=177.0,
        width=249.0,
        height=70.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=hard_4_clicked,
        relief="flat"
    )
    button_5.place(
        x=567.0,
        y=275.0,
        width=249.0,
        height=70.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        511.0,
        97.0,
        image=image_image_2
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=medium_clicked,
        relief="flat"
    )
    button_6.place(
        x=35.0,
        y=75.0,
        width=136.0,
        height=44.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=menu_clicked,
        relief="flat"
    )
    button_7.place(
        x=876.0,
        y=75.0,
        width=113.0,
        height=44.0
    )
    window.resizable(False, False)
    window.mainloop()
# hard_main()