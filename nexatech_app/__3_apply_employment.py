from pathlib import Path
import sys
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, messagebox, font
from default_entry import DefaultTextEntry
import tkinter as tk
from tkcalendar import DateEntry
import datetime
from storage import applicant_data as ad


# Get the script's directory path
SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

# Set the relative path to the assets directory
ASSETS_PATH = SCRIPT_DIR / "assets" / "apply_frame2"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def back_clicked(parent, canvas):
    ad.employment_type = employment_type_var.get()
    ad.job_pos = job_position_entry.get()
    ad.desired_salary = desired_salary_entry.get()
    ad.desired_start_date = desired_starting_entry.get_date()
    ad.application_date = application_date_entry.get_date()
    
    
    employment_type_combobox.place_forget()
    job_position_entry.place_forget()
    desired_salary_entry.place_forget()
    desired_starting_entry.place_forget()
    application_date_entry.place_forget()

    # canvas.delete("all")
    # for widget in canvas.winfo_children():
    #     widget.destroy()

    canvas.delete("all")
    for widget in canvas.winfo_children():
        widget.destroy()
    from __2_apply_personal_info import personal_main
    personal_main(parent)

def next_clicked(parent, canvas):
    emp_type = employment_type_var.get()
    job_pos = job_position_entry.get()
    des_sal = desired_salary_entry.get()
    des_start_date = desired_starting_entry.get_date()
    appli_date = application_date_entry.get_date()

    if not (emp_type or job_pos or des_sal or des_start_date or appli_date) or emp_type == "Select Employment Type" or job_pos == d_job_position_entry or des_sal == d_desired_sal_entry or des_start_date == "" or appli_date == "":
        messagebox.showerror("Error", "Please fill out all fields.")
    elif len(job_pos) < 3:
        messagebox.showerror("Error", "Please enter a valid job position.")
    elif not des_sal.isdigit() or len(des_sal) < 3:
        messagebox.showerror("Error", "Please enter a valid desired salary.")
    else:
        ad.employment_type = emp_type
        ad.job_pos = job_pos
        ad.desired_salary = des_sal
        ad.desired_start_date = des_start_date
        ad.application_date = appli_date

        canvas.delete("all")
        for widget in canvas.winfo_children():
            widget.destroy()
        from __4_apply_education import education_main
        education_main(parent)

def display_values():
    # Employment Type
    if ad.employment_type != "":
        employment_type_var.set(ad.employment_type)
    # Job Position
    if ad.job_pos == d_job_position_entry:
        pass
    elif ad.job_pos != "":
        job_position_entry.delete(0, tk.END)
        job_position_entry.insert(0, ad.job_pos)
        job_position_entry.config(fg="black")

    # Desired Salary
    if ad.desired_salary == d_desired_sal_entry:
        pass
    elif ad.desired_salary != "":
        desired_salary_entry.delete(0, tk.END)
        desired_salary_entry.insert(0, ad.desired_salary)
        desired_salary_entry.config(fg="black")
    
    # Desired Starting Date
    if ad.desired_start_date != "":
        desired_starting_entry.set_date(ad.desired_start_date)
    
    # Application Date
    if ad.application_date != "":
        application_date_entry.set_date(ad.application_date)

