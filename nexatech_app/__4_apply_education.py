import sys
import tkinter as tk
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Button, PhotoImage, ttk, messagebox
from tkcalendar import DateEntry
from default_entry import DefaultTextEntry
from storage import school_data_1 as sd1, school_data_2 as sd2, school_data_3 as sd3
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
import mysql.connector

# Get the script's directory path
SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

# Set the relative path to the assets directory
ASSETS_PATH = SCRIPT_DIR / "assets" / "apply_frame3"

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

def fetch_school_data():
    conn = connect_to_mysql()
    cursor = conn.cursor()  # Replace this with your actual connection code
    cursor.execute("SELECT school_name, school_address FROM school_db ORDER BY school_name ASC")
    school_data = cursor.fetchall()
    cursor.close()
    return school_data

def fetch_school_count():
    conn = connect_to_mysql()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM school_db")
    count = cursor.fetchone()[0]
    cursor.close()
    return count

def add_more_clicked():
    confirmation_message = "Are you sure you want to add more entries?"

    if sd1.cur_educ_list >= 3:
        # If the limit of 3 inputs is reached, show an error message box
        messagebox.showerror("Input Limit Exceeded", "You have reached the maximum limit of inputs (3).")
    
    else:
        # Show the confirmation messagebox
        confirm = messagebox.askquestion("Confirmation", confirmation_message)
        if confirm == 'yes':
            
            if education_attainment_var.get() == "Junior High School":
                education_attainment_var.set("JHS")
            elif education_attainment_var.get() == "Senior High School":
                education_attainment_var.set("SHS")
            elif education_attainment_var.get() == "College":
                education_attainment_var.set("CO")

            if custom_input_checkbox.get() == 1:
                school_name = custom_school_entry.get()
            else:
                school_name = school_name_var.get()
            school_address = school_address_entry.get()
            date_graduated = date_graduated_entry.get_date()
            education_attainment = education_attainment_var.get()

            if (school_name == d_school_name_entry and school_name == d_custom_school_entry)  or school_address == d_school_address_entry or date_graduated == "" or education_attainment == "Select Education Attainment":
                messagebox.showerror("Error", "Please fill out all fields.")
            else:
                if sd1.cur_educ_list == 1:
                    sd1.cur_educ_list += 1
                    sd1.school_name = school_name
                    sd1.school_address = school_address
                    sd1.date_graduated = date_graduated
                    sd1.educ_attainment = education_attainment

                    school_name_var.set("Select your school")
                    custom_school_entry.delete(0, "end")
                    school_address_entry.delete(0, "end")
                    date_graduated_entry.delete(0, "end")
                    education_attainment_var.set("Select Education Attainment")

                    
                    # For Debugging Purposes
                    print("School Data 1")
                    print(sd1.school_name)
                    print(sd1.school_address)
                    print(sd1.date_graduated)
                    print(sd1.educ_attainment)

                    
                elif sd1.cur_educ_list == 2:
                    sd1.cur_educ_list += 1
                    sd2.school_name = school_name
                    sd2.school_address = school_address
                    sd2.date_graduated = date_graduated
                    sd2.educ_attainment = education_attainment

                    school_name_var.set("Select your school")
                    custom_school_entry.delete(0, "end")
                    school_address_entry.delete(0, "end")
                    date_graduated_entry.delete(0, "end")
                    education_attainment_var.set("Select Education Attainment")
                    
                    # For Debugging Purposes
                    print("School Data 2")
                    print(sd2.school_name)
                    print(sd2.school_address)
                    print(sd2.date_graduated)
                    print(sd2.educ_attainment)
                # elif sd1.cur_educ_list == 3:
                #     sd3.school_name = school_name
                #     sd3.school_address = school_address
                #     sd3.date_graduated = date_graduated
                #     sd3.educ_attainment = education_attainment

                    # school_name_entry.delete(0, "end")
                    # school_address_entry.delete(0, "end")
                    # date_graduated_entry.delete(0, "end")
                    # education_attainment_var.set("Select Education Attainment")

                    # For Debugging Purposes
                    # print(sd3.school_name)
                    # print(sd3.school_address)
                    # print(sd3.date_graduated)
                    # print(sd3.educ_attainment)
            custom_input_checkbox.set(0)  # Uncheck the checkbox
            custom_school_entry.place_forget()  # Hide the custom entry
            school_name_entry.place(x=158.0, y=242.0, width=338.0, height=38.0)  # Place the combobox

        else:
            # Do nothing, the user clicked 'no'
            pass


