#This is a Kent School Schedule App that allows students to enter their class schedule and then view their schedule for a given day of the week and letter day.
#Made by: Jacob Barkin, 2024
#Production version 1.0
#Development Version 1.2
#Last updated: 08/30/2024

import json
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Define the file path for the JSON file
home_dir = os.path.expanduser("~")
app_dir = os.path.join(home_dir, "KentScheduleApp")
os.makedirs(app_dir, exist_ok=True)
file_path = os.path.join(app_dir, 'class_schedule.json')

def save_schedule(schedule):
    try:
        with open(file_path, 'w') as file:
            json.dump(schedule, file)
    except IOError as e:
        messagebox.showerror("Error", f"Failed to save schedule: {e}")
        return False
    return True

def save_input():
    schedule = {
        'p0': entry_p0.get(),
        'p1': entry_p1.get(),
        'p2': entry_p2.get(),
        'p3': entry_p3.get(),
        'p4': entry_p4.get(),
        'p5': entry_p5.get(),
        'p6': entry_p6.get()
    }
    if save_schedule(schedule):
        messagebox.showinfo("Info", "Schedule saved successfully!")
        print(f"The file path is: {os.path.abspath(file_path)}")
        input_window.destroy()
        display_main_window()
    else:
        messagebox.showerror("Error", "Failed to save schedule.")

font_type = ("Helvetica", 14)

def display_schedule():
    letter_day_int = letter_day_combobox.get().upper()
    week_day = week_day_combobox.get().capitalize()

    if letter_day_int not in letter_days:
        messagebox.showerror("Error", "Invalid letter day")
        return

    if week_day not in schedules:
        messagebox.showerror("Error", "Invalid day of the week")
        return

    letter_day = letter_days[letter_day_int]
    schedule_text = schedules[week_day].format(*letter_day)
    schedule_label.config(text=schedule_text)
    
    # Destroy the comboboxes and button
    destroy_widgets([letter_day_combobox, week_day_combobox, display_button])
    main_window.geometry("200x350")

def destroy_widgets(widgets):
    for widget in widgets:
        widget.destroy()

def reset_schedule():
    if os.path.exists(file_path):
        os.remove(file_path)
    main_window.destroy()
    display_input_window()

def display_main_window():
    global letter_day_combobox, week_day_combobox, display_button, schedule_label, main_window

    main_window = tk.Tk()
    main_window.title("Class Schedule")
    window_width = 400
    window_height = 300

    # Get the screen width and height
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()

    # Calculate the position to center the window
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    # Set the geometry of the window
    main_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    style = ttk.Style()
    style.configure('TLabel', font=('Helvetica', 12))
    style.configure('TButton', font=('Helvetica', 12))
    style.configure('TCombobox', font=('Helvetica', 12))

    ttk.Label(main_window, text="Letter Day:", style='TLabel').grid(row=0, column=0, padx=10, pady=10)
    letter_day_combobox = ttk.Combobox(main_window, values=["A", "B", "C", "D", "E", "F", "G"], style='TCombobox')
    letter_day_combobox.grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(main_window, text="Day of the Week:", style='TLabel').grid(row=1, column=0, padx=10, pady=10)
    week_day_combobox = ttk.Combobox(main_window, values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], style='TCombobox')
    week_day_combobox.grid(row=1, column=1, padx=10, pady=10)

    display_button = ttk.Button(main_window, text="Display Schedule", command=display_schedule, style='TButton')
    display_button.grid(row=2, column=0, columnspan=2, pady=20, sticky='ew')

    schedule_label = ttk.Label(main_window, text="", style='TLabel')
    schedule_label.grid(row=3, column=0, columnspan=2, pady=10)

    reset_button = ttk.Button(main_window, text="Reset Schedule", command=reset_schedule, style='TButton')
    reset_button.grid(row=4, column=0, columnspan=2, pady=10, sticky='ew')

    main_window.mainloop()

    main_window.mainloop()

