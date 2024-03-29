from pathlib import Path
import sys
from tkinter import Tk, ttk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from default_entry import DefaultTextEntry
import tkinter as tk
from tkcalendar import DateEntry
import datetime
import mysql.connector
from storage import applicant_data as ad, school_data_1 as sd1, school_data_2 as sd2, school_data_3 as sd3, work_data_1 as wd1, work_data_2 as wd2, work_data_3 as wd3
from storage import skill_data_1 as sn1, skill_data_2 as sn2, skill_data_3 as sn3, skill_data_4 as sn4, skill_data_5 as sn5, skill_data_6 as sn6
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
from sql_connection import connection_database

# Get the script's directory path
SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

# Set the relative path to the assets directory
ASSETS_PATH = SCRIPT_DIR / "assets" / "apply_frame5"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
        return conn
    except mysql.connector.Error as err:
        print("Error connecting to MySQL:", err)
        return None

def fetch_skill_data():
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("SELECT skillName FROM skills_db ORDER BY skillName ASC")
    skill_data = cursor.fetchall()
    cursor.close()
    return skill_data

def back_cliked(parent):
    skill_name_1 = skill_1_var.get()
    skill_name_2 = skill_2_var.get()
    skill_name_3 = skill_3_var.get()
    skill_name_4 = skill_4_var.get()
    skill_name_5 = skill_5_var.get()
    skill_name_6 = skill_6_var.get()
    
    if skill_name_4 == d_skill_4_entry and skill_name_5 == d_skill_5_entry and skill_name_6 == d_skill_6_entry:
        sn1.skill_name = skill_name_1
        sn2.skill_name = skill_name_2
        sn3.skill_name = skill_name_3


        # For Debugging Purposes
        # print(sn1.skill_name)
        # print(sn2.skill_name)
        # print(sn3.skill_name)
    elif skill_name_4 != d_skill_4_entry and skill_name_5 == d_skill_5_entry and skill_name_6 == d_skill_6_entry:
        sn1.skill_name = skill_name_1
        sn2.skill_name = skill_name_2
        sn3.skill_name = skill_name_3
        sn4.skill_name = skill_name_4

        # For Debugging Purposes
        # print(sn1.skill_name)
        # print(sn2.skill_name)
        # print(sn3.skill_name)
        # print(sn4.skill_name)
    elif skill_name_4 == d_skill_4_entry and skill_name_5 != d_skill_5_entry and skill_name_6 == d_skill_6_entry:
        sn1.skill_name = skill_name_1
        sn2.skill_name = skill_name_2
        sn3.skill_name = skill_name_3
        sn5.skill_name = skill_name_5


        # For Debugging Purposes
        # print(sn1.skill_name)
        # print(sn2.skill_name)
        # print(sn3.skill_name)
        # print(sn5.skill_name)
    elif skill_name_4 == d_skill_4_entry and skill_name_5 == d_skill_5_entry and skill_name_6 != d_skill_6_entry:
        sn1.skill_name = skill_name_1
        sn2.skill_name = skill_name_2
        sn3.skill_name = skill_name_3
        sn6.skill_name = skill_name_6

        # For Debugging Purposes
        # print(sn1.skill_name)
        # print(sn2.skill_name)
        # print(sn3.skill_name)
        # print(sn6.skill_name)
    elif skill_name_4 == d_skill_4_entry and skill_name_5 != d_skill_5_entry and skill_name_6 != d_skill_6_entry:
        sn1.skill_name = skill_name_1
        sn2.skill_name = skill_name_2
        sn3.skill_name = skill_name_3
        sn5.skill_name = skill_name_5
        sn6.skill_name = skill_name_6
        # For Debugging Purposes
        # print(sn1.skill_name)
        # print(sn2.skill_name)
        # print(sn3.skill_name)
        # print(sn5.skill_name)
        # print(sn6.skill_name)
    elif skill_name_4 != d_skill_4_entry and skill_name_5 != d_skill_5_entry and skill_name_6 != d_skill_6_entry:
        sn1.skill_name = skill_name_1
        sn2.skill_name = skill_name_2
        sn3.skill_name = skill_name_3
        sn4.skill_name = skill_name_4
        sn5.skill_name = skill_name_5
        sn6.skill_name = skill_name_6
        # For Debugging Purposes
        # print(sn1.skill_name)
        # print(sn2.skill_name)
        # print(sn3.skill_name)
        # print(sn4.skill_name)
        # print(sn5.skill_name)
        # print(sn6.skill_name)


    from __5_apply_work_exp import work_experience_main
    work_experience_main(parent)

