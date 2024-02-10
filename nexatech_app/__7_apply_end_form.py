from pathlib import Path
import sys
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from storage import applicant_data as ad, school_data_1 as sd1, school_data_2 as sd2, school_data_3 as sd3, work_data_1 as wd1, work_data_2 as wd2, work_data_3 as wd3, skill_data_1 as md1, skill_data_2 as md2, skill_data_3 as md3, skill_data_4 as md4, skill_data_5 as md5, skill_data_6 as md6

# Get the script's directory path
SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

# Set the relative path to the assets directory
ASSETS_PATH = SCRIPT_DIR / "assets" / "apply_frame6"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def return_home_clicked(parent):
    # Empty the values in the applicant_data
    ad.reset_values()

    # Empty the values in the school_data
    sd1.reset_values()
    sd2.reset_values()
    sd3.reset_values()

    # Empty the values in the work_data
    wd1.reset_values()
    wd2.reset_values()
    wd3.reset_values()

    # Empth the values in the skill_data
    md1.reset_values()
    md2.reset_values()
    md3.reset_values()
    md4.reset_values()
    md5.reset_values()
    md6.reset_values()
    
    parent.destroy()
    from __1_apply_home_page import apply_home
    apply_home()


def end_application_main(parent):


    canvas = Canvas(
        parent,
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
        23.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        511.0,
        107.0,
        image=image_image_2
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#ccd4d9",
        cursor='hand2',
        command=lambda: return_home_clicked(parent),
        relief="flat"
    )
    button_1.place(
        x=325.0,
        y=423.0,
        width=373.0,
        height=50.0
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        512.0,
        181.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        511.0,
        308.0,
        image=image_image_4
    )

    parent.mainloop()

