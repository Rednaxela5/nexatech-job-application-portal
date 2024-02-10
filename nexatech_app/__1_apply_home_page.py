from pathlib import Path
import sys
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage



def apply_home():
    # Get the script's directory path
    SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

    # Set the relative path to the assets directory
    ASSETS_PATH = SCRIPT_DIR / "assets" / "apply_frame0"


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def admin_control_clicked():
        # Close the login window
        window.destroy()
        # Open the main application window
        from _1_login_page import login_menu
        login_menu()

    def apply_now_clicked():
        window.destroy()
        from __2_apply_personal_info import personal_main
        a_window = Tk()
        a_window.geometry("1024x568")
        a_window.configure(bg = "#0F2634")
        a_window.title("Nexatech Job Application Form")
        a_window.resizable(False, False)
        icon_img = PhotoImage(file=relative_to_assets("job_logo.png"))
        a_window.iconphoto(False, icon_img)
        personal_main(a_window)

    # --------------------------------------------------------------------------------#
    # ---------------------------------- GUI SETUP ---------------------------------- #
    # --------------------------------------------------------------------------------#
    
    global window

    window = Tk()

    window.geometry("1024x568")
    window.configure(bg = "#0F2634")
    window.title("Nexatech Job Portal")

    icon_img = PhotoImage(file=relative_to_assets("job_logo.png"))
    window.iconphoto(False, icon_img)
    
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
        512.0,
        23.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        790.0,
        271.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        329.0,
        219.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        186.0,
        171.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        512.0,
        540.0,
        image=image_image_5
    )

    # Removed the following lines to remove the text for in partial fulfilment of the project requirements
    # image_image_6 = PhotoImage(
    #     file=relative_to_assets("image_6.png"))
    # image_6 = canvas.create_image(
    #     512.0,
    #     526.0,
    #     image=image_image_6
    # )

    # image_image_7 = PhotoImage(
    #     file=relative_to_assets("image_7.png"))
    # image_7 = canvas.create_image(
    #     512.0,
    #     546.0,
    #     image=image_image_7
    # )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        315.0,
        301.0,
        image=image_image_8
    )

    # --------------------------------------------------------------------------------#
    # ----------------------------------- BUTTONS ----------------------------------- #
    # --------------------------------------------------------------------------------#

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=admin_control_clicked,
        activebackground="#0F2634",
        cursor='hand2',
        relief="flat"
    )
    button_1.place(
        x=315.0,
        y=361.0,
        width=228.0,
        height=38.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=apply_now_clicked,
        activebackground="#0F2634",
        cursor='hand2',
        relief="flat"
    )
    button_2.place(
        x=68.0,
        y=361.0,
        width=228.0,
        height=38.0
    )

    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    apply_home()