def submit_clicked(parent):
    skill_name_1 = skill_1_var.get()
    skill_name_2 = skill_2_var.get()
    skill_name_3 = skill_3_var.get()
    skill_name_4 = skill_4_var.get()
    skill_name_5 = skill_5_var.get()
    skill_name_6 = skill_6_var.get()

    confirmation_message = "Are you sure you want to submit?"

    # Check for duplicate skills
    skill_list = [skill_name_1, skill_name_2, skill_name_3, skill_name_4, skill_name_5, skill_name_6]
    
    if skill_name_1 == d_skill_1_entry or skill_name_2 == d_skill_2_entry or skill_name_3 == d_skill_3_entry:
        messagebox.showerror("Error", "Please select at least three major skills")
    elif len(skill_list) != len(set(skill_list)):
        messagebox.showerror("Error", "Duplicate skills found")
    else:
        confirm = messagebox.askyesno("Confirmation", confirmation_message)
        if confirm:
            if skill_name_4 == d_skill_4_entry and skill_name_5 == d_skill_5_entry and skill_name_6 == d_skill_6_entry:
                sn1.skill_name = skill_name_1
                sn2.skill_name = skill_name_2
                sn3.skill_name = skill_name_3
                # For Debugging Purposes
                # print(sn1.skill_name)
                # print(sn2.skill_name)
                # print(sn3.skill_name)
            elif skill_name_4 != d_skill_4_entry and skill_name_5 == d_skill_5_entry and skill_name_6 == d_skill_6_entry:
                sn1.skill_name = skill_name_1
                sn2.skill_name = skill_name_2
                sn3.skill_name = skill_name_3
                sn4.skill_name = skill_name_4
                # For Debugging Purposes
                # print(sn1.skill_name)
                # print(sn2.skill_name)
                # print(sn3.skill_name)
                # print(sn4.skill_name)
            elif skill_name_4 == d_skill_4_entry and skill_name_5 != d_skill_5_entry and skill_name_6 == d_skill_6_entry:
                sn1.skill_name = skill_name_1
                sn2.skill_name = skill_name_2
                sn3.skill_name = skill_name_3
                sn5.skill_name = skill_name_5
                # For Debugging Purposes
                # print(sn1.skill_name)
                # print(sn2.skill_name)
                # print(sn3.skill_name)
                # print(sn5.skill_name)
            elif skill_name_4 == d_skill_4_entry and skill_name_5 == d_skill_5_entry and skill_name_6 != d_skill_6_entry:
                sn1.skill_name = skill_name_1
                sn2.skill_name = skill_name_2
                sn3.skill_name = skill_name_3
                sn6.skill_name = skill_name_6
                # For Debugging Purposes
                # print(sn1.skill_name)
                # print(sn2.skill_name)
                # print(sn3.skill_name)
                # print(sn6.skill_name)
            elif skill_name_4 == d_skill_4_entry and skill_name_5 != d_skill_5_entry and skill_name_6 != d_skill_6_entry:
                sn1.skill_name = skill_name_1
                sn2.skill_name = skill_name_2
                sn3.skill_name = skill_name_3
                sn5.skill_name = skill_name_5
                sn6.skill_name = skill_name_6
                # For Debugging Purposes
                # print(sn1.skill_name)
                # print(sn2.skill_name)
                # print(sn3.skill_name)
                # print(sn5.skill_name)
                # print(sn6.skill_name)
            elif skill_name_4 != d_skill_4_entry and skill_name_5 != d_skill_5_entry and skill_name_6 != d_skill_6_entry:
                sn1.skill_name = skill_name_1
                sn2.skill_name = skill_name_2
                sn3.skill_name = skill_name_3
                sn4.skill_name = skill_name_4
                sn5.skill_name = skill_name_5
                sn6.skill_name = skill_name_6
                # For Debugging Purposes
                # print(sn1.skill_name)
                # print(sn2.skill_name)
                # print(sn3.skill_name)
                # print(sn4.skill_name)
                # print(sn5.skill_name)
                # print(sn6.skill_name)
            
            # For Debugging Purposes
            # Applicant Details
            print(ad.name)
            print(ad.birthdate)
            print(ad.sss_id)
            print(ad.address)
            print(ad.city)
            print(ad.province)
            print(ad.zipcode)
            print(ad.phoneNumber)
            print(ad.emailaddress)
            print(ad.employment_type)
            print(ad.job_pos)
            print(ad.desired_salary)
            print(ad.desired_start_date)
            print(ad.application_date)

            # School Details
            print(sd1.school_name)
            print(sd1.school_address)
            print(sd1.date_graduated)
            print(sd1.educ_attainment)
            print(sd2.school_name)
            print(sd2.school_address)
            print(sd2.date_graduated)
            print(sd2.educ_attainment)
            print(sd3.school_name)
            print(sd3.school_address)
            print(sd3.date_graduated)
            print(sd3.educ_attainment)

            # Work Experience
            print(wd1.prev_company)
            print(wd1.work_position)
            print(wd1.work_date_started)
            print(wd1.work_date_ended)
            print(wd1.reason_for_leaving)  
            print(wd2.prev_company)
            print(wd2.work_position)
            print(wd2.work_date_started)
            print(wd2.work_date_ended)
            print(wd2.reason_for_leaving)
            print(wd3.prev_company)
            print(wd3.work_position)
            print(wd3.work_date_started)
            print(wd3.work_date_ended)
            print(wd3.reason_for_leaving)

            # Major Skills
            print(sn1.skill_name)
            print(sn2.skill_name)
            print(sn3.skill_name)
            print(sn4.skill_name)
            print(sn5.skill_name)
            print(sn6.skill_name)
            
            
            connection_database()
    
            from __7_apply_end_form import end_application_main
            end_application_main(parent)
        else:
            pass

