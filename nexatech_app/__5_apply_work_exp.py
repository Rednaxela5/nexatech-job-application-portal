from pathlib import Path
import sys
import tkinter as tk
from tkinter import Tk, Canvas, Button, PhotoImage, Entry, ttk, messagebox
from tkcalendar import DateEntry
from default_entry import DefaultTextEntry
from storage import work_data_1 as wd1, work_data_2 as wd2, work_data_3 as wd3, work_data_4 as wd4, work_data_5 as wd5, work_data_6 as wd6, work_data_7 as wd7, work_data_8 as wd8, work_data_9 as wd9, work_data_10 as wd10


# Get the script's directory path
SCRIPT_DIR = Path(sys.argv[0]).resolve().parent

# Set the relative path to the assets directory
ASSETS_PATH = SCRIPT_DIR / "assets" / "apply_frame4"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def back_clicked(parent):
    prev_company = prev_company_entry.get()
    work_position = work_position_entry.get()
    work_date_started = work_date_started_entry.get_date()
    work_date_ended = work_date_ended_entry.get()
    reason_for_leaving = reason_for_leaving_entry.get()
    if wd1.cur_work_exp == 1:
        wd1.prev_company = prev_company
        wd1.work_position = work_position
        wd1.work_date_started = work_date_started
        wd1.work_date_ended = work_date_ended
        wd1.reason_for_leaving = reason_for_leaving

        # For Debugging Purposes
        print("Previous Company: ", wd1.prev_company)
        print("Work Position: ", wd1.work_position)
        print("Work Date Started: ", wd1.work_date_started)
        print("Work Date Ended: ", wd1.work_date_ended)
        print("Reason for Leaving: ", wd1.reason_for_leaving)

    elif wd1.cur_work_exp == 2:
        wd2.prev_company = prev_company
        wd2.work_position = work_position
        wd2.work_date_started = work_date_started
        wd2.work_date_ended = work_date_ended
        wd2.reason_for_leaving = reason_for_leaving

        # For Debugging Purposes
        print("Previous Company: ", wd2.prev_company)
        print("Work Position: ", wd2.work_position)
        print("Work Date Started: ", wd2.work_date_started)
        print("Work Date Ended: ", wd2.work_date_ended)
        print("Reason for Leaving: ", wd2.reason_for_leaving)

    elif wd1.cur_work_exp == 3:
        wd3.prev_company = prev_company
        wd3.work_position = work_position
        wd3.work_date_started = work_date_started
        wd3.work_date_ended = work_date_ended
        wd3.reason_for_leaving = reason_for_leaving

        # For Debugging Purposes
        print("Previous Company: ", wd3.prev_company)
        print("Work Position: ", wd3.work_position)
        print("Work Date Started: ", wd3.work_date_started)
        print("Work Date Ended: ", wd3.work_date_ended)
        print("Reason for Leaving: ", wd3.reason_for_leaving)

    elif wd1.cur_work_exp == 4:
        wd4.prev_company = prev_company
        wd4.work_position = work_position
        wd4.work_date_started = work_date_started
        wd4.work_date_ended = work_date_ended
        wd4.reason_for_leaving = reason_for_leaving

        # For Debugging Purposes
        print("Previous Company: ", wd4.prev_company)
        print("Work Position: ", wd4.work_position)
        print("Work Date Started: ", wd4.work_date_started)
        print("Work Date Ended: ", wd4.work_date_ended)
        print("Reason for Leaving: ", wd4.reason_for_leaving)

    elif wd1.cur_work_exp == 5:
        wd5.prev_company = prev_company
        wd5.work_position = work_position
        wd5.work_date_started = work_date_started
        wd5.work_date_ended = work_date_ended
        wd5.reason_for_leaving = reason_for_leaving

        # For Debugging Purposes
        print("Previous Company: ", wd5.prev_company)
        print("Work Position: ", wd5.work_position)
        print("Work Date Started: ", wd5.work_date_started)
        print("Work Date Ended: ", wd5.work_date_ended)
        print("Reason for Leaving: ", wd5.reason_for_leaving)

    elif wd1.cur_work_exp == 6:
        wd6.prev_company = prev_company
        wd6.work_position = work_position
        wd6.work_date_started = work_date_started
        wd6.work_date_ended = work_date_ended
        wd6.reason_for_leaving = reason_for_leaving

        # For Debugging Purposes
        print("Previous Company: ", wd6.prev_company)
        print("Work Position: ", wd6.work_position)
        print("Work Date Started: ", wd6.work_date_started)
        print("Work Date Ended: ", wd6.work_date_ended)
        print("Reason for Leaving: ", wd6.reason_for_leaving)

    elif wd1.cur_work_exp == 7:
        wd7.prev_company = prev_company
        wd7.work_position = work_position
        wd7.work_date_started = work_date_started
        wd7.work_date_ended = work_date_ended
        wd7.reason_for_leaving = reason_for_leaving

        # For Debugging Purposes
        print("Previous Company: ", wd7.prev_company)
        print("Work Position: ", wd7.work_position)
        print("Work Date Started: ", wd7.work_date_started)
        print("Work Date Ended: ", wd7.work_date_ended)
        print("Reason for Leaving: ", wd7.reason_for_leaving)

    elif wd1.cur_work_exp == 8:
        wd8.prev_company = prev_company
        wd8.work_position = work_position
        wd8.work_date_started = work_date_started
        wd8.work_date_ended = work_date_ended
        wd8.reason_for_leaving = reason_for_leaving

        # For Debugging Purposes
        print("Previous Company: ", wd8.prev_company)
        print("Work Position: ", wd8.work_position)
        print("Work Date Started: ", wd8.work_date_started)
        print("Work Date Ended: ", wd8.work_date_ended)
        print("Reason for Leaving: ", wd8.reason_for_leaving)

    elif wd1.cur_work_exp == 9:
        wd9.prev_company = prev_company
        wd9.work_position = work_position
        wd9.work_date_started = work_date_started
        wd9.work_date_ended = work_date_ended
        wd9.reason_for_leaving = reason_for_leaving

        # For Debugging Purposes
        print("Previous Company: ", wd9.prev_company)
        print("Work Position: ", wd9.work_position)
        print("Work Date Started: ", wd9.work_date_started)
        print("Work Date Ended: ", wd9.work_date_ended)
        print("Reason for Leaving: ", wd9.reason_for_leaving)

    elif wd1.cur_work_exp == 10:
        wd10.prev_company = prev_company
        wd10.work_position = work_position
        wd10.work_date_started = work_date_started
        wd10.work_date_ended = work_date_ended
        wd10.reason_for_leaving = reason_for_leaving

        # For Debugging Purposes
        print("Previous Company: ", wd10.prev_company)
        print("Work Position: ", wd10.work_position)
        print("Work Date Started: ", wd10.work_date_started)
        print("Work Date Ended: ", wd10.work_date_ended)
        print("Reason for Leaving: ", wd10.reason_for_leaving)

    from __4_apply_education import education_main
    education_main(parent)

