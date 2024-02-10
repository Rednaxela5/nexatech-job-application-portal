from pathlib import Path
import sys
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, Label, Frame, ttk, messagebox
from default_entry import DefaultTextEntry
from _2_admin_edit_applicant import edit_applicant
import mysql.connector
import config as db_controller
from storage import applicant_data as ad

# Get the script's directory path
SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

# Set the relative path to the assets directory
ASSETS_PATH = SCRIPT_DIR / "assets" / "dash_frame3"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def edit_applicant_clicked(parent):
    edit_applicant(parent)

def filter_treeview_records(event):
    query = entry_1.get()
    applicant_table.delete(*applicant_table.get_children())
    applicant_data = db_controller.display_applicant_details(query)
    
    for row in applicant_data:
        # Check if query exists in any value from data
        if query.lower() in str(row).lower():
            applicant_table.insert('', 'end', values=row)

def on_table_select(event):
    button_1.config(state="normal")
    button_2.config(state="normal")

    try:
        applicant_table.select()[0]
    except:
        applicant_table.selection_id = None
        return
    
    # Get the selected item
    global item
    item = applicant_table.selection()[0]

    # Get the values of the selected item
    applicant_table.selection_id = applicant_table.item(item, "values")[0]




def applicant(parent):
    # --------------------------------------------------------------------------------#
    # ---------------------------------- GUI SETUP ---------------------------------- #
    # --------------------------------------------------------------------------------#

    # Defaul Text for each entry box
    d_search_entry = "Search applicant by name..."

    fontstyle = "Montserrat"

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

    global entry_1
    entry_1 = DefaultTextEntry(
        default_text=d_search_entry,
        bd=0,
        font=fontstyle,
        bg="#E7E7E7",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=662.0,
        y=155.0,
        width=310.0,
        height=35.0
    )

    entry_1.bind("<KeyRelease>", filter_treeview_records)

    global image_image_1
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        84.0,
        35.0,
        image=image_image_1
    )

    global image_image_2
    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        159.0,
        122.0,
        image=image_image_2
    )

    global image_image_3
    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        408.0,
        276.0,
        image=image_image_3
    )

    global entry_image_1
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        610.0,
        105.0,
        image=entry_image_1
    )

    

    global image_image_4
    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        430.0,
        105.0,
        image=image_image_4
    )

    global image_image_5
    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        136.0,
        96.0,
        image=image_image_5
    )

    global image_image_6
    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        145.0,
        119.0,
        image=image_image_6
    )

    # --------------------------------------------------------------------------------#
    # ---------------------------- TREEVIEW/TABLE SETUP ----------------------------- #
    # --------------------------------------------------------------------------------#
    global applicant_table
    applicant_table = ttk.Treeview(
        master=parent,
        columns=("ID", "Name", "Birthdate", "SSS ID", "Address"),
        height=12,
        show="headings",
    )

    #Define Column Headings
  
    # Configure Heading
    applicant_table.heading("ID", text="ID", anchor="center")
    applicant_table.heading("Name", text="Name", anchor="center")
    applicant_table.heading("Birthdate", text="Birthdate", anchor="center")
    applicant_table.heading("SSS ID", text="SSS ID", anchor="center")
    applicant_table.heading("Address", text="Address", anchor="center")


    # Configure Column Width
    applicant_table.column("ID", width=60, anchor="center")
    applicant_table.column("Name", width=100, anchor="w")
    applicant_table.column("Birthdate", width=90, anchor="center")
    applicant_table.column("SSS ID", width=100, anchor="center")
    applicant_table.column("Address", width=365, anchor="w")

    # Configure selected row color
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", font=("Montserrat", 10))
    style.configure("Treeview.Heading", background="#1a415a", fieldbackground="#1a415a", foreground="white", font=("Montserrat SemiBold", 11,))
    style.map("Treeview", background=[("selected", "#1a415a")])

    # Place the Table
    applicant_table.place(x=262, y=215)
    
    global applicant_data
    applicant_data = db_controller.display_applicant_details(None)

    for app_data in applicant_data:
        applicant_table.insert('', 'end', values=app_data)

    # Add Selection Event
    applicant_table.bind("<<TreeviewSelect>>", on_table_select)

    # Populate the table
    # --------------------------------------------------------------------------------#
    # ----------------------------------- BUTTONS ----------------------------------- #
    # --------------------------------------------------------------------------------#
    global button_image_1
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    
    global button_1
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        activebackground="#ffffff",
        cursor='hand2',
        relief="flat",
        state="disabled"
    )
    button_1.place(
        x=845.0,
        y=490.0,
        width=135.0,
        height=40.0
    )

    global button_image_2
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    
    global button_2
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: edit_applicant_clicked(parent),
        activebackground="#ffffff",
        cursor='hand2',
        relief="flat",
        state="disabled"
    )
    button_2.place(
        x=725.0,
        y=490.0,
        width=103.0,
        height=40.0
    )

    global image_image_7    
    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        411.0,
        139.0,
        image=image_image_7
    )

    