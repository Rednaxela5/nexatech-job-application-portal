from pathlib import Path
import sys
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, Label, Frame, ttk, messagebox
from default_entry import DefaultTextEntry
import tkinter as tk
from tkcalendar import DateEntry
import datetime
from storage import applicant_data as ad
import sql_connection as db_controller


# Get the script's directory path
SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

# Set the relative path to the assets directory
ASSETS_PATH = SCRIPT_DIR / "assets" / "dash_frame4"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# def update_date():
#     dateOfBirth.set_date(datetime.date.today())

def display_values():


    # Full Name
    if ad.name == d_fullname_entry:
        pass
    elif ad.name != "":
        fullname_entry.delete(0, tk.END)
        fullname_entry.insert(0, ad.name)
        fullname_entry.config(fg="black")

    # Date of Birth
    if ad.birthdate != "":
        dateOfBirth.set_date(ad.birthdate)
    # SSS ID
    if ad.sss_id == d_sssID_entry:
        pass
    elif ad.sss_id != "":
        sssID_entry.delete(0, tk.END)
        sssID_entry.insert(0, ad.sss_id)
        sssID_entry.config(fg="black")
    
    # Address
    if ad.address == d_address_entry:
        pass
    elif ad.address != "":
        address_entry.delete(0, tk.END)
        address_entry.insert(0, ad.address)
        address_entry.config(fg="black")

    # City
    if ad.city == d_city_entry:
        pass
    elif ad.city != "":
        city_entry.delete(0, tk.END)
        city_entry.insert(0, ad.city)
        city_entry.config(fg="black")

    # Province
    if ad.province == d_province_entry:
        pass
    elif ad.province != "":
        province_entry.delete(0, tk.END)
        province_entry.insert(0, ad.province)
        province_entry.config(fg="black")
    
    # ZIP Code
    if ad.zipcode == d_zipcode_entry:
        pass
    elif ad.zipcode != "":
        zip_code_entry.delete(0, tk.END)
        zip_code_entry.insert(0, ad.zipcode)
        zip_code_entry.config(fg="black")
    
    # Phone Number
    if ad.phoneNumber == d_phone_number_entry:
        pass
    elif ad.phoneNumber != "":
        phone_number_entry.delete(0, tk.END)
        phone_number_entry.insert(0, ad.phoneNumber)
        phone_number_entry.config(fg="black")
    
    # Email Address
    if ad.emailaddress == d_email_address_entry:
        pass
    elif ad.emailaddress != "":
        email_address_entry.delete(0, tk.END)
        email_address_entry.insert(0, ad.emailaddress)
        email_address_entry.config(fg="black")

def back_clicked(parent):
    from _2_admin_applicants import applicant
    applicant(parent)