def display_values():

    if sn1.skill_name == d_skill_1_entry:
        pass
    elif sn1.skill_name != "":
        skill_1_var.set(sn1.skill_name)
    
    if sn2.skill_name == d_skill_2_entry:
        pass
    elif sn2.skill_name != "":
        skill_2_var.set(sn2.skill_name)
    
    if sn3.skill_name == d_skill_3_entry:
        pass
    elif sn3.skill_name != "":
        skill_3_var.set(sn3.skill_name)
    
    if sn4.skill_name == d_skill_4_entry:
        pass
    elif sn4.skill_name != "":
        skill_4_var.set(sn4.skill_name)

    if sn5.skill_name == d_skill_5_entry:
        pass
    elif sn4.skill_name != "":
        skill_5_var.set(sn5.skill_name)

    if sn6.skill_name == d_skill_6_entry:
        pass
    elif sn6.skill_name != "":
        skill_6_var.set(sn6.skill_name)

def major_skill_main(parent):   
    # Global Variables
    global skill_1_var
    global skill_2_var
    global skill_3_var
    global skill_4_var
    global skill_5_var
    global skill_6_var

    global d_skill_1_entry
    global d_skill_2_entry
    global d_skill_3_entry
    global d_skill_4_entry
    global d_skill_5_entry
    global d_skill_6_entry

    d_skill_1_entry = "Select Skill Name 1"
    d_skill_2_entry = "Select Skill Name 2"
    d_skill_3_entry = "Select Skill Name 3"
    d_skill_4_entry = "Select Skill Name 4"
    d_skill_5_entry = "Select Skill Name 5"
    d_skill_6_entry = "Select Skill Name 6"

    # --------------------------------------------------------------------------------#
    # ---------------------------------- GUI SETUP ---------------------------------- #
    # --------------------------------------------------------------------------------#
    fontstyle = ("Montserrat", 12)

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
        880.0,
        147.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        710.0,
        147.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        551.0,
        147.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        389.0,
        147.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        176.0,
        147.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        165.0,
        230.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        572.0,
        231.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        572.0,
        314.0,
        image=image_image_9
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets("image_10.png"))
    image_10 = canvas.create_image(
        572.0,
        399.0,
        image=image_image_10
    )

    image_image_11 = PhotoImage(
        file=relative_to_assets("image_11.png"))
    image_11 = canvas.create_image(
        167.0,
        314.0,
        image=image_image_11
    )

    image_image_12 = PhotoImage(
        file=relative_to_assets("image_12.png"))
    image_12 = canvas.create_image(
        167.0,
        399.0,
        image=image_image_12
    )

    image_image_13 = PhotoImage(
        file=relative_to_assets("image_13.png"))
    image_13 = canvas.create_image(
        512.0,
        191.0,
        image=image_image_13
    )

    image_image_14 = PhotoImage(
        file=relative_to_assets("image_14.png"))
    image_14 = canvas.create_image(
        459.0,
        230.0,
        image=image_image_14
    )

    image_image_15 = PhotoImage(
        file=relative_to_assets("image_15.png"))
    image_15 = canvas.create_image(
        459.0,
        314.0,
        image=image_image_15
    )

    image_image_16 = PhotoImage(
        file=relative_to_assets("image_16.png"))
    image_16 = canvas.create_image(
        459.0,
        400.0,
        image=image_image_16
    )

    image_image_17 = PhotoImage(
        file=relative_to_assets("image_17.png"))
    image_17 = canvas.create_image(
        511.0,
        78.0,
        image=image_image_17
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        307.5,
        261.5,
        image=entry_image_1
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        307.5,
        344.5,
        image=entry_image_2
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        307.5,
        428.5,
        image=entry_image_3
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        717.5,
        261.5,
        image=entry_image_4
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        717.0,
        344.5,
        image=entry_image_5
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        717.0,
        428.5,
        image=entry_image_6
    )

    # --------------------------------------------------------------------------------#
    # --------------------------------- ENTRY SETUP ----------------------------------#
    # --------------------------------------------------------------------------------#
    # skill_1_entry = DefaultTextEntry(
    #     default_text=d_skill_1_entry,
    #     bd=0,
    #     font=fontstyle,
    #     bg="#FFFFFF",
    #     fg="#000716",
    #     highlightthickness=0
    # )

    skills_data = fetch_skill_data()
    skills_options = [skill[0] for skill in skills_data]

    # Variable Declaration for skills input
    skill_1_var = tk.StringVar()
    skill_1_var.set(d_skill_1_entry)

    skill_2_var = tk.StringVar()
    skill_2_var.set(d_skill_2_entry)

    skill_3_var = tk.StringVar()
    skill_3_var.set(d_skill_3_entry)

    skill_4_var = tk.StringVar()
    skill_4_var.set(d_skill_4_entry)

    skill_5_var = tk.StringVar()
    skill_5_var.set(d_skill_5_entry)

    skill_6_var = tk.StringVar()
    skill_6_var.set(d_skill_6_entry)

    skill_1_entry = ttk.Combobox(
        parent,
        textvariable=skill_1_var,
        values=skills_options,
        font= fontstyle,
        state="readonly",
    )
    skill_1_entry.place(
        x=134.0,
        y=241.0,
        width=348.0,
        height=43.0
    )

    skill_2_entry = ttk.Combobox(
        parent,
        textvariable=skill_2_var,
        values=skills_options,
        font= fontstyle,
        state="readonly",
    )
    skill_2_entry.place(
        x=134.0,
        y=324.0,
        width=348.0,
        height=43.0
    )

    skill_3_entry = ttk.Combobox(
        parent,
        textvariable=skill_3_var,
        values=skills_options,
        font= fontstyle,
        state="readonly",
    )
    skill_3_entry.place(
        x=134.0,
        y=408.0,
        width=348.0,
        height=43.0
    )

    skill_4_entry = ttk.Combobox(
        parent,
        textvariable=skill_4_var,
        values=skills_options,
        font= fontstyle,
        state="readonly",
    )
    skill_4_entry.place(
        x=538.5,
        y=241.0,
        width=358.0,
        height=43.0
    )

    skill_5_entry = ttk.Combobox(
        parent,
        textvariable=skill_5_var,
        values=skills_options,
        font= fontstyle,
        state="readonly",
    )
    skill_5_entry.place(
        x=538.0,
        y=324.0,
        width=358.0,
        height=43.0
    )

    
    skill_6_entry = ttk.Combobox(
        parent,
        textvariable=skill_6_var,
        values=skills_options,
        font= fontstyle,
        state="readonly",
    )
    skill_6_entry.place(
        x=538.0,
        y=408.0,
        width=358.0,
        height=43.0
    )

    # --------------------------------------------------------------------------------#
    # ----------------------------------- BUTTONS ----------------------------------- #
    # --------------------------------------------------------------------------------#

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    submit_button = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#ccd4d9",
        cursor='hand2',
        command=lambda: submit_clicked(parent),
        relief="flat"
    )
    submit_button.place(
        x=694.0,
        y=509.0,
        width=178.0,
        height=33.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    back_button = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#ccd4d9",
        cursor='hand2',
        command=lambda: back_cliked(parent),
        relief="flat"
    )
    back_button.place(
        x=151.0,
        y=509.0,
        width=178.0,
        height=33.0
    )

    display_values()
    parent.mainloop()


if __name__ == "__main__":
    root = Tk()
    root.geometry("1024x568")
    major_skill_main(root)