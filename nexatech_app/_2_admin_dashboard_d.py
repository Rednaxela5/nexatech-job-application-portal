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

def fetch_data():
    # Connect to MySQL database
    conn = db_controller.connect_to_mysql()
    if conn is None:
        return []

    cursor = conn.cursor()
    cursor.callproc('CountJobPos')
    
    # Fetch all rows
    rows = cursor.fetchall()
    conn.close()
    
    return rows

# def populate_table():
#     # Clear existing data
#     for row in tree.get_children():
#         tree.delete(row)
    
#     # Fetch data from the database
#     data = fetch_data()
    
#     # Insert fetched data into the table
#     for row in data:
#         tree.insert('', 'end', values=row)

def dash(parent):

    # --------------------------------------------------------------------------------#
    # ---------------------------------- GUI SETUP ---------------------------------- #
    # --------------------------------------------------------------------------------# 

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


    # --------------------------------------------------------------------------------#
    # ---------------------------- TREEVIEW/TABLE SETUP ----------------------------- #
    # --------------------------------------------------------------------------------#

    # ============================ JOB POSITIONS TABLE ============================ #
    job_pos_table = ttk.Treeview(
        master=parent, 
        columns=('Job Position', 'Total'), 
        height=8, 
        show='headings'
    )

    # Define column headings
    job_pos_table.heading('#0', text='Job Position')
    job_pos_table.heading('#1', text='Total')
    
    # Configure heading
    job_pos_table.heading("Job Position", text="Job Position", anchor="center")
    job_pos_table.heading("Total", text="Total", anchor="center")

    #Configure column width
    job_pos_table.column("Job Position", width=210)
    job_pos_table.column("Total", width=110, anchor="center")

    # Configure selected row color
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", font=("Montserrat", 10))
    style.configure("Treeview.Heading", background="#1a415a", fieldbackground="#1a415a", foreground="white", font=("Montserrat SemiBold", 11,))
    style.map("Treeview", background=[("selected", "#1a415a")])

    # Place the table
    job_pos_table.place(x=253.0, y=324.0)

    # Populate the table
    common_count_job_data = db_controller.count_common_job_pos()

    for job_data in common_count_job_data:
        job_pos_table.insert('', 'end', values=job_data)


    # ==================== COMMON SKILLS TABLE ==================== #
    common_skills_table = ttk.Treeview(
        master=parent, 
        columns=('Skill Name', 'Total'), 
        height=8, 
        show='headings'
    )

    # Define column headings
    common_skills_table.heading('#0', text='Skill Name')
    common_skills_table.heading('#1', text='Total')

    # Configure heading
    common_skills_table.heading("Skill Name", text="Skill Name", anchor="center")
    common_skills_table.heading("Total", text="Total", anchor="center")

    #Configure column width
    common_skills_table.column("Skill Name", width=220)
    common_skills_table.column("Total", width=110, anchor="center")

    # Place the table
    common_skills_table.place(x=640.0, y=324.0)

    # Populate the Common Skills Table
    common_count_skills_data = db_controller.count_common_skills()

    for skill_data in common_count_skills_data:
        common_skills_table.insert('', 'end', values=skill_data)