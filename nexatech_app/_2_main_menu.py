from pathlib import Path
import sys
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from _3_0_easy_window import easy_main
from _4_0_medium_window import medium_main
from _5_0_hard_window import hard_main

def selection_main():
    # Get the script's directory path
    SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

    # Set the relative path to the assets directory
    ASSETS_PATH = SCRIPT_DIR / "assets" / "frame1"

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def easy_clicked():
        window.destroy()
        easy_main()
        
    def medium_clicked():
        window.destroy()
        medium_main()

    def hard_clicked():
        window.destroy()
        hard_main()

    def home_clicked():
        window.destroy()
        from __1_apply_home_page import apply_home
        apply_home()

    def logout_clicked():
        window.destroy()
        from _1_login_page import login_menu
        login_menu()

    window = Tk()

    window.geometry("1024x568")
    window.configure(bg = "#CCD4D9")
    window.title("Nexatech System Administration")
    #window.iconbitmap(r"F:\Nexatech Application\test_run_4\build\assets\frame1\check_database.ico")

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
        x=81.0,
        y=169.0,
        width=250.0,
        height=79.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=medium_clicked,
        relief="flat"
    )
    button_2.place(
        x=81.0,
        y=288.0,
        width=250.0,
        height=79.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=hard_clicked,
        relief="flat"
    )
    button_3.place(
        x=81.0,
        y=412.0,
        width=250.0,
        height=79.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=home_clicked,
        relief="flat"
    )
    button_4.place(
        x=21.0,
        y=72.0,
        width=75.0,
        height=29.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=logout_clicked,
        relief="flat"
    )
    button_5.place(
        x=913.0,
        y=71.0,
        width=91.0,
        height=30.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        512.0,
        86.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        662.0,
        206.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        478.0,
        321.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        630.0,
        448.0,
        image=image_image_5
    )
    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    selection_main()