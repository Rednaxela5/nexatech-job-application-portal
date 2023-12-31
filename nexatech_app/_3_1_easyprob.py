from pathlib import Path
import sys
import os
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from tkinter import ttk
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
import mysql.connector

def easy_1_main():
    # Get the script's directory path
    SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

    # Set the relative path to the assets directory
    ASSETS_PATH = SCRIPT_DIR / "assets" / "frame3"

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def back_clicked():
        window.destroy()
        from _3_0_easy_window import easy_main
        easy_main()

    def easy_2_clicked():
        window.destroy()
        from _3_2_easyprob import easy_2_main
        easy_2_main()

    def display_easy_1_clicked():
        canvas.create_text(
            460.0,
            348.0,
            anchor="c",
            text="""            SELECT applicantNo, name, SSS_ID, emailAddress, 
            desiredSalary 
            FROM aplicant_details 
            ORDER BY desiredSalary ASC;""",
            fill="#0F2634",
            font=("Montserrat", 35 * -1)
        )
        def display_results(results):
            # Remove the previous contents of the image area
            for widget in canvas.winfo_children():
                widget.destroy()
            
            result_window = tk.Toplevel(window)
            result_window.title("Query Results")
            result_window.geometry("994x326")
            result_window.resizable(width=True, height=True)
            style = ttk.Style()
            style.configure("Treeview.Heading", font=("Gotham", 11, "bold"))
            style.configure("Treeview", font=("Gotham", 9))
            tree = ttk.Treeview(result_window)
            tree["columns"] = ("applicantNo", "name", "SSS_ID", "emailAddress", "desiredSalary")
            tree.column("#0", width=0, stretch=tk.NO)
            tree.heading("applicantNo", text="Applicant No.", anchor="w")
            tree.heading("name", text="Name", anchor="w")
            tree.heading("SSS_ID", text="SSS ID", anchor="w")
            tree.heading("emailAddress", text="Email Address", anchor="w")
            tree.heading("desiredSalary", text="Desired Salary", anchor="w")
          
            for i, row in enumerate(results):
                tree.insert("", "end", text=str(i+1), values=row)

            tree.pack(expand=True, fill=tk.BOTH)
        
        
        # Replace these with your actual database credentials
        # MYSQL_HOST = 'localhost'
        # MYSQL_USER = 'root'
        # MYSQL_PASSWORD = 'P@ssw0rd2023!'
        # MYSQL_DATABASE = 'nexatech'

        try:
            # Connect to the database
            connection = mysql.connector.connect(
                host=MYSQL_HOST,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DATABASE
            )
            cursor = connection.cursor()

            # Execute the query
            query = "SELECT applicantNo, name, SSS_ID, emailAddress, desiredSalary FROM applicant_details ORDER BY desiredSalary ASC;"
            cursor.execute(query)
            results = cursor.fetchall()

            # Display the results in a new window
            display_results(results)

            # Close the cursor and connection
            cursor.close()
            connection.close()

        except mysql.connector.Error as e:
                print(f"Error connecting to the database: {e}")

    window = Tk()

    window.geometry("1024x568")
    window.configure(bg = "#CCD4D9")
    window.title("Nexatech System Administration")


    canvas = Canvas(
        window,
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
        22.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=back_clicked,
        relief="flat"
    )
    button_1.place(
        x=15.0,
        y=64.0,
        width=113.0,
        height=44.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=easy_2_clicked,
        relief="flat"
    )
    button_2.place(
        x=873.0,
        y=64.0,
        width=136.0,
        height=44.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=display_easy_1_clicked,
        relief="flat"
    )
    button_3.place(
        x=436.0,
        y=519.0,
        width=134.0,
        height=36.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        500.0,
        86.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        511.0,
        153.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        511.0,
        348.0,
        image=image_image_4
    )
    window.resizable(False, False)
    window.mainloop()
# easy_1_main()