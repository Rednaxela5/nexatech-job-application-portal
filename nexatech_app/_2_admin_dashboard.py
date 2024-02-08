from pathlib import Path
import sys
import os

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, Frame, BOTH
from PIL import Image, ImageTk
from _2_admin_dashboard_d import dash
from _2_admin_new_applicant import new_app
from _2_admin_applicants import applicant
from _2_admin_about import about


# Get the script's directory path
SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

# Set the relative path to the assets directory
ASSETS_PATH = SCRIPT_DIR / "assets" / "dash_frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def dashboard():
    


    def logout_clicked():
        # Close the login window
        window.destroy()
        # Open the main application window
        from _1_login_page import login_menu
        login_menu()

    def delete_pages():
        for frame in main_frame.winfo_children():
            frame.forget()

    # Function to handle button press
    def handle_button_press(btn_name):
        global current_window
        if btn_name == "dash":
            current_window = dash(window)
        elif btn_name == "new_applicant":
            current_window = new_app(window)
        elif btn_name == "applicant":
            current_window = applicant(window)
        elif btn_name == "about":
            current_window = about(window)


    def hide_indicators():
        db_indicate.config(bg="#0f2634")
        new_applicant_indicate.config(bg="#0f2634")
        applicant_indicate.config(bg="#0f2634")
        about_indicate.config(bg="#0f2634")

    def indicate(lb, page):

        hide_indicators()
        lb.config(bg="#FFFFFF")
        # delete_pages()
        handle_button_press(page)

    # Functions for changing tabs with buttons
    # def dash_button_clicked():
    #     print("Dashboard button clicked")
    #     canvas.itemconfig(page_navigator, text="Dashboard")
    #     sidebar_navigator.place




    # def new_applicant_clicked():
    #     new_applicant_frame = Frame(main_frame)


    #     lb = Label(new_applicant_frame, text="New Applicant\n\nPage: 2", bg="#CCD4D9", fg="#464040", font=("Montserrat", 20, "bold"))
    #     lb.pack()

    #     new_applicant_frame.pack(pady=20)
    
    # def applicant_clicked():
    #     applicant_frame = Frame(main_frame)


    #     lb = Label(applicant_frame, text="Applicants\n\nPage: 3", bg="#CCD4D9", fg="#464040", font=("Montserrat", 20, "bold"))
    #     lb.pack()

    #     book_title = Label(applicant_frame, text="Book Title")
    #     book_title.pack()

    #     book_entry = Entry(applicant_frame)
    #     book_entry.pack()

    #     applicant_frame.pack(pady=20)

    # def about_clicked():
    #     about_frame = Frame(main_frame)


    #     lb = Label(about_frame, text="About\n\nPage: 4", bg="#CCD4D9", fg="#464040", font=("Montserrat", 20, "bold"))
    #     lb.pack()

    #     about_frame.pack(pady=20)

    
    
        

    # --------------------------------------------------------------------------------#
    # ---------------------------------- GUI SETUP ---------------------------------- #
    # --------------------------------------------------------------------------------#
    
    window = Tk()
    window.title("Nexatech Job Portal")
    window.geometry("1024x568")
    window.configure(bg = "#0F2634")

    icon_img = PhotoImage(file=relative_to_assets("job_logo.png"))
    window.iconphoto(False, icon_img)

    
   
    
    
    canvas = Canvas(
        window,
        bg = "#0F2634",
        height = 568,
        width = 1024,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)

    # Main Frame
    canvas.create_rectangle(
        208.0,
        0.0,
        1024.0,
        568.0,
        fill="#CCD4D9",
        outline="")

    # Header Frame
    canvas.create_rectangle(
        208.0,
        0.0,
        1024.0,
        67.0,
        fill="#C0C5C8",
        outline="")

    # Option Frame
    canvas.create_rectangle(
        0.0,
        0.0,
        208.0,
        568.0,
        fill="#0F2634",
        outline="")


    canvas.create_text(
        231.0,
        20.0,
        anchor="nw",
        text="System Administration",
        fill="#0F2634",
        font=("Montserrat", "14", "bold")
    )

    # User Profile
    canvas.create_text(
        769.0,
        20.0,
        anchor="nw",
        text="Alexander Porlares",
        fill="#0F2634",
        font=("Montserrat", "14", "bold")
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        101.0,
        33.0,
        image=image_image_2
    )
    main_frame = Frame(window, bg="#ccd3d8")
    main_frame.place(x=208, y=67, height=816, width=568)
    main_frame.configure(height=816, width=501)

    
    
    # --------------------------------------------------------------------------------#
    # ----------------------------------- BUTTONS ----------------------------------- #
    # --------------------------------------------------------------------------------#

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        activebackground="#c0c5c8",
        cursor='hand2',
        relief="flat"
    )
    button_1.place(
        x=963.0,
        y=9.0,
        width=48.0,
        height=48.0
    )

    button_image_hover_1 = PhotoImage(
        file=relative_to_assets("button_hover_1.png"))

    def button_1_hover(e):
        button_1.config(
            image=button_image_hover_1
        )
    def button_1_leave(e):
        button_1.config(
            image=button_image_1
        )

    button_1.bind('<Enter>', button_1_hover)
    button_1.bind('<Leave>', button_1_leave)


    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=logout_clicked,
        activebackground="#0F2634",
        cursor='hand2',
        relief="flat"
    )
    button_2.place(
        x=4.0,
        y=516.0,
        width=200.0,
        height=47.0
    )

    button_image_hover_2 = PhotoImage(
        file=relative_to_assets("button_hover_2.png"))

    def button_2_hover(e):
        button_2.config(
            image=button_image_hover_2
        )
    def button_2_leave(e):
        button_2.config(
            image=button_image_2
        )

    button_2.bind('<Enter>', button_2_hover)
    button_2.bind('<Leave>', button_2_leave)


    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: indicate(about_indicate, handle_button_press("about")),
        activebackground="#0F2634",
        cursor='hand2',
        relief="flat"
    )
    button_3.place(
        x=4.0,
        y=231.0,
        width=200.0,
        height=47.0
    )

    button_image_hover_3 = PhotoImage(
        file=relative_to_assets("button_hover_3.png"))

    def button_3_hover(e):
        button_3.config(
            image=button_image_hover_3
        )
    def button_3_leave(e):
        button_3.config(
            image=button_image_3
        )

    button_3.bind('<Enter>', button_3_hover)
    button_3.bind('<Leave>', button_3_leave)

    about_indicate = Label(window, text='', bg="#0F2634")
    about_indicate.place(x=4.0, y=231, height=47.0, width=3)


    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: indicate(applicant_indicate, handle_button_press("applicant")),
        activebackground="#0F2634",
        cursor='hand2',
        relief="flat"
    )
    button_4.place(
        x=4.0,
        y=184.0,
        width=200.0,
        height=47.0
    )

    button_image_hover_4 = PhotoImage(
        file=relative_to_assets("button_hover_4.png"))

    def button_4_hover(e):
        button_4.config(
            image=button_image_hover_4
        )
    def button_4_leave(e):
        button_4.config(
            image=button_image_4
        )

    button_4.bind('<Enter>', button_4_hover)
    button_4.bind('<Leave>', button_4_leave)

    applicant_indicate = Label(window, text='', bg="#0F2634")
    applicant_indicate.place(x=4.0, y=184, height=47.0, width=3)

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: indicate(new_applicant_indicate, handle_button_press("new_applicant")),
        activebackground="#0F2634",
        cursor='hand2',
        relief="flat"
    )
    button_5.place(
        x=4.0,
        y=137.0,
        width=200.0,
        height=47.0
    )

    button_image_hover_5 = PhotoImage(
        file=relative_to_assets("button_hover_5.png"))

    def button_5_hover(e):
        button_5.config(
            image=button_image_hover_5
        )
    def button_5_leave(e):
        button_5.config(
            image=button_image_5
        )

    button_5.bind('<Enter>', button_5_hover)
    button_5.bind('<Leave>', button_5_leave)

    new_applicant_indicate = Label(window, text='', bg="#0F2634")
    new_applicant_indicate.place(x=4.0, y=137, height=47.0, width=3)

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: indicate(db_indicate, handle_button_press("dash")),
        activebackground="#0F2634",
        cursor='hand2',
        relief="flat"
    )
    button_6.place(
        x=4.0,
        y=90.0,
        width=200.0,
        height=47.0
    )

    button_image_hover_6 = PhotoImage(
        file=relative_to_assets("button_hover_6.png"))

    def button_6_hover(e):
        button_6.config(
            image=button_image_hover_6
        )
    def button_6_leave(e):
        button_6.config(
            image=button_image_6
        )

    button_6.bind('<Enter>', button_6_hover)
    button_6.bind('<Leave>', button_6_leave)

    db_indicate = Label(window, text='', bg="#0F2634")
    db_indicate.place(x=4.0, y=90, height=47.0, width=3)

    # EXPERIMENTAL
    # window.bind('<Button-1>', keep_flat) 

    indicate(db_indicate, "dash")
    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    dashboard()