def next_clicked(parent):
    prev_company = prev_company_entry.get()
    work_position = work_position_entry.get()
    work_date_started = work_date_started_entry.get_date()
    work_date_ended = work_date_ended_entry.get()
    reason_for_leaving = reason_for_leaving_entry.get()

    if prev_company == d_prev_company_entry or work_position == d_work_position_entry or work_date_started == "" or work_date_ended == "" or reason_for_leaving == d_reason_for_leaving:
        messagebox.showerror("Error", "Please fill out all fields.")
    else:
        if wd1.cur_work_exp == 1:
            wd1.prev_company = prev_company
            wd1.work_position = work_position
            wd1.work_date_started = work_date_started
            wd1.work_date_ended = work_date_ended
            wd1.reason_for_leaving = reason_for_leaving

            # For Debugging Purposes
            print("Previous Company: " , wd1.prev_company)
            print("Work Position: " , wd1.work_position)
            print("Work Date Started: " , wd1.work_date_started)
            print("Work Date Ended: " , wd1.work_date_ended)
            print("Reason for Leaving: " , wd1.reason_for_leaving)

        elif wd1.cur_work_exp == 2:
            wd2.prev_company = prev_company
            wd2.work_position = work_position
            wd2.work_date_started = work_date_started
            wd2.work_date_ended = work_date_ended
            wd2.reason_for_leaving = reason_for_leaving

            # For Debugging Purposes
            print("Previous Company: ", wd2.prev_company)
            print("Work Position: ", wd2.work_position)
            print("Work Date Started: ", wd2.work_date_started)
            print("Work Date Ended: ", wd2.work_date_ended)
            print("Reason for Leaving: ", wd2.reason_for_leaving)

        elif wd1.cur_work_exp == 3:
            wd3.prev_company = prev_company
            wd3.work_position = work_position
            wd3.work_date_started = work_date_started
            wd3.work_date_ended = work_date_ended
            wd3.reason_for_leaving = reason_for_leaving

            # For Debugging Purposes
            print("Previous Company: ", wd3.prev_company)
            print("Work Position: ", wd3.work_position)
            print("Work Date Started: ", wd3.work_date_started)
            print("Work Date Ended: ", wd3.work_date_ended)
            print("Reason for Leaving: ", wd3.reason_for_leaving)


        elif wd1.cur_work_exp == 4:
            wd4.prev_company = prev_company
            wd4.work_position = work_position
            wd4.work_date_started = work_date_started
            wd4.work_date_ended = work_date_ended
            wd4.reason_for_leaving = reason_for_leaving

            # For Debugging Purposes
            print("Previous Company: ", wd4.prev_company)
            print("Work Position: ", wd4.work_position)
            print("Work Date Started: ", wd4.work_date_started)
            print("Work Date Ended: ", wd4.work_date_ended)
            print("Reason for Leaving: ", wd4.reason_for_leaving)

        elif wd1.cur_work_exp == 5:
            wd5.prev_company = prev_company
            wd5.work_position = work_position
            wd5.work_date_started = work_date_started
            wd5.work_date_ended = work_date_ended
            wd5.reason_for_leaving = reason_for_leaving

            # For Debugging Purposes
            print("Previous Company: ", wd5.prev_company)
            print("Work Position: ", wd5.work_position)
            print("Work Date Started: ", wd5.work_date_started)
            print("Work Date Ended: ", wd5.work_date_ended)
            print("Reason for Leaving: ", wd5.reason_for_leaving)

        
        elif wd1.cur_work_exp == 6:
            wd6.prev_company = prev_company
            wd6.work_position = work_position
            wd6.work_date_started = work_date_started
            wd6.work_date_ended = work_date_ended
            wd6.reason_for_leaving = reason_for_leaving

            # For Debugging Purposes
            print("Previous Company: ", wd6.prev_company)
            print("Work Position: ", wd6.work_position)
            print("Work Date Started: ", wd6.work_date_started)
            print("Work Date Ended: ", wd6.work_date_ended)
            print("Reason for Leaving: ", wd6.reason_for_leaving)

        elif wd1.cur_work_exp == 7:
            wd7.prev_company = prev_company
            wd7.work_position = work_position
            wd7.work_date_started = work_date_started
            wd7.work_date_ended = work_date_ended
            wd7.reason_for_leaving = reason_for_leaving

            # For Debugging Purposes
            print("Previous Company: ", wd7.prev_company)
            print("Work Position: ", wd7.work_position)
            print("Work Date Started: ", wd7.work_date_started)
            print("Work Date Ended: ", wd7.work_date_ended)
            print("Reason for Leaving: ", wd7.reason_for_leaving)

        elif wd1.cur_work_exp == 8:
            wd8.prev_company = prev_company
            wd8.work_position = work_position
            wd8.work_date_started = work_date_started
            wd8.work_date_ended = work_date_ended
            wd8.reason_for_leaving = reason_for_leaving

            # For Debugging Purposes
            print("Previous Company: ", wd8.prev_company)
            print("Work Position: ", wd8.work_position)
            print("Work Date Started: ", wd8.work_date_started)
            print("Work Date Ended: ", wd8.work_date_ended)
            print("Reason for Leaving: ", wd8.reason_for_leaving)
            
        elif wd1.cur_work_exp == 9:
            wd9.prev_company = prev_company
            wd9.work_position = work_position
            wd9.work_date_started = work_date_started
            wd9.work_date_ended = work_date_ended
            wd9.reason_for_leaving = reason_for_leaving

            # For Debugging Purposes
            print("Previous Company: ", wd9.prev_company)
            print("Work Position: ", wd9.work_position)
            print("Work Date Started: ", wd9.work_date_started)
            print("Work Date Ended: ", wd9.work_date_ended)
            print("Reason for Leaving: ", wd9.reason_for_leaving)

        elif wd1.cur_work_exp == 10:
            wd10.prev_company = prev_company
            wd10.work_position = work_position
            wd10.work_date_started = work_date_started
            wd10.work_date_ended = work_date_ended
            wd10.reason_for_leaving = reason_for_leaving

            # For Debugging Purposes
            print("Previous Company: ", wd10.prev_company)
            print("Work Position: ", wd10.work_position)
            print("Work Date Started: ", wd10.work_date_started)
            print("Work Date Ended: ", wd10.work_date_ended)
            print("Reason for Leaving: ", wd10.reason_for_leaving)

        from __6_apply_major_skills import major_skill_main
        major_skill_main(parent)

