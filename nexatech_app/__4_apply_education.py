import sys
import tkinter as tk
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Button, PhotoImage, ttk, messagebox
from tkcalendar import DateEntry
from default_entry import DefaultTextEntry
from storage import school_data_1 as sd1, school_data_2 as sd2, school_data_3 as sd3
from sql_connection import connection_database

# Get the script's directory path
SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

# Set the relative path to the assets directory
ASSETS_PATH = SCRIPT_DIR / "assets" / "apply_frame3"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
                            # "Ateneo de Manila University",
                           
                            # "Far Eastern Univers
                            # ity",
                            # "Polytechnic University of the Philippines",
                            # "Polytechnic University of the Philippines-San Juan",
                            # "Polytechnic University of the Philippines-Parañaque",
                            # "Polytechnic University of the Philippines-Taguig",
                            # "Philippines Science High School",
                            # "University of the East",
                            # "Japan-Philippines Institue of Technology Plaridel Campus Inc.",
                            # "Technological Institute of the Philippines",
                            # "University of the Philippines-Diliman",
                            # "University of the Philippines-Manila",
                            # "University of the Philippines-Los Banos",
    # Name of School
    # Source: https://counselorcorporation.com/list-of-universities-in-philippines/
    school_name_options = [ 
                            "Abe International Business College",
                            "Abra State Institute of Science and Technology",
                            "ACLC College of Butuan",
                            "ACTS Computer College Sta Cruz",
                            "Adamson University",
                            "Adventist International Institute of Advanced Studies",
                            "Adventist University of the Philippines",
                            "Agusan Del Sur College",
                            "Aklan State University",
                            "Aldersgate College",
                            "Alliance Graduate School",
                            "AMA Computer College Tuguegarao",
                            "AMA Computer University",
                            "Angeles University Foundation",
                            "Araullo University",
                            "Arellano University",
                            "Asia Pacific College",
                            "Asian College of Technology",
                            "Asian Institute of Journalism and Communication",
                            "Asian Institute of Management",
                            "Asian Institute of Maritime Studies",
                            "Asian Social Institute Manila",
                            "Asian Theological Seminary Philippines",
                            "Ateneo de Davao University",
                            "Ateneo de Manila University",
                            "Ateneo de Naga University",
                            "Ateneo de Zamboanga University",
                            "Aurora State College of Technology",
                            "Bagui Central University",
                            "Baguio College of Technology",
                            "Basilan State College",
                            "Bataan Peninsula State University",
                            "Batanes State College",
                            "Batangas State University",
                            "Benedicto College",
                            "Benguet State University",
                            "Bestlink College of the Philippines",
                            "Bicol Christian College of Medicine AMEC BCCM",
                            "Bicol State College of Applied Sciences and Technology",
                            "Bicol University",
                            "Biliran Province State University",
                            "Binangonan Catholic College",
                            "BIT International College",
                            "Bohol Island State University (Central Visayas State College of Agriculture)",
                            "Brokenshire College",
                            "Bukidnon State University",
                            "Bulacan Agricultural State College",
                            "Bulacan State University",
                            "Cagayan State University",
                            "Calayan Educational Foundation",
                            "Calayan Educational Foundation",
                            "Camarines Norte State College",
                            "Camarines Sur Polytechnic Colleges",
                            "CAP College Foundation",
                            "Capitol University",
                            "Capiz State University",
                            "Caraga State University",
                            "Carlos Hilado Memorial State College",
                            "Catanduanes State University",
                            "Cavite State University",
                            "Cebu Aeronautical Technical School (Computer Arts and Technological College Legazpi City)",
                            "Cebu Doctors’ University",
                            "Cebu Institute of Medicine",
                            "Cebu Institute of Technology",
                            "Cebu Normal University",
                            "Cebu Technological University",
                            "Center for Industrial Technology and Enterprise",
                            "Central Bicol State University of Agriculture",
                            "Central Colleges of the Philippines",
                            "Central Luzon State University",
                            "Central Mindanao University",
                            "Central Philippine Adventist College",
                            "Central Philippine University",
                            "Centro Escolar University Manila Mendiola",
                            "Chiang Kai Shek College",
                            "City College of Angeles",
                            "Colegio de Dagupan",
                            "Colegio de San Juan de Letran",
                            "Colegio de San Pedro",
                            "Colegio de Sta Catalina de Alejandria",
                            "Colegio San Agustin Bacolod",
                            "College of Development Communication",
                            "College of Technological Sciences Cebu",
                            "College of the Holy Spirit",
                            "Columban College",
                            "Computer Arts and Technology CAT College Polangui",
                            "Comteq Computer and Business College",
                            "Cotabato Foundation College of Science and Technology",
                            "Davao del Norte State College",
                            "Davao del Sur State College",
                            "Davao Doctors College",
                            "Davao Medical School Foundation",
                            "De La Salle Araneta University",
                            "De La Salle College of Saint Benilde",
                            "De La Salle Health Sciences Institute",
                            "De La Salle Lipa",
                            "De La Salle University Dasmariñas",
                            "De La Salle University Manila",
                            "Dipolog Medical Center College Foundation",
                            "Divine Word College of Legazpi",
                            "DMMA College of Southern Philippines",
                            "Don Bosco College",
                            "Don Honorio Ventura State University DHVSU",
                            "Don Honorio Ventura Technological State University",
                            "Don Mariano Marcos Memorial State University",
                            "Dr Aurelio Mendoza Memorial College",
                            "Eastern Samar State University",
                            "Eastern Visayas State University",
                            "Emilio Aguinaldo College",
                            "Eulogio Amang Rodríguez Institute of Science and Technology",
                            "F L Vargas College",
                            "Far Eastern University Cavite",
                            "Far Eastern University East Asia College",
                            "Far Eastern University Institute of Medicine",
                            "Far Eastern University Philippines",
                            "Father Saturnino Urios University",
                            "Fatima University",
                            "Feati University",
                            "Fernandez College of Arts and Technology",
                            "Filamer Christian University",
                            "First Asia Institute of Technology and Humanities",
                            "Foundation University",
                            "Gingoog City Colleges",
                            "Guagua National Colleges Pampanga",
                            "Guimaras State College",
                            "Holy Angel University",
                            "Holy Child Colleges of Butuan",
                            "Holy Cross of Davao College",
                            "Holy Name University",
                            "Holy Trinity University Philippines",
                            "ICCT Colleges",
                            "Ifugao State University",
                            "Iligan Computer Institute",
                            "Iligan Medical Center College",
                            "Ilocos Sur Community College",
                            "Ilocos Sur Polytechnic State College",
                            "Iloilo Doctors’ College",
                            "Iloilo Science and Technology University (Western Visayas College of Science & Technology)",
                            "Informatics Computer Institute",
                            "Information and Communications Technology Academy",
                            "Inspire Sports Academy",
                            "International Graduate School of Leadership (International School of Theology Asia)",
                            "Isabela State University",
                            "Je Mondejar Computer College",
                            "John B Lacson Foundation Maritime University",
                            "Jose Maria College",
                            "Jose Rizal Memorial State University",
                            "Jose Rizal University",
                            "Kalayaan College",
                            "La Consolacion College Bacolod",
                            "La Consolacion University Philippines",
                            "La Patria College",
                            "La Salle University Ozamiz",
                            "Laguna State Polytechnic University",
                            "Leyte Normal University",
                            "Liceo de Cagayan University",
                            "Lipa City Colleges",
                            "Lorma Colleges MacArthur",
                            "Lyceum Northwestern University",
                            "Lyceum of the Philippines University Batangas",
                            "Lyceum of the Philippines University",
                            "Malayan Colleges Laguna",
                            "Manila Business College",
                            "Manila Central University",
                            "Manuel L Quezon University",
                            "Manuel S Enverga University",
                            "Mapua Institute of Technology",
                            "Marian College",
                            "Mariano Marcos State University",
                            "Maritime Academy of Asia and the Pacific Kamaya Point",
                            "Mater Dei College Bohol",
                            "Metro Dumaguete College",
                            "MHAM College of Medicine",
                            "Microcity College of Business and Technology",
                            "Mindanao State University at Naawan",
                            "Mindanao State University General Santos",
                            "Mindanao State University Iligan Institute of Technology",
                            "Mindanao State University Marawi City",
                            "Mindanao State University Tawi-Tawi College of Technology and Oceanography",
                            "Mindanao State University",
                            "Mindoro State University",
                            "Miriam College",
                            "Misamis University",
                            "Mountain Province State Polytechnic College",
                            "Mountain View College Philippines",
                            "MSC Institute of Technology",
                            "Naga College Foundation",
                            "National College of Business and Arts NCBA",
                            "National College of Science and Technology",
                            "National Defense College of the Philippines",
                            "National Teachers College Philippines",
                            "National University Philippines",
                            "Negros College",
                            "Negros Oriental State University (Central Visayas Polytechnic College)",
                            "New Era University",
                            "Northeastern college",
                            "Northern Luzon Adventist College",
                            "Northern Negros State College of Science & Technology",
                            "Northwest Samar State University",
                            "Northwestern University Laoag City",
                            "Norzagaray College",
                            "Notre Dame of Dadiangas University",
                            "Notre Dame of Kidapawan College",
                            "Notre Dame of Marbel University",
                            "Notre Dame University Cotabato",
                            "Nueva Ecija University of Science and Technology",
                            "Nueva Vizcaya State University",
                            "NYK-TDG Maritime Academy",
                            "Occidental Mindoro State College",
                            "Our Lady of the Pillar College Cauayan",
                            "Palawan State University",
                            "Palompon Institute of Technology",
                            "Pampanga State Agricultural University",
                            "Pangasinan State University",
                            "PanPacific University North Philippines",
                            "Panpacific University North Philippines",
                            "Partido State University",
                            "Pasig Catholic College",
                            "PATTS College of Aeronautics",
                            "Philippine Christian University",
                            "Philippine College of Criminology",
                            "Philippine College of Ministry",
                            "Philippine Merchant Marine Academy",
                            "Philippine Military Academy",
                            "Philippine National Police Academy",
                            "Philippine Normal University",
                            "Philippine School of Business Administration",
                            "Philippine Women’s University",
                            "PLT College",
                            "Polytechnic University of the Philippines",
                            "President Ramon Magsaysay State University",
                            "Quirino State University",
                            "Republic Central Colleges",
                            "Riverside College",
                            "Rizal Technological University",
                            "Rogationist College",
                            "Romblon State University",
                            "Sacred Heart College Lucena City",
                            "Saint Ferdinand College",
                            "Saint Francis of Assisi College Cavite",
                            "Saint Joseph College Maasin",
                            "Saint Joseph Institute of Technology",
                            "Saint Jude College",
                            "Saint Louis College",
                            "Saint Louis University Baguio City",
                            "Saint Luke’s College of Medicine",
                            "Saint Mary’s University of Bayombong",
                            "Saint Michael’s College of Laguna",
                            "Saint Paul University Dumaguete",
                            "Saint Paul University Manila",
                            "Saint Paul University Pasig",
                            "Saint Paul University Philippines",
                            "Salazar Colleges of Science and Institute of Technology",
                            "Samar State University",
                            "Samson College of Science and Technology",
                            "San Antonio de Padua College",
                            "San Beda University",
                            "San Carlos College",
                            "San Isidro College",
                            "San Pablo Colleges San Pablo City Laguna",
                            "San Pedro College of Business Administration",
                            "San Sebastian College Manila",
                            "San Sebastian College Recoletos de Cavite",
                            "Siena College of Taytay",
                            "Silliman University",
                            "Siquijor State College",
                            "Sorsogon State College",
                            "Southeast Asia Interdisciplinary Development Institute",
                            "Southern City Colleges",
                            "Southern Leyte State University",
                            "Southern Luzon State University (Polytechnic College)",
                            "Southern Philippines Agri Business and Marine and Aquatic School of Technology",
                            "Southville SISFU",
                            "Southway College of Technology",
                            "Southwestern University Cebu Philippines",
                            "Southwestern University PHINMA",
                            "St Augustine School of Nursing",
                            "St Cecilia’s College Cebu",
                            "St Joseph’s College Quezon City",
                            "St Louis College Valenzuela",
                            "St Marys College",
                            "St Nicolas College of Business and Technology",
                            "St Paul College of Ilocos Sur",
                            "St Paul University Iloilo",
                            "St Paul University Surigao",
                            "St Scholastica’s College",
                            "St Vincent’s College",
                            "St. Paul University Quezon City",
                            "Sultan Kudarat State University",
                            "Surigao del Sur State University",
                            "Surigao State College of Technology",
                            "System Technology Institute",
                            "Systems Plus Computer College Quezon City",
                            "Tanchuling College",
                            "Tarlac Agricultural University",
                            "Tarlac Agricultural University",
                            "Tarlac State University",
                            "Technological Institute of the Philippines",
                            "Technological Research for Advanced Computer Education College",
                            "Technological University of the Philippines",
                            "The Lewis College",
                            "Trinity University of Asia (Trinity College of Quezon City)",
                            "Universidad Aldersgate",
                            "Universidad de Santa Isabel",
                            "Universidad de Zamboanga",
                            "University of Antique (Polytechnic State College of Antique)",
                            "University of Asia and the Pacific",
                            "University of Baguio",
                            "University of Batangas",
                            "University of Bohol",
                            "University of Cagayan Valley",
                            "University of Caloocan City",
                            "University of Cebu",
                            "University of Cebu",
                            "University of Eastern Philippines",
                            "University of Iloilo",
                            "University of La Salette",
                            "University of Luzon",
                            "University of Makati",
                            "University of Manila",
                            "University of Mindanao",
                            "University of Negros Occidental Recoletos",
                            "University of Northeastern Philippines",
                            "University of Northern Philippines",
                            "University of Nueva Caceres",
                            "University of Pangasinan",
                            "University of Perpetual Help System Dalta",
                            "University of Perpetual Help System Laguna",
                            "University of Rizal System",
                            "University of Saint Anthony Iriga City",
                            "University of Saint La Salle Bacolod",
                            "University of Saint Louis Tuguegarao",
                            "University of San Agustin",
                            "University of San Carlos",
                            "University of San Jose Recoletos",
                            "University of Santo Tomas",
                            "University of Science and Technology of Southern Philippines USTP",
                            "University of Southeastern Philippines",
                            "University of Southern Mindanao",
                            "University of Sto Tomas Legazpi Bicol Dominican University",
                            "University of the Assumption",
                            "University of the City of Manila",
                            "University of the Cordilleras (Baguio Colleges Foundation)",
                            "University of the East Ramon Magsaysay",
                            "University of the East",
                            "University of the Immaculate Conception",
                            "University of the Philippines Baguio",
                            "University of the Philippines Cebu",
                            "University of the Philippines Diliman",
                            "University of the Philippines Manila",
                            "University of the Philippines Mindanao",
                            "University of the Philippines Visayas",
                            "University of the Philippines",
                            "University of the Visayas",
                            "Urdaneta City University",
                            "Virgen Milagrosa University Foundation",
                            "Visayas State University",
                            "Wesleyan University Philippines",
                            "West Visayas State University",
                            "Western Institute of Technology",
                            "Western Leyte College of Ormoc City",
                            "Western Mindanao State University",
                            "Western Philippines University",
                            "Xavier University Ateneo de Cagayan",
                            "Zamboanga Peninsula Polytechnic State University",
                            "Zamboanga State College of Marine Sciences and Technology"

]
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

    school_addresses = {
                            "Abe International Business College": "Quezon City, Metro Manila",
                            "Abra State Institute of Science and Technology": "Lagangilang, Abra",
                            "ACLC College of Butuan": "Butuan City, Agusan del Norte",
                            "ACTS Computer College Sta Cruz": "Sta. Cruz, Laguna",
                            "Adamson University": "Ermita, Manila",
                            "Adventist International Institute of Advanced Studies": "Silang, Cavite",
                            "Adventist University of the Philippines": "Silang, Cavite",
                            "Agusan Del Sur College": "San Francisco, Agusan del Sur",
                            "Aklan State University": "Banga, Aklan",
                            "Aldersgate College": "Solano, Nueva Vizcaya",
                            "Alliance Graduate School": "Quezon City, Metro Manila",
                            "AMA Computer College Tuguegarao": "Tuguegarao City",
                            "AMA Computer University": "Quezon City, Metro Manila",
                            "Angeles University Foundation": "Angeles City, Pampanga",
                            "Araullo University": "Cabanatuan City, Nueva Ecija",
                            "Arellano University": "Sampaloc, Manila",
                            "Asia Pacific College": "Makati City",
                            "Asian College of Technology": "Cebu City, Cebu",
                            "Asian Institute of Journalism and Communication": "Quezon City, Metro Manila",
                            "Asian Institute of Management": "Makati City",
                            "Asian Institute of Maritime Studies": "Pasay City, Metro Manila",
                            "Asian Social Institute Manila": "Manila City, Metro Manila",
                            "Asian Theological Seminary Philippines": "Quezon City, Metro Manila",
                            "Ateneo de Davao University": "Davao City",
                            "Ateneo de Manila University": "Katipunan Ave, Quezon City",
                            "Ateneo de Naga University": "Naga City, Camarines Sur",
                            "Ateneo de Zamboanga University": "Zamboanga City",
                            "Aurora State College of Technology": "Baler, Aurora",
                            "Baguio Central University": "Baguio City, Benguet",
                            "Baguio College of Technology": "Baguio City, Benguet",
                            "Basilan State College": "Isabela City, Basilan",
                            "Bataan Peninsula State University": "Balanga City, Bataan",
                            "Batanes State College": "Basco, Batanes",
                            "Batangas State University": "Batangas City, Batangas",
                            "Benedicto College": "Mandaue City, Cebu",
                            "Benguet State University": "La Trinidad, Benguet",
                            "Bestlink College of the Philippines": "Quezon City, Metro Manila",
                            "Bicol Christian College of Medicine AMEC BCCM": "Legazpi City, Albay",
                            "Bicol State College of Applied Sciences and Technology": "Naga City, Camarines Sur",
                            "Bicol University": "Legazpi City, Albay",
                            "Biliran Province State University": "Naval, Biliran",
                            "Binangonan Catholic College": "Binangonan, Rizal",
                            "BIT International College": "Tacloban City, Leyte",
                            "Bohol Island State University (Central Visayas State College of Agriculture)": "Tagbilaran City, Bohol",
                            "Brokenshire College": "Davao City, Davao del Sur",
                            "Bukidnon State University": "Malaybalay City, Bukidnon",
                            "Bulacan Agricultural State College": "San Ildefonso, Bulacan",
                            "Bulacan State University": "Malolos City, Bulacan",
                            "Cagayan State University": "Tuguegarao City, Cagayan",
                            "Calayan Educational Foundation": "Lucena City, Quezon",
                            "Calayan Educational Foundation": "Lucena City, Quezon",
                            "Camarines Norte State College": "Daet, Camarines Norte",
                            "Camarines Sur Polytechnic Colleges": "Naga City, Camarines Sur",
                            "CAP College Foundation": "Dasmariñas, Cavite",
                            "Capitol University": "Cagayan de Oro City, Misamis Oriental",
                            "Capiz State University": "Roxas City, Capiz",
                            "Caraga State University": "Butuan City",
                            "Carlos Hilado Memorial State College": "Talisay City, Negros Occidental",
                            "Catanduanes State University": "Virac, Catanduanes",
                            "Cavite State University": "Indang, Cavite",
                            "Cebu Aeronautical Technical School (Computer Arts and Technological College Legazpi City)": "Legazpi City, Albay",
                            "Cebu Doctors’ University": "Mandaue City, Cebu",
                            "Cebu Institute of Medicine": "Cebu City, Cebu",
                            "Cebu Institute of Technology": "Cebu City",
                            "Cebu Normal University": "Cebu City",
                            "Cebu Technological University": "Cebu City",
                            "Center for Industrial Technology and Enterprise": "San Isidro, Nueva Ecija",
                            "Central Bicol State University of Agriculture": "Pili, Camarines Sur",
                            "Central Colleges of the Philippines": "Quezon City, Metro Manila",
                            "Central Luzon State University": "Science City of Muñoz, Nueva Ecija",
                            "Central Mindanao University": "Musuan, Bukidnon",
                            "Central Philippine Adventist College": "Murcia, Negros Occidental",
                            "Central Philippine University": "Jaro, Iloilo City",
                            "Centro Escolar University Manila Mendiola": "San Miguel, Manila",
                            "Chiang Kai Shek College": "Manila City, Metro Manila",
                            "City College of Angeles": "Angeles City, Pampanga",
                            "Colegio de Dagupan": "Dagupan City, Pangasinan",
                            "Colegio de San Juan de Letran": "Manila City, Metro Manila",
                            "Colegio de San Pedro": "San Pedro City, Laguna",
                            "Colegio de Sta Catalina de Alejandria": "Pamplona, Camarines Sur",
                            "Colegio San Agustin Bacolod": "Bacolod City, Negros Occidental",
                            "College of Development Communication": "Los Baños, Laguna",
                            "College of Technological Sciences Cebu": "Cebu City, Cebu",
                            "College of the Holy Spirit": "Manila City, Metro Manila",
                            "Columban College": "Olongapo City, Zambales",
                            "Computer Arts and Technology CAT College Polangui": "Polangui, Albay",
                            "Comteq Computer and Business College": "Iligan City, Lanao del Norte",
                            "Cotabato Foundation College of Science and Technology": "Datu Odin Sinsuat, Maguindanao",
                            "Davao del Norte State College": "Panabo City, Davao del Norte",
                            "Davao del Sur State College": "Digos City, Davao del Sur",
                            "Davao Doctors College": "Davao City, Davao del Sur",
                            "Davao Medical School Foundation": "Davao City, Davao del Sur",
                            "De La Salle Araneta University:": "Malabon City",
                            "De La Salle College of Saint Benilde": "Malate, Manila",
                            "De La Salle Health Sciences Institute": "Dasmariñas City, Cavite",
                            "De La Salle Lipa": "Lipa City, Batangas",
                            "De La Salle University Dasmariñas": "Dasmariñas City, Cavite",
                            "De La Salle University Manila": "Malate, Manila",
                            "Dipolog Medical Center College Foundation": "Dipolog City, Zamboanga del Norte",
                            "Divine Word College of Legazpi": "Legazpi City, Albay",
                            "DMMA College of Southern Philippines": "Davao City, Davao del Sur",
                            "Don Bosco College": "Canlubang, Calamba City, Laguna",
                            "Don Honorio Ventura State University DHVSU": "Bacolor, Pampanga",
                            "Don Honorio Ventura Technological State University": "Bacolor, Pampanga",
                            "Don Mariano Marcos Memorial State University": "San Fernando City, La Union",
                            "Dr Aurelio Mendoza Memorial College": "Ozamiz City, Misamis Occidental",
                            "Eastern Samar State University": "Borongan City, Eastern Samar",
                            "Eastern Visayas State University": "Tacloban City, Leyte",
                            "Emilio Aguinaldo College": "Ermita, Manila",
                            "Eulogio Amang Rodríguez Institute of Science and Technology": "Manila City, Metro Manila",
                            "F L Vargas College": "Pamplona, Cagayan",
                            "Far Eastern University Cavite": "Silang, Cavite",
                            "Far Eastern University East Asia College": "Sampaloc, Manila",
                            "Far Eastern University Institute of Medicine": "Sampaloc, Manila",
                            "Far Eastern University Philippines": "Sampaloc, Manila",
                            "Father Saturnino Urios University": "Butuan City, Agusan del Norte",
                            "Fatima University": "Valenzuela City",
                            "Feati University": "Manila City, Metro Manila",
                            "Fernandez College of Arts and Technology": "Baliuag, Bulacan",
                            "Filamer Christian University": "Roxas City, Capiz",
                            "First Asia Institute of Technology and Humanities": "Batangas",
                            "Foundation University": "Dumaguete City, Negros Oriental",
                            "Gingoog City Colleges": "Gingoog City, Misamis Oriental",
                            "Guagua National Colleges Pampanga": "Guagua, Pampanga",
                            "Guimaras State College": "Jordan, Guimaras",
                            "Holy Angel University": "Angeles City, Pampanga",
                            "Holy Child Colleges of Butuan": "Butuan City, Agusan del Norte",
                            "Holy Cross of Davao College": "Davao City, Davao del Sur",
                            "Holy Name University": "Tagbilaran City, Bohol",
                            "Holy Trinity University Philippines": "Puerto Princesa City, Palawan",
                            "ICCT Colleges": "San Mateo, Rizal",
                            "Ifugao State University": "Nayon, Lamut, Ifugao",
                            "Iligan Computer Institute": "Iligan City, Lanao del Norte",
                            "Iligan Medical Center College": "Iligan City, Lanao del Norte",
                            "Ilocos Sur Community College": "Candon City, Ilocos Sur",
                            "Ilocos Sur Polytechnic State College": "Ilocos Sur",
                            "Iloilo Doctors’ College": "Iloilo City, Iloilo",
                            "Iloilo Science and Technology University (Western Visayas College of Science & Technology)": "Iloilo City, Iloilo",
                            "Informatics Computer Institute": "Quezon City, Metro Manila",
                            "Information and Communications Technology Academy": "Bacolod City, Negros Occidental",
                            "Inspire Sports Academy": "Calamba City, Laguna",
                            "International Graduate School of Leadership (International School of Theology Asia)": "Quezon City, Metro Manila",
                            "Isabela State University": "Cauayan City, Isabela",
                            "Je Mondejar Computer College": "Tagbilaran City, Bohol",
                            "John B Lacson Foundation Maritime University": "Iloilo City, Iloilo",
                            "Jose Maria College": "Davao City, Davao del Sur",
                            "Jose Rizal Memorial State University": "Dapitan City, Zamboanga del Norte",
                            "Jose Rizal University": "Mandaluyong City",
                            "Kalayaan College": "Quezon City, Metro Manila",
                            "La Consolacion College Bacolod": "Bacolod City, Negros Occidental",
                            "La Consolacion University Philippines": "Malolos City, Bulacan",
                            "La Patria College": "Batac City, Ilocos Norte",
                            "La Salle University Ozamiz": "Ozamiz City, Misamis Occidental",
                            "Laguna State Polytechnic University": "Santa Cruz, Laguna",
                            "Leyte Normal University": "Tacloban City, Leyte",
                            "Liceo de Cagayan University": "Cagayan de Oro City",
                            "Lipa City Colleges": "Lipa City, Batangas",
                            "Lorma Colleges MacArthur": "Carlatan, San Fernando City, La Union",
                            "Lyceum Northwestern University": "Dagupan City, Pangasinan",
                            "Lyceum of the Philippines University Batangas": "Batangas City, Batangas",
                            "Lyceum of the Philippines University": "Intramuros, Manila",
                            "Malayan Colleges Laguna": "Cabuyao, Laguna",
                            "Manila Business College": "Quezon City, Metro Manila",
                            "Manila Central University": "Caloocan City",
                            "Manuel L Quezon University": "Quiapo, Manila City, Metro Manila",
                            "Manuel S Enverga University": "Lucena City, Quezon",
                            "Mapua Institute of Technology": "Intramuros, Manila",
                            "Marian College": "Tagum City, Davao del Norte",
                            "Mariano Marcos State University": "Batac City, Ilocos Norte",
                            "Maritime Academy of Asia and the Pacific Kamaya Point": "Mariveles, Bataan",
                            "Mater Dei College Bohol": "Tubigon, Bohol",
                            "Metro Dumaguete College": "Dumaguete City, Negros Oriental",
                            "MHAM College of Medicine": "Cebu City, Cebu",
                            "Microcity College of Business and Technology": "San Fernando City, La Union",
                            "Mindanao State University at Naawan": "Naawan, Misamis Oriental",
                            "Mindanao State University General Santos": "General Santos City",
                            "Mindanao State University Iligan Institute of Technology": "Iligan City, Lanao del Norte",
                            "Mindanao State University Marawi City": "Marawi City, Lanao del Sur",
                            "Mindanao State University Tawi-Tawi College of Technology and Oceanography": "Bongao, Tawi-Tawi",
                            "Mindanao State University": "Marawi City, Lanao del Sur",
                            "Mindoro State University": "Calapan City, Oriental Mindoro",
                            "Miriam College": "Quezon City",
                            "Misamis University": "Ozamiz City, Misamis Occidental",
                            "Mountain Province State Polytechnic College": "Bontoc, Mountain Province",
                            "Mountain View College Philippines": "Bukidnon",
                            "MSC Institute of Technology": "Cainta, Rizal",
                            "Naga College Foundation": "Naga City, Camarines Sur",
                            "National College of Business and Arts NCBA": "Quezon City, Metro Manila",
                            "National College of Science and Technology": "Dasmariñas, Cavite",
                            "National Defense College of the Philippines": "Quezon City",
                            "National Teachers College Philippines": "Manila City, Metro Manila",
                            "National University Philippines": "Sampaloc, Manila",
                            "Negros College": "Kabankalan City, Negros Occidental",
                            "Negros Oriental State University (Central Visayas Polytechnic College)": "Dumaguete City, Negros Oriental",
                            "New Era University": "Quezon City, Metro Manila",
                            "Northeastern college": "Santiago City, Isabela",
                            "Northern Luzon Adventist College": "Artacho, Sison, Pangasinan",
                            "Northern Negros State College of Science & Technology": "Sagay City, Negros Occidental",
                            "Northwest Samar State University": "Calbayog City, Samar",
                            "Northwestern University Laoag City": "Laoag City, Ilocos Norte",
                            "Norzagaray College": "Norzagaray, Bulacan",
                            "Notre Dame of Dadiangas University": "General Santos City, South Cotabato",
                            "Notre Dame of Kidapawan College": "Kidapawan City, Cotabato",
                            "Notre Dame of Marbel University": "Koronadal City, South Cotabato",
                            "Notre Dame University Cotabato": "Cotabato City, Maguindanao",
                            "Nueva Ecija University of Science and Technology": "Cabanatuan City, Nueva Ecija",
                            "Nueva Vizcaya State University": "Bayombong, Nueva Vizcaya",
                            "NYK-TDG Maritime Academy": "Canlubang, Calamba City, Laguna",
                            "Occidental Mindoro State College": "San Jose, Occidental Mindoro",
                            "Our Lady of the Pillar College Cauayan": "Cauayan City, Isabela",
                            "Palawan State University": "Puerto Princesa",
                            "Palompon Institute of Technology": "Palompon, Leyte",
                            "Pampanga State Agricultural University": "Magalang, Pampanga",
                            "Pangasinan State University": "Lingayen, Pangasinan",
                            "PanPacific University North Philippines": "Urdaneta City, Pangasinan",
                            "Partido State University": "Camarines Sur",
                            "Pasig Catholic College": "Pasig City, Metro Manila",
                            "PATTS College of Aeronautics": "Pasay City, Metro Manila",
                            "Philippine Christian University": "Manila City",
                            "Philippine College of Criminology": "Manila City, Metro Manila",
                            "Philippine College of Ministry": "Quezon City, Metro Manila",
                            "Philippine Merchant Marine Academy": "San Narciso, Zambales",
                            "Philippine Military Academy": "Baguio City, Benguet",
                            "Philippine National Police Academy": "Silang, Cavite",
                            "Philippine Normal University": "Manila City",
                            "Philippine School of Business Administration": "Quezon City, Metro Manila",
                            "Philippine Women’s University": "Malate, Manila",
                            "PLT College": "Butuan City, Agusan del Norte",
                            "Polytechnic University of the Philippines": "Sta. Mesa, Manila",
                            "President Ramon Magsaysay State University": "Iba, Zambales",
                            "Quirino State University": "Diffun, Quirino",
                            "Republic Central Colleges": "Quezon City, Metro Manila",
                            "Riverside College": "Bacolod City, Negros Occidental",
                            "Rizal Technological University": "Mandaluyong City",
                            "Rogationist College": "Tagaytay City, Cavite",
                            "Romblon State University": "Odiongan, Romblon",
                            "Sacred Heart College Lucena City": "Lucena City, Quezon",
                            "Saint Ferdinand College": "Urdaneta City, Pangasinan",
                            "Saint Francis of Assisi College Cavite": "Dasmariñas, Cavite",
                            "Saint Joseph College Maasin": "Maasin City, Southern Leyte",
                            "Saint Joseph Institute of Technology": "Butuan City, Agusan del Norte",
                            "Saint Jude College": "Manila City, Metro Manila",
                            "Saint Louis College": "San Fernando City, La Union",
                            "Saint Louis University Baguio City": "Baguio City",
                            "Saint Luke’s College of Medicine": "Quezon City, Metro Manila",
                            "Saint Mary’s University of Bayombong": "Bayombong, Nueva Vizcaya",
                            "Saint Michael’s College of Laguna": "Laguna",
                            "Saint Paul University Dumaguete": "Dumaguete City, Negros Oriental",
                            "Saint Paul University Manila": "Manila City, Metro Manila",
                            "Saint Paul University Pasig": "Pasig City, Metro Manila",
                            "Saint Paul University Philippines": "Tuguegarao City, Cagayan",
                            "Salazar Colleges of Science and Institute of Technology": "Zamboanga City, Zamboanga del Sur",
                            "Samar State University": "Catbalogan City, Samar",
                            "Samson College of Science and Technology": "Calamba City, Laguna",
                            "San Antonio de Padua College": "Roxas City, Capiz",
                            "San Beda University": "Mendiola, Manila",
                            "San Carlos College": "San Carlos City, Pangasinan",
                            "San Isidro College": "Malaybalay City, Bukidnon",
                            "San Pablo Colleges San Pablo City Laguna": "San Pablo City, Laguna",
                            "San Pedro College of Business Administration": "San Pedro City, Laguna",
                            "San Sebastian College Manila": "Manila City, Metro Manila",
                            "San Sebastian College Recoletos de Cavite": "Cavite City, Cavite",
                            "Siena College of Taytay": "Taytay, Rizal",
                            "Silliman University": "Dumaguete City, Negros Oriental",
                            "Siquijor State College": "Siquijor, Siquijor",
                            "Sorsogon State College": "Sorsogon City, Sorsogon",
                            "Southeast Asia Interdisciplinary Development Institute": "Quezon City, Metro Manila",
                            "Southern City Colleges": "Zamboanga City, Zamboanga del Sur",
                            "Southern Leyte State University": "Sogod, Southern Leyte",
                            "Southern Luzon State University (Polytechnic College)": "Lucban, Quezon",
                            "Southern Philippines Agri Business and Marine and Aquatic School of Technology": "Malita, Davao Occidental",
                            "Southville SISFU": "Las Piñas City, Metro Manila",
                            "Southway College of Technology": "San Fernando City, La Union",
                            "Southwestern University Cebu Philippines": "Cebu City, Cebu",
                            "Southwestern University PHINMA": "Cebu City, Cebu",
                            "St Augustine School of Nursing": "Quezon City, Metro Manila",
                            "St Cecilia’s College Cebu": "Cebu City, Cebu",
                            "St Joseph’s College Quezon City": "Quezon City, Metro Manila",
                            "St Louis College Valenzuela": "Valenzuela City, Metro Manila",
                            "St Marys College": "Tagum City, Davao del Norte",
                            "St Nicolas College of Business and Technology": "San Nicolas, Ilocos Norte",
                            "St Paul College of Ilocos Sur": "Bantay, Ilocos Sur",
                            "St Paul University Iloilo": "Iloilo City, Iloilo",
                            "St Paul University Surigao": "Surigao City, Surigao del Norte",
                            "St Scholastica’s College": "Malate, Manila",
                            "St Vincent’s College": "Dipolog City, Zamboanga del Norte",
                            "St. Paul University Quezon City": "Quezon City, Metro Manila",
                            "Sultan Kudarat State University": "Tacurong City, Sultan Kudarat",
                            "Surigao del Sur State University": "Tandag City, Surigao del Sur",
                            "Surigao State College of Technology": "Surigao City",
                            "System Technology Institute": "Cubao, Quezon City",
                            "Systems Plus Computer College Quezon City": "Quezon City, Metro Manila",
                            "Tanchuling College": "Tagum City, Davao del Norte",
                            "Tarlac Agricultural University": "Camarines Norte",
                            "Tarlac Agricultural University": "Camarines Norte",
                            "Tarlac State University":"Tarlac City, Tarlac",
                            "Technological Institute of the Philippines": "Cubao, Quezon City",
                            "Technological Research for Advanced Computer Education College": "San Juan, Metro Manila",
                            "Technological University of the Philippines": "Ermita, Manila",
                            "The Lewis College": "Sorsogon City, Sorsogon",
                            "Trinity University of Asia (Trinity College of Quezon City)": "Quezon City, Metro Manila",
                            "Universidad Aldersgate": "Solano, Nueva Vizcaya",
                            "Universidad de Santa Isabel": "Naga City, Camarines Sur",
                            "Universidad de Zamboanga": "Zamboanga City",
                            "University of Antique (Polytechnic State College of Antique)": "Sibalom, Antique",
                            "University of Asia and the Pacific": "Pasig City",
                            "University of Baguio": "Baguio City",
                            "University of Batangas": "Batangas City, Batangas",
                            "University of Bohol": "Tagbilaran City, Bohol",
                            "University of Cagayan Valley": "Tuguegarao City, Cagayan",
                            "University of Caloocan City": "Caloocan City, Metro Manila",
                            "University of Cebu": "Cebu City, Cebu",
                            "University of Cebu": "Cebu City, Cebu",
                            "University of Eastern Philippines:": "Catarman, Northern Samar",
                            "University of Iloilo": "Iloilo City, Iloilo",
                            "University of La Salette": "Santiago City, Isabela",
                            "University of Luzon": "Dagupan City, Pangasinan",
                            "University of Makati": "Makati City, Metro Manila",
                            "University of Manila": "Manila City, Metro Manila",
                            "University of Mindanao": "Davao City",
                            "University of Negros Occidental Recoletos": "Bacolod City",
                            "University of Northeastern Philippines": "Iriga City, Camarines Sur",
                            "University of Northern Philippines": "Vigan City, Ilocos Sur",
                            "University of Nueva Caceres": "Naga City, Camarines Sur",
                            "University of Pangasinan": "Dagupan City, Pangasinan",
                            "University of Perpetual Help System Dalta": "Las Piñas City",
                            "University of Perpetual Help System Laguna": "Biñan City, Laguna",
                            "University of Rizal System": "Morong, Rizal",
                            "University of Saint Anthony Iriga City": "Iriga City, Camarines Sur",
                            "University of Saint La Salle Bacolod": "Bacolod City, Negros Occidental",
                            "University of Saint Louis Tuguegarao": "Tuguegarao City, Cagayan",
                            "University of San Agustin": "Iloilo City",
                            "University of San Carlos": "Cebu City",
                            "University of San Jose Recoletos": "Cebu City",
                            "University of Santo Tomas": "Sampaloc, Manila",
                            "University of Science and Technology of Southern Philippines USTP": "Cagayan de Oro City",
                            "University of Southeastern Philippines": "Davao City",
                            "University of Southern Mindanao": "Kabacan, Cotabato",
                            "University of Sto Tomas Legazpi Bicol Dominican University": "Legazpi City, Albay",
                            "University of the Assumption": "San Fernando City, Pampanga",
                            "University of the City of Manila": "Intramuros, Manila",
                            "University of the Cordilleras (Baguio Colleges Foundation)": "Baguio City",
                            "University of the East Ramon Magsaysay": "Quezon City, Metro Manila",
                            "University of the East": "Sampaloc, Manila",
                            "University of the Immaculate Conception": "Davao City",
                            "University of the Philippines Diliman": "Diliman, Quezon City",
                            "University of the Philippines Baguio": "Baguio City",
                            "University of the Philippines Cebu": "Cebu City",
                            "University of the Philippines Manila": "Ermita, Manila",
                            "University of the Philippines Mindanao": "Mintal, Davao City",
                            "University of the Philippines Visayas": "Iloilo City, Iloilo",
                            "University of the Philippines": "Ermita, Manila",
                            "University of the Visayas": "Cebu City, Cebu",
                            "Urdaneta City University": "Urdaneta City, Pangasinan",
                            "Virgen Milagrosa University Foundation": "San Carlos City, Pangasinan",
                            "Visayas State University": "Baybay City, Leyte",
                            "Wesleyan University Philippines": "Cabanatuan City, Nueva Ecija",
                            "West Visayas State University": "La Paz, Iloilo City",
                            "Western Institute of Technology": "Iloilo City, Iloilo",
                            "Western Leyte College of Ormoc City": "Ormoc City, Leyte",
                            "Western Mindanao State University": "Zamboanga City",
                            "Western Philippines University": "Aborlan, Palawan",
                            "Xavier University Ateneo de Cagayan": "Cagayan de Oro City",
                            "Zamboanga Peninsula Polytechnic State University": "Dipolog City, Zamboanga del Norte",
                            "Zamboanga State College of Marine Sciences and Technology": "Zamboanga City, Zamboanga del Sur",

              
    }
    # school_addresses = {
    #     "Ateneo de Manila University": "Katipunan Ave, Quezon City",
    #     "Far Eastern University": "Sampaloc, Manila",
    #     "Polytechnic University of the Philippines": "Sta. Mesa, Manila",
    #     "Polytechnic University of the Philippines-San Juan": "San Juan, Metro Manila",
    #     "Polytechnic University of the Philippines-Parañaque": "Parañaque, Metro Manila",
    #     "Polytechnic University of the Philippines-Taguig": "Taguig, Metro Manila",
    #     "Philippines Science High School": "Agham Rd, Diliman, Quezon City",
    #     "University of the East": "Sampaloc, Manila",
    #     "Japan-Philippines Institute of Technology-Plaridel": "Plaridel, Bulacan",
    #     "Technological Institute of the Philippines": "Manila, Metro Manila",
    #     "Technological University of the Philippines": "Ermita, Manila",
    #     "University of the Philippines-Diliman": "Diliman, Quezon City",
    #     "University of the Philippines-Los Baños": "Los Baños, Laguna",
    # }

    # Provide me a list of college Universities in the Philippines

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


    