def back_clicked(parent):
    if custom_input_checkbox.get() == 1:
        school_name = custom_school_entry.get()
    else:
        school_name = school_name_var.get()
    school_address = school_address_entry.get()
    date_graduated = date_graduated_entry.get_date()
    education_attainment = education_attainment_var.get()
    if sd1.cur_educ_list == 1:
        sd1.school_name = school_name
        sd1.school_address = school_address
        sd1.date_graduated = date_graduated
        sd1.educ_attainment = education_attainment

        # For Debugging Purposes
        print("School Data 1")
        print(sd1.school_name)
        print(sd1.school_address)
        print(sd1.date_graduated)
        print(sd1.educ_attainment)
    elif sd1.cur_educ_list == 2:
        sd2.school_name = school_name
        sd2.school_address = school_address
        sd2.date_graduated = date_graduated
        sd2.educ_attainment = education_attainment

        # For Debugging Purposes
        print("School Data 2")
        print(sd2.school_name)
        print(sd2.school_address)
        print(sd2.date_graduated)
        print(sd2.educ_attainment)
    elif sd1.cur_educ_list == 3:
        sd3.school_name = school_name
        sd3.school_address = school_address
        sd3.date_graduated = date_graduated
        sd3.educ_attainment = education_attainment

        # For Debugging Purposes
        print("School Data 3")
        print(sd3.school_name)
        print(sd3.school_address)
        print(sd3.date_graduated)
        print(sd3.educ_attainment)

   
    from __3_apply_employment import emp_main
    emp_main(parent)

def next_clicked(parent):
    if education_attainment_var.get() == "Junior High School":
        education_attainment_var.set("JHS")
    elif education_attainment_var.get() == "Senior High School":
        education_attainment_var.set("SHS")
    elif education_attainment_var.get() == "College":
        education_attainment_var.set("CO")

    if custom_input_checkbox.get() == 1:
        school_name = custom_school_entry.get()
    else:
        school_name = school_name_var.get()
    school_address = school_address_entry.get()
    date_graduated = date_graduated_entry.get_date()
    education_attainment = education_attainment_var.get()

    if school_name == d_school_name_entry or school_address == d_school_address_entry or date_graduated == "" or education_attainment == "Select Education Attainment":
        messagebox.showerror("Error", "Please fill out all fields.")
    else:
        
        if sd1.cur_educ_list == 1:
            sd1.school_name = school_name
            sd1.school_address = school_address
            sd1.date_graduated = date_graduated
            sd1.educ_attainment = education_attainment

            # For Debugging Purposes
            print("School Data 1")
            print(sd1.school_name)
            print(sd1.school_address)
            print(sd1.date_graduated)
            print(sd1.educ_attainment)

        elif sd1.cur_educ_list == 2:
            sd2.school_name = school_name
            sd2.school_address = school_address
            sd2.date_graduated = date_graduated
            sd2.educ_attainment = education_attainment
            
            # For Debugging Purposes
            print("School Data 2")
            print(sd2.school_name)
            print(sd2.school_address)
            print(sd2.date_graduated)
            print(sd2.educ_attainment)
            
        elif sd1.cur_educ_list == 3:
            sd3.school_name = school_name
            sd3.school_address = school_address
            sd3.date_graduated = date_graduated
            sd3.educ_attainment = education_attainment

            # For Debugging Purposes
            print("School Data 3")
            print(sd3.school_name)
            print(sd3.school_address)
            print(sd3.date_graduated)
            print(sd3.educ_attainment)
        
        # connection_database()

        from __5_apply_work_exp import work_experience_main
        work_experience_main(parent)