def display_values():
    if wd1.cur_work_exp == 1:  # Check if there are any entries in the list
        # Previous Company
        if wd1.prev_company == d_prev_company_entry:
            pass
        elif wd1.prev_company != "":
            prev_company_entry.delete(0, tk.END)
            prev_company_entry.insert(0, wd1.prev_company)
            prev_company_entry.config(fg="black")

        # Work Position
        if wd1.work_position == d_work_position_entry:
            pass
        elif wd1.work_position != "":
            work_position_entry.delete(0, tk.END)
            work_position_entry.insert(0, wd1.work_position)
            work_position_entry.config(fg="black")

        # Work Date Started
        if wd1.work_date_started != "":
            work_date_started_entry.set_date(wd1.work_date_started)

        # Work Date Ended
        if wd1.work_date_started != "":
            work_date_ended_entry.set_date(wd1.work_date_ended)

        # Reason for Leaving
        if wd1.reason_for_leaving == d_reason_for_leaving:
            pass
        elif wd1.reason_for_leaving != "":
            reason_for_leaving_entry.delete(0, tk.END)
            reason_for_leaving_entry.insert(0, wd1.reason_for_leaving)
            reason_for_leaving_entry.config(fg="black")
    if wd1.cur_work_exp == 2:  # Check if there are any entries in the list
        # Previous Company
        if wd2.prev_company == d_prev_company_entry:
            pass
        elif wd2.prev_company != "":
            prev_company_entry.delete(0, tk.END)
            prev_company_entry.insert(0, wd2.prev_company)
            prev_company_entry.config(fg="black")

        # Work Position
        if wd2.work_position == d_work_position_entry:
            pass
        elif wd2.work_position != "":
            work_position_entry.delete(0, tk.END)
            work_position_entry.insert(0, wd2.work_position)
            work_position_entry.config(fg="black")

        # Work Date Started
        if wd2.work_date_started != "":
            work_date_started_entry.set_date(wd2.work_date_started)

        # Work Date Ended
        if wd2.work_date_started != "":
            work_date_ended_entry.set_date(wd2.work_date_ended)

        # Reason for Leaving
        if wd2.reason_for_leaving == d_reason_for_leaving:
            pass
        elif wd2.reason_for_leaving != "":
            reason_for_leaving_entry.delete(0, tk.END)
            reason_for_leaving_entry.insert(0, wd2.reason_for_leaving)
            reason_for_leaving_entry.config(fg="black")
    if wd1.cur_work_exp == 3:  # Check if there are any entries in the list
        # Previous Company
        if wd3.prev_company == d_prev_company_entry:
            pass
        elif wd3.prev_company != "":
            prev_company_entry.delete(0, tk.END)
            prev_company_entry.insert(0, wd3.prev_company)
            prev_company_entry.config(fg="black")

        # Work Position
        if wd3.work_position == d_work_position_entry:
            pass
        elif wd3.work_position != "":
            work_position_entry.delete(0, tk.END)
            work_position_entry.insert(0, wd3.work_position)
            work_position_entry.config(fg="black")

        # Work Date Started
        if wd3.work_date_started != "":
            work_date_started_entry.set_date(wd3.work_date_started)

        # Work Date Ended
        if wd3.work_date_started != "":
            work_date_ended_entry.set_date(wd3.work_date_ended)

        # Reason for Leaving
        if wd3.reason_for_leaving == d_reason_for_leaving:
            pass
        elif wd3.reason_for_leaving != "":
            reason_for_leaving_entry.delete(0, tk.END)
            reason_for_leaving_entry.insert(0, wd3.reason_for_leaving)
            reason_for_leaving_entry.config(fg="black")

    if wd1.cur_work_exp == 4:  # Check if there are any entries in the list
        # Previous Company
        if wd4.prev_company == d_prev_company_entry:
            pass
        elif wd4.prev_company != "":
            prev_company_entry.delete(0, tk.END)
            prev_company_entry.insert(0, wd4.prev_company)
            prev_company_entry.config(fg="black")
        
        # Work Position
        if wd4.work_position == d_work_position_entry:
            pass
        elif wd4.work_position != "":
            work_position_entry.delete(0, tk.END)
            work_position_entry.insert(0, wd4.work_position)
            work_position_entry.config(fg="black")
        
        # Work Date Started
        if wd4.work_date_started != "":
            work_date_started_entry.set_date(wd4.work_date_started)
        
        # Work Date Ended
        if wd4.work_date_started != "":
            work_date_ended_entry.set_date(wd4.work_date_ended)

        # Reason for Leaving
        if wd4.reason_for_leaving == d_reason_for_leaving:
            pass
        elif wd4.reason_for_leaving != "":
            reason_for_leaving_entry.delete(0, tk.END)
            reason_for_leaving_entry.insert(0, wd4.reason_for_leaving)
            reason_for_leaving_entry.config(fg="black")
    
    if wd1.cur_work_exp == 5:  # Check if there are any entries in the list
        # Previous Company
        if wd5.prev_company == d_prev_company_entry:
            pass
        elif wd5.prev_company != "":
            prev_company_entry.delete(0, tk.END)
            prev_company_entry.insert(0, wd5.prev_company)
            prev_company_entry.config(fg="black")
        
        # Work Position
        if wd5.work_position == d_work_position_entry:
            pass
        elif wd5.work_position != "":
            work_position_entry.delete(0, tk.END)
            work_position_entry.insert(0, wd5.work_position)
            work_position_entry.config(fg="black")
        
        # Work Date Started
        if wd5.work_date_started != "":
            work_date_started_entry.set_date(wd5.work_date_started)
        
        # Work Date Ended
        if wd5.work_date_started != "":
            work_date_ended_entry.set_date(wd5.work_date_ended)
        
        # Reason for Leaving
        if wd5.reason_for_leaving == d_reason_for_leaving:
            pass
        elif wd5.reason_for_leaving != "":
            reason_for_leaving_entry.delete(0, tk.END)
            reason_for_leaving_entry.insert(0, wd5.reason_for_leaving)
            reason_for_leaving_entry.config(fg="black")
        
    if wd1.cur_work_exp == 6:  # Check if there are any entries in the list
        # Previous Company
        if wd6.prev_company == d_prev_company_entry:
            pass
        elif wd6.prev_company != "":
            prev_company_entry.delete(0, tk.END)
            prev_company_entry.insert(0, wd6.prev_company)
            prev_company_entry.config(fg="black")
        
        # Work Position
        if wd6.work_position == d_work_position_entry:
            pass
        elif wd6.work_position != "":
            work_position_entry.delete(0, tk.END)
            work_position_entry.insert(0, wd6.work_position)
            work_position_entry.config(fg="black")
        
        # Work Date Started
        if wd6.work_date_started != "":
            work_date_started_entry.set_date(wd6.work_date_started)
        
        # Work Date Ended
        if wd6.work_date_started != "":
            work_date_ended_entry.set_date(wd6.work_date_ended)
        
        # Reason for Leaving
        if wd6.reason_for_leaving == d_reason_for_leaving:
            pass  
        elif wd6.reason_for_leaving != "":
            reason_for_leaving_entry.delete(0, tk.END)
            reason_for_leaving_entry.insert(0, wd6.reason_for_leaving)
            reason_for_leaving_entry.config(fg="black")
    
    if wd1.cur_work_exp == 7:  # Check if there are any entries in the list
        # Previous Company
        if wd7.prev_company == d_prev_company_entry:
            pass
        elif wd7.prev_company != "":
            prev_company_entry.delete(0, tk.END)
            prev_company_entry.insert(0, wd7.prev_company)
            prev_company_entry.config(fg="black")
        
        # Work Position
        if wd7.work_position == d_work_position_entry:
            pass
        elif wd7.work_position != "":
            work_position_entry.delete(0, tk.END)
            work_position_entry.insert(0, wd7.work_position)
            work_position_entry.config(fg="black")
        
        # Work Date Started
        if wd7.work_date_started != "":
            work_date_started_entry.set_date(wd7.work_date_started)
        
        # Work Date Ended
        if wd7.work_date_started != "":
            work_date_ended_entry.set_date(wd7.work_date_ended)
        
        # Reason for Leaving
        if wd7.reason_for_leaving == d_reason_for_leaving:
            pass
        elif wd7.reason_for_leaving != "":
            reason_for_leaving_entry.delete(0, tk.END)
            reason_for_leaving_entry.insert(0, wd7.reason_for_leaving)
            reason_for_leaving_entry.config(fg="black")
        
    if wd1.cur_work_exp == 8:  # Check if there are any entries in the list
        # Previous Company
        if wd8.prev_company == d_prev_company_entry:
            pass
        elif wd8.prev_company != "":
            prev_company_entry.delete(0, tk.END)
            prev_company_entry.insert(0, wd8.prev_company)
            prev_company_entry.config(fg="black")
        
        # Work Position
        if wd8.work_position == d_work_position_entry:
            pass
        elif wd8.work_position != "":
            work_position_entry.delete(0, tk.END)
            work_position_entry.insert(0, wd8.work_position)
            work_position_entry.config(fg="black")
        
        # Work Date Started
        if wd8.work_date_started != "":
            work_date_started_entry.set_date(wd8.work_date_started)
        
        # Work Date Ended
        if wd8.work_date_started != "":
            work_date_ended_entry.set_date(wd8.work_date_ended)
        
        # Reason for Leaving
        if wd8.reason_for_leaving == d_reason_for_leaving:
            pass
        elif wd8.reason_for_leaving != "":
            reason_for_leaving_entry.delete(0, tk.END)
            reason_for_leaving_entry.insert(0, wd8.reason_for_leaving)
            reason_for_leaving_entry.config(fg="black")
    
    if wd1.cur_work_exp == 9:  # Check if there are any entries in the list
        # Previous Company
        if wd9.prev_company == d_prev_company_entry:
            pass
        elif wd9.prev_company != "":
            prev_company_entry.delete(0, tk.END)
            prev_company_entry.insert(0, wd9.prev_company)
            prev_company_entry.config(fg="black")
        
        # Work Position
        if wd9.work_position == d_work_position_entry:
            pass
        elif wd9.work_position != "":
            work_position_entry.delete(0, tk.END)
            work_position_entry.insert(0, wd9.work_position)
            work_position_entry.config(fg="black")
        
        # Work Date Started
        if wd9.work_date_started != "":
            work_date_started_entry.set_date(wd9.work_date_started)
        
        # Work Date Ended
        if wd9.work_date_started != "":
            work_date_ended_entry.set_date(wd9.work_date_ended)
        
        # Reason for Leaving
        if wd9.reason_for_leaving == d_reason_for_leaving:
            pass
        elif wd9.reason_for_leaving != "":
            reason_for_leaving_entry.delete(0, tk.END)
            reason_for_leaving_entry.insert(0, wd9.reason_for_leaving)
            reason_for_leaving_entry.config(fg="black")
    
    if wd1.cur_work_exp == 10: # Check if there are any entries in the list
        # Previous Company
        if wd10.prev_company == d_prev_company_entry:
            pass
        elif wd10.prev_company != "":
            prev_company_entry.delete(0, tk.END)
            prev_company_entry.insert(0, wd10.prev_company)
            prev_company_entry.config(fg="black")
        
        # Work Position
        if wd10.work_position == d_work_position_entry:
            pass
        elif wd10.work_position != "":
            work_position_entry.delete(0, tk.END)
            work_position_entry.insert(0, wd10.work_position)
            work_position_entry.config(fg="black")

        # Work Date Started
        if wd10.work_date_started != "":
            work_date_started_entry.set_date(wd10.work_date_started)
        
        # Work Date Ended
        if wd10.work_date_started != "":
            work_date_ended_entry.set_date(wd10.work_date_ended)
        
        # Reason for Leaving
        if wd10.reason_for_leaving == d_reason_for_leaving:
            pass
        elif wd10.reason_for_leaving != "":
            reason_for_leaving_entry.delete(0, tk.END)
            reason_for_leaving_entry.insert(0, wd10.reason_for_leaving)
            reason_for_leaving_entry.config(fg="black")