def update_clicked(parent):
    name = fullname_entry.get()
    birthdate = dateOfBirth.get_date()
    sss_id = sssID_entry.get()
    address = address_entry.get()
    city = city_entry.get()
    province = province_entry.get()
    zipcode = zip_code_entry.get()
    phoneNumber = phone_number_entry.get()
    emailaddress = email_address_entry.get()
    
    if not (name or birthdate or sss_id or address or city or province or zipcode or phoneNumber or emailaddress) or name == d_fullname_entry or birthdate == "" or sss_id == d_sssID_entry or address == d_address_entry or city == d_city_entry or province == d_province_entry or zipcode == d_zipcode_entry or phoneNumber == d_phone_number_entry or emailaddress == d_email_address_entry:
        messagebox.showerror("Error", "Please fill out all fields.")
    elif len(name) < 3:
        messagebox.showerror("Error", "Enter valid name.")
    elif not sss_id.isdigit() or len(sss_id) != 10:
        messagebox.showerror("Error", "SSS ID should be a 10-digit number.")
    elif address == d_address_entry or not address.strip() or len(address) < 5:
        messagebox.showerror("Error", "Please provide a valid address.")
    elif city == d_city_entry or not city.strip():
        messagebox.showerror("Error", "Please provide a valid city.")
    elif province == d_province_entry or not province.strip():
        messagebox.showerror("Error", "Please provide a valid province.")
    elif not zipcode.isdigit() or len(zipcode) != 4:
        messagebox.showerror("Error", "Zip code should be a 4-digit number.")
    elif not phoneNumber.isdigit() or len(phoneNumber) > 11:
        messagebox.showerror("Error", "Phone number should be a valid number with up to 11 digits.")
    elif "@" not in emailaddress:
        messagebox.showerror("Error", "Please provide a valid email address.")
        
    else:

        ad.name = fullname_entry.get()
        ad.birthdate = dateOfBirth.get_date()
        ad.sss_id = sssID_entry.get()
        ad.address = address_entry.get()
        ad.city = city_entry.get()
        ad.province = province_entry.get()
        ad.zipcode = zip_code_entry.get()
        ad.phoneNumber = phone_number_entry.get()
        ad.emailaddress = email_address_entry.get()

        confirmation_message = "Do you want to update the details?"
        confirm = messagebox.askyesno("Confirmation", confirmation_message)
        if confirm:
            if db_controller.update_applicant_details():  # Assuming update_applicant_details returns True on success
                messagebox.showinfo("Success", "Applicant details updated successfully.")
                from _2_admin_applicants import applicant
                applicant(parent)
            else:
                messagebox.showerror("Error", "Failed to update applicant details.")  # Assuming update_applicant_details returns False on failure
        else:
            pass

        # For Debugging Purposes
        # print(applicant_data.name)
        # print(applicant_data.birthdate)
        # print(applicant_data.sss_id)
        # print(applicant_data.address)
        # print(applicant_data.city)
        # print(applicant_data.province)
        # print(applicant_data.zipcode)
        # print(applicant_data.phoneNumber)
        # print(applicant_data.emailaddress)
        
        # fullname_entry.place_forget()
        # dateOfBirth.place_forget()
        # sssID_entry.place_forget()
        # address_entry.place_forget()
        # city_entry.place_forget()
        # province_entry.place_forget()
        # zip_code_entry.place_forget()
        # phone_number_entry.place_forget()
        # email_address_entry.place_forget()
        # canvas.place_forget()