def emp_main(parent):
    global d_job_position_entry
    global d_desired_sal_entry
    global employment_type_var
    global employment_type_combobox
    global desired_salary_entry
    global job_position_entry
    global desired_starting_entry
    global application_date_entry
    

    d_job_position_entry = "Enter Job Position"
    d_desired_sal_entry = "Enter Desired Salary"

    # --------------------------------------------------------------------------------#
    # ---------------------------------- GUI SETUP ---------------------------------- #
    # --------------------------------------------------------------------------------#
    fontstyle = "Montserrat"
    
    canvas = Canvas(
        parent,
        bg = "#ccd4d9",
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
        552.0,
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
        207.0,
        218.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        195.0,
        304.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        557.0,
        218.0,
        image=image_image_9
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets("image_10.png"))
    image_10 = canvas.create_image(
        585.0,
        304.0,
        image=image_image_10
    )

    image_image_11 = PhotoImage(
        file=relative_to_assets("image_11.png"))
    image_11 = canvas.create_image(
        202.0,
        383.0,
        image=image_image_11
    )

    image_image_12 = PhotoImage(
        file=relative_to_assets("image_12.png"))
    image_12 = canvas.create_image(
        511.0,
        78.0,
        image=image_image_12
    )


    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        696.0,
        248.0,
        image=entry_image_1
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        696.0,
        334.0,
        image=entry_image_2
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        327.0,
        413.0,
        image=entry_image_3
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        327.0,
        248.0,
        image=entry_image_4
    )
    

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        327.0,
        334.0,
        image=entry_image_5
    )


    # --------------------------------------------------------------------------------#
    # --------------------------------- ENTRY SETUP --------------------------------- #
    # --------------------------------------------------------------------------------#
    # https://stackoverflow.com/questions/28938758/combobox-fontsize-in-tkinter
    # bigfont = ttk.FOnt(family="Helvetica",size=36)
    # window.option_add("*TCombobox*Listbox*Font", bigfont)

    # Create a Combobox for employment type selection
    employment_type_options = ["Full-time", "Part-time"]
    
    employment_type_var = tk.StringVar()
    employment_type_combobox = ttk.Combobox(
        parent,
        values=employment_type_options,
        textvariable=employment_type_var,
        font=fontstyle,
        state="readonly",
    )
    employment_type_combobox.set("Select Employment Type")
    employment_type_combobox.place(x=159.0, y=229.0, width=336.0, height=38.0)


    # Customize the font size of the Combobox options
    
    # employment_type_entry = Entry(
    #     bd=0,
    #     bg="#FFFFFF",
    #     fg="#000716",
    #     highlightthickness=0
    # )
    # employment_type_entry.place(
    #     x=159.0,
    #     y=228.0,
    #     width=336.0,
    #     height=38.0
    # )

    
    job_position_entry = DefaultTextEntry(
        parent,
        default_text=d_job_position_entry,
        bd=0,
        font=fontstyle,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    job_position_entry.place(
        x=528.0,
        y=228.0,
        width=336.0,
        height=38.0
    )

    
    
    desired_salary_entry = DefaultTextEntry(
        parent,
        default_text=d_desired_sal_entry,
        bd=0,
        font=fontstyle,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    desired_salary_entry.place(
        x=159.0,
        y=314.0,
        width=336.0,
        height=38.0
    )

    
    desired_starting_entry = DateEntry(
        parent,
        font=fontstyle,
        background="#FFFFFF",
        foreground="#000716",
        borderwidth=2,  # Set the borderwidth to 0 to remove the border
        selectbackground="#359ca6",  # Customize the background color when the date is selected
        selectforeground="white",  # Customize the foreground color when the date is selected
        normalbackground="#FFFFFF",  # Customize the background color when the widget is not focused
        normalforeground="#000716",  # Customize the foreground color when the widget is not focused
        highlightthickness=0,
        arrowcolor="#FFFFFF",
        date_pattern="yyyy-mm-dd",  # Customize the date pattern to your preference
        firstweekday = "sunday"
    )
    desired_starting_entry.place(
        x=528.0,
        y=315.0,
        width=336.0,
        height=38.0
    )

    
    
    application_date_entry = DateEntry(
        parent,
        font=fontstyle,
        fieldbackground='light green',
        background="#FFFFFF",
        foreground="#000716",
        borderwidth=2,  # Set the borderwidth to 0 to remove the border
        selectbackground="#359ca6",  # Customize the background color when the date is selected
        selectforeground="white",  # Customize the foreground color when the date is selected
        normalbackground="#FFFFFF",  # Customize the background color when the widget is not focused
        normalforeground="#000716",  # Customize the foreground color when the widget is not focused
        highlightthickness=0,
        arrowcolor="#FFFFFF",
        date_pattern="yyyy-mm-dd",  # Customize the date pattern to your preference
        firstweekday = "sunday"
    )
    application_date_entry.place(
        x=159.0,
        y=394.0,
        width=336.0,
        height=38.0
    )


    # --------------------------------------------------------------------------------#
    # ----------------------------------- BUTTONS ----------------------------------- #
    # --------------------------------------------------------------------------------#
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        parent,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back_clicked(parent, canvas),
        relief="flat"
    )
    button_1.place(
        x=151.0,
        y=509.0,
        width=178.0,
        height=33.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        parent,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: next_clicked(parent, canvas),
        relief="flat"
    )
    button_2.place(
        x=694.0,
        y=509.0,
        width=178.0,
        height=33.0
    )

    
    display_values()
    parent.mainloop()