def add_more_clicked():
    confirmation_message = "Are you sure you want to add more entries?"

    if wd1.cur_work_exp >= 10:
        # If the limit of 3 inputs is reached, show an error message box
        messagebox.showerror("Input Limit Exceeded", "You have reached the maximum limit of inputs (3).")
    else:
        # Show the confirmation messagebox
        confirm = messagebox.askquestion("Confirmation", confirmation_message)
        if confirm == 'yes':
            prev_company = prev_company_entry.get()
            work_position = work_position_entry.get()
            work_date_started = work_date_started_entry.get_date()
            work_date_ended = work_date_ended_entry.get()
            reason_for_leaving = reason_for_leaving_entry.get()

            if prev_company == d_prev_company_entry or work_position == d_work_position_entry or work_date_started == "" or work_date_ended == "" or reason_for_leaving == d_reason_for_leaving:
                messagebox.showerror("Error", "Please fill out all fields.")
            else:
                if wd1.cur_work_exp == 1:
                    wd1.prev_company = prev_company
                    wd1.work_position = work_position
                    wd1.work_date_started = work_date_started
                    wd1.work_date_ended = work_date_ended
                    wd1.reason_for_leaving = reason_for_leaving

                    prev_company_entry.delete(0, "end")
                    work_position_entry.delete(0, "end")
                    work_date_started_entry.delete(0, "end")
                    work_date_ended_entry.delete(0, "end")
                    reason_for_leaving_entry.delete(0, "end")

                elif wd1.cur_work_exp == 2:
                    wd2.prev_company = prev_company
                    wd2.work_position = work_position
                    wd2.work_date_started = work_date_started
                    wd2.work_date_ended = work_date_ended
                    wd2.reason_for_leaving = reason_for_leaving

                    prev_company_entry.delete(0, "end")
                    work_position_entry.delete(0, "end")
                    work_date_started_entry.delete(0, "end")
                    work_date_ended_entry.delete(0, "end")
                    reason_for_leaving_entry.delete(0, "end")

                elif wd1.cur_work_exp == 3:
                    wd3.prev_company = prev_company
                    wd3.work_position = work_position
                    wd3.work_date_started = work_date_started
                    wd3.work_date_ended = work_date_ended
                    wd3.reason_for_leaving = reason_for_leaving

                    prev_company_entry.delete(0, "end")
                    work_position_entry.delete(0, "end")
                    work_date_started_entry.delete(0, "end")
                    work_date_ended_entry.delete(0, "end")
                    reason_for_leaving_entry.delete(0, "end")

                elif wd1.cur_work_exp == 4:
                    wd4.prev_company = prev_company
                    wd4.work_position = work_position
                    wd4.work_date_started = work_date_started
                    wd4.work_date_ended = work_date_ended
                    wd4.reason_for_leaving = reason_for_leaving

                    prev_company_entry.delete(0, "end")
                    work_position_entry.delete(0, "end")
                    work_date_started_entry.delete(0, "end")
                    work_date_ended_entry.delete(0, "end")
                    reason_for_leaving_entry.delete(0, "end")

                elif wd1.cur_work_exp == 5:
                    wd5.prev_company = prev_company
                    wd5.work_position = work_position
                    wd5.work_date_started = work_date_started
                    wd5.work_date_ended = work_date_ended
                    wd5.reason_for_leaving = reason_for_leaving

                    prev_company_entry.delete(0, "end")
                    work_position_entry.delete(0, "end")
                    work_date_started_entry.delete(0, "end")
                    work_date_ended_entry.delete(0, "end")
                    reason_for_leaving_entry.delete(0, "end")
                
                elif wd1.cur_work_exp == 6:
                    wd6.prev_company = prev_company
                    wd6.work_position = work_position
                    wd6.work_date_started = work_date_started
                    wd6.work_date_ended = work_date_ended
                    wd6.reason_for_leaving = reason_for_leaving
                    
                    prev_company_entry.delete(0, "end")
                    work_position_entry.delete(0, "end")
                    work_date_started_entry.delete(0, "end")
                    work_date_ended_entry.delete(0, "end")
                    reason_for_leaving_entry.delete(0, "end")
                
                elif wd1.cur_work_exp == 7:
                    wd7.prev_company = prev_company
                    wd7.work_position = work_position
                    wd7.work_date_started = work_date_started
                    wd7.work_date_ended = work_date_ended
                    wd7.reason_for_leaving = reason_for_leaving

                    prev_company_entry.delete(0, "end")
                    work_position_entry.delete(0, "end")
                    work_date_started_entry.delete(0, "end")
                    work_date_ended_entry.delete(0, "end")
                    reason_for_leaving_entry.delete(0, "end")

                elif wd1.cur_work_exp == 8:
                    wd8.prev_company = prev_company
                    wd8.work_position = work_position
                    wd8.work_date_started = work_date_started
                    wd8.work_date_ended = work_date_ended
                    wd8.reason_for_leaving = reason_for_leaving
                    
                    prev_company_entry.delete(0, "end")
                    work_position_entry.delete(0, "end")
                    work_date_started_entry.delete(0, "end")
                    work_date_ended_entry.delete(0, "end")
                    reason_for_leaving_entry.delete(0, "end")
                
                elif wd1.cur_work_exp == 9:
                    wd9.prev_company = prev_company
                    wd9.work_position = work_position
                    wd9.work_date_started = work_date_started
                    wd9.work_date_ended = work_date_ended
                    wd9.reason_for_leaving = reason_for_leaving

                    prev_company_entry.delete(0, "end")
                    work_position_entry.delete(0, "end")
                    work_date_started_entry.delete(0, "end")
                    work_date_ended_entry.delete(0, "end")
                    reason_for_leaving_entry.delete(0, "end")
                
                # elif wd1.cur_work_exp == 10:
                #     wd10.prev_company = prev_company
                #     wd10.work_position = work_position
                #     wd10.work_date_started = work_date_started
                #     wd10.work_date_ended = work_date_ended
                #     wd10.reason_for_leaving = reason_for_leaving

                #     prev_company_entry.delete(0, "end")
                #     work_position_entry.delete(0, "end")
                #     work_date_started_entry.delete(0, "end")
                #     work_date_ended_entry.delete(0, "end")
                #     reason_for_leaving_entry.delete(0, "end")
                
                # Increment the counter only if the data is successfully added
                wd1.cur_work_exp += 1

                    # Reset the entry boxes and education_attainment_var
        else:
            # Do nothing, the user clicked 'no'
            pass


