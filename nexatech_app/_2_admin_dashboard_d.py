from pathlib import Path
import sys
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, Label, Frame, ttk, messagebox
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
import mysql.connector
import config as db_controller

# Get the script's directory path
SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

# Set the relative path to the assets directory
ASSETS_PATH = SCRIPT_DIR / "assets" / "dash_frame1"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def dash(parent):
    

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
        190.0,
        105.0,
        anchor="ne",
        text=db_controller.tot_applicant(),
        fill="#0F2634",
        font=("Montserrat", 25, "bold")
    )

    canvas.create_text(
        355.0,
        105.0,
        anchor="ne",
        text=db_controller.full_time(),
        fill="#0F2634",
        font=("Montserrat", 25, "bold")
    )

    canvas.create_text(
        525.0,
        105.0,
        anchor="ne",
        text=db_controller.part_time(),
        fill="#0F2634",
        font=("Montserrat", 25, "bold")
    )

    canvas.create_text(
        770.0,
        105.0,
        anchor="ne",
        text="₱{:,.0f}".format(db_controller.avg_des_sal()),
        fill="#0F2634",
        font=("Montserrat", 25, "bold")
    )


    # job_pos_table = ttk.Treeview(
    #     parent,
    #     columns=("Job Position", "Number of Applicants"),
    #     show="headings"
    # )

    # job_pos_table.place(x=209, y=341)

    table_columns = ["Job Position", "Total Count"]
    # Create a treeview (table)
    tree = ttk.Treeview(parent, columns=table_columns, show="headings")

    # Define column headings
    tree.heading("#0", text="Job Position", anchor="center")
    tree.heading("#1", text="Total Count", anchor="center")

    
    for column in table_columns:
        tree.heading(column=column, text=column)
        tree.column(column=column, width=70)

    
    # Configure header color
    tree["style"] = "mystyle.Treeview"
    style = ttk.Style()
    style.theme_use("default")
    style.configure("mystyle.Treeview.Heading", background="#4a6778", foreground="white")

    # Configure selected row color
    style.map("Treeview", background=[("selected", "#ccd4d9")])

    tree.place(x=209, y=310)