def display_input_window():
    global entry_p0, entry_p1, entry_p2, entry_p3, entry_p4, entry_p5, entry_p6, input_window

    input_window = tk.Tk()
    input_window.title("Enter Class Schedule")
    window_width = 400
    window_height = 400

    # Get the screen width and height
    screen_width = input_window.winfo_screenwidth()
    screen_height = input_window.winfo_screenheight()

    # Calculate the position to center the window
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    # Set the geometry of the window
    input_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    style = ttk.Style()
    style.configure('TLabel', font=('Helvetica', 12))
    style.configure('TButton', font=('Helvetica', 12))
    style.configure('TEntry', font=('Helvetica', 12))

    # Add a title and instructions
    ttk.Label(input_window, text="Enter Your Class Schedule", font=('Helvetica', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
    ttk.Label(input_window, text="Please enter your classes for each period:", font=('Helvetica', 12)).grid(row=1, column=0, columnspan=2, pady=5)

    periods = ["Period 0:", "Period 1:", "Period 2:", "Period 3:", "Period 4:", "Period 5:", "Period 6:"]
    entries = []

    for i, period in enumerate(periods):
        ttk.Label(input_window, text=period, style='TLabel').grid(row=i+2, column=0, padx=10, pady=5, sticky='e')
        entry = ttk.Entry(input_window, style='TEntry')
        entry.grid(row=i+2, column=1, padx=10, pady=5)
        entries.append(entry)

    entry_p0, entry_p1, entry_p2, entry_p3, entry_p4, entry_p5, entry_p6 = entries

    ttk.Button(input_window, text="Save Schedule", command=save_input, style='TButton').grid(row=9, column=0, columnspan=2, pady=20)

    input_window.mainloop()

# Check if the JSON file exists
if os.path.exists(file_path):
    # Load the class schedule from the file
    with open(file_path, 'r') as file:
        schedule = json.load(file)
    p0 = schedule['p0']
    p1 = schedule['p1']
    p2 = schedule['p2']
    p3 = schedule['p3']
    p4 = schedule['p4']
    p5 = schedule['p5']
    p6 = schedule['p6']

    # Define the letter days
    letter_days = {
        "A": (p0, p1, p3, p4, p5),
        "B": (p1, p2, p4, p5, p6),
        "C": (p2, p3, p5, p6, p0),
        "D": (p3, p1, p6, p0, p4),
        "E": (p1, p2, p0, p4, p5),
        "F": (p2, p3, p1, p5, p6),
        "G": (p3, p0, p2, p6, p4)
    }

    schedules = {
        "Monday": "8:30-9:30: {}\n9:35-10:00: Assembly\n10:05-11:05: {}\n11:10-12:10: {}\n12:15-1:00: Lunch\n1:05-2:05: {}\n2:10-2:30: Office Hours\n2:35-3:35: {}",
        "Tuesday": "8:30-9:30: {}\n9:35-10:00: Advisory\n10:05-11:05: {}\n11:10-12:10: {}\n12:15-1:00: Lunch\n1:05-2:05: {}\n2:10-3:10: {}\n3:15-4:15: Clubs",
        "Wednesday": "9:00-10:00: {}\n10:05-11:05: {}\n11:10-12:10: {}\n12:15-1:00: Lunch\n1:05-2:05: {}\n2:10-2:30: Office Hours\n2:35-3:35: {}",
        "Thursday": "8:30-9:30: {}\n9:35-10:00: Other\n10:05-11:05: {}\n11:10-12:10: {}\n12:15-1:00: Lunch\n1:05-2:05: {}\n2:10-3:10: {}\n3:15-3:45: Office Hours",
        "Friday": "8:30-9:30: {}\n9:35-10:00: Class Meeting\n10:05-11:05: {}\n11:10-12:10: {}\n12:15-1:00: Lunch\n1:05-2:05: {}\n2:10-2:30: Clubs\n2:35-3:35: {}"
    }

    display_main_window()
else:
    display_input_window()

print("Program finished")