def work_experience_main(parent):
    # Global variables
    global prev_company_entry
    global work_position_entry
    global work_date_started_entry
    global work_date_ended_entry
    global reason_for_leaving_entry
    global d_prev_company_entry
    global d_work_position_entry
    global d_reason_for_leaving

    d_prev_company_entry = "Enter Previous Employer/Company"
    d_work_position_entry = "Enter Work Position"
    d_reason_for_leaving = "Enter Reason"

    # --------------------------------------------------------------------------------#
    # ---------------------------------- GUI SETUP ---------------------------------- #
    # --------------------------------------------------------------------------------#

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
        256.0,
        211.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        203.0,
        297.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        206.0,
        383.0,
        image=image_image_9
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets("image_10.png"))
    image_10 = canvas.create_image(
        557.0,
        211.0,
        image=image_image_10
    )

    image_image_11 = PhotoImage(
        file=relative_to_assets("image_11.png"))
    image_11 = canvas.create_image(
        568.0,
        297.0,
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
        691.0,
        241.0,
        image=entry_image_1
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        691.0,
        327.0,
        image=entry_image_2
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        322.0,
        241.0,
        image=entry_image_3
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        322.0,
        327.0,
        image=entry_image_4
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        322.0,
        413.0,
        image=entry_image_5
    )

    # --------------------------------------------------------------------------------#
    # --------------------------------- ENTRY SETUP --------------------------------- #
    # --------------------------------------------------------------------------------#

    prev_company_entry = DefaultTextEntry(
        default_text=d_prev_company_entry,
        bd=0,
        font=fontstyle,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    prev_company_entry.place(
        x=154.0,
        y=221.0,
        width=336.0,
        height=38.0
    )

    work_position_entry = DefaultTextEntry(
        default_text=d_work_position_entry,
        bd=0,
        font=fontstyle,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    work_position_entry.place(
        x=523.0,
        y=221.0,
        width=336.0,
        height=38.0
    )

    work_date_started_entry = DateEntry(
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
        firstweekday="sunday"
    )
    work_date_started_entry.place(
        x=154.0,
        y=308.0,
        width=336.0,
        height=38.0
    )
    
    work_date_ended_entry = DateEntry(
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
        firstweekday="sunday"
    )
    work_date_ended_entry.place(
        x=523.0,
        y=308.0,
        width=336.0,
        height=38.0
    )

    reason_for_leaving_entry = DefaultTextEntry(
        default_text=d_reason_for_leaving,
        bd=0,
        font=fontstyle,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    reason_for_leaving_entry.place(
        x=154.0,
        y=393.0,
        width=336.0,
        height=38.0
    )

    # --------------------------------------------------------------------------------#
    # ----------------------------------- BUTTONS ----------------------------------- #
    # --------------------------------------------------------------------------------#
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#ccd4d9",
        cursor='hand2',
        command=lambda:next_clicked(parent),
        relief="flat"
    )
    button_1.place(
        x=694.0,
        y=509.0,
        width=178.0,
        height=33.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#ccd4d9",
        cursor='hand2',
        command=add_more_clicked,
        relief="flat"
    )
    button_2.place(
        x=379.0,
        y=455.0,
        width=266.0,
        height=33.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#ccd4d9",
        cursor='hand2',
        command=lambda: back_clicked(parent),
        relief="flat"
    )
    button_3.place(
        x=151.0,
        y=509.0,
        width=178.0,
        height=33.0
    )
    
    display_values()
    parent.mainloop()