def edit_applicant(parent):
    # Global Variables
    global dateOfBirth
    global fullname_entry
    global sssID_entry
    global address_entry
    global city_entry
    global province_entry
    global zip_code_entry
    global phone_number_entry
    global email_address_entry 

    global d_fullname_entry
    global d_sssID_entry
    global d_address_entry
    global d_city_entry
    global d_province_entry
    global d_zipcode_entry
    global d_phone_number_entry
    global d_email_address_entry
    
    # Default Text for Each Entry Box
    d_fullname_entry = "Enter Full Name"
    d_sssID_entry = "Enter SSS ID"
    d_address_entry = "Enter Address"
    d_city_entry = "Enter City"
    d_province_entry = "Enter Province"
    d_zipcode_entry = "Enter ZIP Code"
    d_phone_number_entry = "Enter Phone Number"
    d_email_address_entry = "Enter Email Address"

    # --------------------------------------------------------------------------------#
    # ---------------------------------- GUI SETUP ---------------------------------- #
    # --------------------------------------------------------------------------------#

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

    global image_image_1
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        120.0,
        42.0,
        image=image_image_1
    )

    global image_image_2
    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        136.0,
        64.0,
        image=image_image_2
    )

    global entry_image_1
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        593.0,
        371.0,
        image=entry_image_1
    )
    

    global entry_image_2
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        227.0,
        371.0,
        image=entry_image_2
    )
    

    global entry_image_3
    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        652.5,
        291.0,
        image=entry_image_3
    )
    

    global entry_image_4
    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        408.5,
        291.0,
        image=entry_image_4
    )
    

    global entry_image_5
    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        164.5,
        291.0,
        image=entry_image_5
    )
    

    global entry_image_6
    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        408.5,
        216.0,
        image=entry_image_6
    )
    

    global entry_image_7
    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        652.5,
        144.0,
        image=entry_image_7
    )
    

    global entry_image_8
    entry_image_8 = PhotoImage(
        file=relative_to_assets("entry_8.png"))
    entry_bg_8 = canvas.create_image(
        408.5,
        144.0,
        image=entry_image_8
    )
    

    global entry_image_9
    entry_image_9 = PhotoImage(
        file=relative_to_assets("entry_9.png"))
    entry_bg_9 = canvas.create_image(
        164.5,
        144.0,
        image=entry_image_9
    )
    

    global image_image_3
    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        79.0,
        111.0,
        image=image_image_3
    )

    global image_image_4
    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        60.0,
        259.0,
        image=image_image_4
    )

    global image_image_5
    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        97.0,
        341.0,
        image=image_image_5
    )

    global image_image_6
    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        556.0,
        111.0,
        image=image_image_6
    )

    global image_image_7
    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        565.0,
        259.0,
        image=image_image_7
    )

    global image_image_8
    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        332.0,
        111.0,
        image=image_image_8
    )

    global image_image_9
    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        321.0,
        259.0,
        image=image_image_9
    )

    global image_image_10
    image_image_10 = PhotoImage(
        file=relative_to_assets("image_10.png"))
    image_10 = canvas.create_image(
        461.0,
        341.0,
        image=image_image_10
    )

    global image_image_11
    image_image_11 = PhotoImage(
        file=relative_to_assets("image_11.png"))
    image_11 = canvas.create_image(
        73.0,
        185.0,
        image=image_image_11
    )

    
    # --------------------------------------------------------------------------------#
    # --------------------------------- ENTRY SETUP --------------------------------- #
    # --------------------------------------------------------------------------------#

    fullname_entry = DefaultTextEntry(
        default_text=d_fullname_entry,
        font=fontstyle,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    fullname_entry.place(
        x=266.0,
        y=191.0,
        width=217.0,
        height=38.0
    )

    dateOfBirth = DateEntry(
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
    dateOfBirth.place(
        x=508.0,
        y=192.0,
        width=220.0,
        height=38.0
    )

    sssID_entry = DefaultTextEntry(
        default_text=d_sssID_entry,
        font=fontstyle,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    sssID_entry.place(
        x=755.0,
        y=191.0,
        width=217.0,
        height=38.0
    )

    address_entry = DefaultTextEntry(
        default_text=d_address_entry,
        font=fontstyle,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    address_entry.place(
        x=266.0,
        y=263.0,
        width=705.0,
        height=38.0
    )

    city_entry = DefaultTextEntry(
        default_text=d_city_entry,
        font=fontstyle,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    city_entry.place(
        x=266.0,
        y=338.0,
        width=217.0,
        height=38.0
    )

    province_entry = DefaultTextEntry(
        default_text=d_province_entry,
        font=fontstyle,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    province_entry.place(
        x=510.0,
        y=338.0,
        width=217.0,
        height=38.0
    )   

    zip_code_entry = DefaultTextEntry(
        default_text=d_zipcode_entry,
        font=fontstyle,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    zip_code_entry.place(
        x=755.0,
        y=338.0,
        width=217.0,
        height=38.0
    )
    
    phone_number_entry = DefaultTextEntry(
        default_text=d_phone_number_entry,
        font=fontstyle,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    phone_number_entry.place(
        x=265.0,
        y=418.0,
        width=342.0,
        height=38.0
    )

    email_address_value = StringVar()

    email_address_entry = DefaultTextEntry(
        default_text=d_email_address_entry,
        textvariable=email_address_value,
        font=fontstyle,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    email_address_entry.place(
        x=635.0,
        y=418.0,
        width=336.0,
        height=38.0
    )

    

    # --------------------------------------------------------------------------------#
    # ----------------------------------- BUTTONS ----------------------------------- #
    # --------------------------------------------------------------------------------#
    # Update Button
    global button_image_1
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    
    global button_1
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: update_clicked(parent),
        activebackground="#ccd4d9",
        cursor='hand2',
        relief="flat"
    )
    button_1.place(
        x=840.0,
        y=500.0,
        width=139.0,
        height=41.0
    )

    # Back Button
    global button_image_2
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    
    global button_2
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: back_clicked(parent),
        activebackground="#ccd4d9",
        cursor='hand2',
        relief="flat"
    )
    button_2.place(
        x=255.0,
        y=500.0,
        width=115.0,
        height=41.0
    )

    display_values()



    
    