def display_values():
    # School Data 1
    if sd1.educ_attainment == "JHS":
        sd1.educ_attainment = "Junior High School"
    elif sd1.educ_attainment == "SHS":
        sd1.educ_attainment = "Senior High School"
    elif sd1.educ_attainment == "CO":
        sd1.educ_attainment = "College"
    
    # Schoool Data 2
    if sd2.educ_attainment == "JHS":
        sd2.educ_attainment = "Junior High School"
    elif sd2.educ_attainment == "SHS":
        sd2.educ_attainment = "Senior High School"
    elif sd2.educ_attainment == "CO":
        sd2.educ_attainment = "College"

    # School Data 3
    if sd3.educ_attainment == "JHS":
        sd3.educ_attainment = "Junior High School"
    elif sd3.educ_attainment == "SHS":
        sd3.educ_attainment = "Senior High School"
    elif sd3.educ_attainment == "CO":
        sd3.educ_attainment = "College"

    if sd1.cur_educ_list == 1:  # Check if there are any entries in the list
        # For Debugging Purposes
        print("School Data 1")
        print(sd1.school_name)
        print(sd1.school_address)
        print(sd1.date_graduated)
        print(sd1.educ_attainment)


        # School Name
        if sd1.school_name == d_school_name_entry or sd1.school_name == d_custom_school_entry:
            pass
        elif sd1.school_name != "":
            school_name_var.set(sd1.school_name)

        # School Address
        if sd1.school_address == d_school_address_entry:
            pass
        elif sd1.school_address != "":
            school_address_entry.delete(0, tk.END)
            school_address_entry.insert(0, sd1.school_address)
            school_address_entry.config(fg="black")

        # Date Graduated
        if sd1.date_graduated != "":
            date_graduated_entry.set_date(sd1.date_graduated)

        # Educational Attainment
        if sd1.educ_attainment != "":
            education_attainment_var.set(sd1.educ_attainment)

    if sd1.cur_educ_list == 2:

        # For Debugging Purposes
        print("School Data 2")
        print(sd2.school_name)
        print(sd2.school_address)
        print(sd2.date_graduated)
        print(sd2.educ_attainment)
        # School Name
        if sd2.school_name == d_school_name_entry or sd2.school_name == d_custom_school_entry:
            pass
        elif sd2.school_name != "":
            school_name_var.set(sd2.school_name)
            custom_school_entry.insert(0, sd2.school_name)

        # School Address
        if sd2.school_address == d_school_address_entry:
            pass
        elif sd2.school_address != "":
            school_address_entry.delete(0, tk.END)
            school_address_entry.insert(0, sd2.school_address)
            school_address_entry.config(fg="black")

        # Date Graduated
        if sd2.date_graduated != "":
            date_graduated_entry.set_date(sd2.date_graduated)

        # Educational Attainment
        if sd2.educ_attainment != "":
            education_attainment_var.set(sd2.educ_attainment)

    if sd1.cur_educ_list == 3:

        # For Debugging Purposes
        print("School Data 3")
        print(sd3.school_name)
        print(sd3.school_address)
        print(sd3.date_graduated)
        print(sd3.educ_attainment)
        # School Name
        if sd3.school_name == d_school_name_entry or sd3.school_name == d_custom_school_entry:
            pass
        elif sd3.school_name != "":
            school_name_var.set(sd3.school_name)

        # School Address
        if sd3.school_address == d_school_address_entry:
            pass
        elif sd3.school_address != "":
            school_address_entry.delete(0, tk.END)
            school_address_entry.insert(0, sd3.school_address)
            school_address_entry.config(fg="black")

        # Date Graduated
        if sd3.date_graduated != "":
            date_graduated_entry.set_date(sd3.date_graduated)

        # Educational Attainment
        if sd3.educ_attainment != "":
            education_attainment_var.set(sd3.educ_attainment)

# # Function to update the school address entry
# def update_school_address(event):
#     selected_school = school_name_var.get()
#     school_address_entry.delete(0, tk.END)
#     school_address_entry.insert(0, school_addresses.get(selected_school, "Enter address"))


def update_school_address(event):
    def on_entry_click(event):
        if school_address_entry.get() == "Enter address":
            school_address_entry.delete(0, tk.END)
            school_address_entry.config(fg='black')

    def on_focus_out(event):
        if not school_address_entry.get():
            school_address_entry.insert(0, "Enter address")
            school_address_entry.config(fg='gray')
        elif school_address_entry.get() != "Enter address" or school_address_entry.get() == "":
            school_address_entry.config(fg='black')
    selected_school = school_name_var.get()
    school_address_entry.delete(0, tk.END)
    school_address_entry.insert(0, school_addresses.get(selected_school, "Enter address"))

    school_address_entry.bind("<FocusIn>", on_entry_click)
    school_address_entry.bind("<FocusOut>", on_focus_out)

def toggle_custom_input():
    if custom_input_checkbox.get():
        school_address_entry.delete(0, tk.END)
        school_name_entry.place_forget()  # Hide the combobox
        custom_school_entry.place(x=158.0, y=242.0, width=336.0, height=38.0)  # Place the custom entry
    else:
        custom_school_entry.place_forget()  # Hide the custom entry
        school_name_entry.place(x=158.0, y=242.0, width=338.0, height=38.0)  # Place the combobox
  

def education_main(parent):
    # Global Variables
    global school_name_entry
    global custom_school_entry
    global school_address_entry
    global date_graduated_entry
    global education_attainment_var
    global custom_input_checkbox
    global school_name_var
    global school_addresses
    
    global d_school_address_entry
    global d_school_name_entry
    global d_custom_school_entry
    # --------------------------------------------------------------------------------#
    # ---------------------------------- GUI SETUP ---------------------------------- #
    # --------------------------------------------------------------------------------#
    d_school_name_entry = "Select your school"
    d_custom_school_entry = "Enter School Name"
    d_school_address_entry = "Enter School Address"
   
    fontstyle = "Montserrat"

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
        553.0,
        147.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        386.0,
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
        200.0,
        231.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        200.0,
        317.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        567.0,
        231.0,
        image=image_image_9
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets("image_10.png"))
    image_10 = canvas.create_image(
        587.0,
        317.0,
        image=image_image_10
    )

    image_image_11 = PhotoImage(
        file=relative_to_assets("image_11.png"))
    image_11 = canvas.create_image(
        511.0,
        78.0,
        image=image_image_11
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        696.0,
        261.0,
        image=entry_image_1
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        696.0,
        347.0,
        image=entry_image_2
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        327.0,
        261.0,
        image=entry_image_3
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        327.0,
        347.0,
        image=entry_image_4
    )

    

    # --------------------------------------------------------------------------------#
    # --------------------------------- ENTRY SETUP --------------------------------- #
    # --------------------------------------------------------------------------------#

    # Name of School
    # Source: https://counselorcorporation.com/list-of-universities-in-philippines/
    school_data = fetch_school_data()
    school_count = fetch_school_count()
    print("School Count", school_count)
    # Update school_name_options and school_addresses
    school_name_options = [school[0] for school in school_data]


    school_name_var = tk.StringVar()
    school_name_var.set("Select your school")

    school_name_entry = ttk.Combobox(
        parent,
        textvariable=school_name_var,
        values=school_name_options,
        font= ("Montserrat", 12),
        state="readonly",
    )

    school_name_entry.place(
        x=158.0,
        y=242.0,
        width=338.0,
        height=38.0
    )

    custom_input_checkbox = tk.BooleanVar()
    not_listed_checkbox = tk.Checkbutton(
        parent,
        text="School not listed?",
        font=("Montserrat", 10),
        bg="#ccd4d9",
        fg="#354855",
        variable=custom_input_checkbox,
        command=toggle_custom_input
    )
    not_listed_checkbox.place(x=150.0, y=282.0)

    custom_school_entry = DefaultTextEntry(
        default_text=d_custom_school_entry,
        bd=0,
        font=fontstyle,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )

    custom_school_entry.place(
        x=158.0,
        y=242.0,
        width=336.0,
        height=38.0
    )
    custom_school_entry.place_forget()

    # School Address

    # Fetch data from the database
    school_addresses = {}
    for school in school_data:
        school_addresses[school[0]] = school[1]
        print(f"School Name: {school[0]}, School Address: {school[1]}")

    school_address_entry = tk.Entry(
        bd=0,
        font=("Montserrat", 12),
        bg="#FFFFFF",
        highlightthickness=0
    )
    school_address_entry.place(
        x=528.0,
        y=241.0,
        width=336.0,
        height=38.0
    )
    # Bind the ComboboxSelected event to the update_school_address function
    school_name_entry.bind("<<ComboboxSelected>>", update_school_address)

    
    # Education Attainment
    education_attainment_options = ["Junior High School", "Senior High School", "College"]
    education_attainment_var = tk.StringVar()
    education_attainment_var.set("Select Education Attainment")

    education_attainment_entry = ttk.Combobox(
        parent,
        textvariable=education_attainment_var,
        values=education_attainment_options,
        font=fontstyle,
        state="readonly",
    )

    education_attainment_entry.place(
        x=528.0,
        y=328.0,
        width=336.0,
        height=38.0
    )

    
    
    # Date Graduated
    date_graduated_entry = DateEntry(
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
    date_graduated_entry.place(
        x=159.0,
        y=328.0,
        width=336.0,
        height=38.0
    )

    
    # --------------------------------------------------------------------------------#
    # ----------------------------------- BUTTONS ----------------------------------- #
    # --------------------------------------------------------------------------------#
    
    # Add More Button
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=add_more_clicked,
        relief="flat"
    )
    button_1.place(
        x=404.0,
        y=449.0,
        width=216.0,
        height=33.0
    )

    # Back Button
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back_clicked(parent),
        relief="flat"
    )
    button_2.place(
        x=151.0,
        y=509.0,
        width=178.0,
        height=33.0
    )

    # Next Button
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: next_clicked(parent),
        relief="flat"
    )
    button_3.place(
        x=694.0,
        y=509.0,
        width=178.0,
        height=33.0
    )
    display_values()
    
    parent.mainloop()


if __name__ == "__main__":
    root = Tk()
    root.geometry("1024x568")
    education_main(root)