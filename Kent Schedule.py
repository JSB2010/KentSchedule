import json
import os

# Define the file path for the JSON file
file_path = 'class_schedule.json'

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
else:
    # Prompt the user for input and save it to the JSON file
    p0 = input("Enter your Period 0 class: ")
    p1 = input("Enter your Period 1 class: ")
    p2 = input("Enter your Period 2 class: ")
    p3 = input("Enter your Period 3 class: ")
    p4 = input("Enter your Period 4 class: ")
    p5 = input("Enter your Period 5 class: ")
    p6 = input("Enter your Period 6 class: ")

    schedule = {
        'p0': p0,
        'p1': p1,
        'p2': p2,
        'p3': p3,
        'p4': p4,
        'p5': p5,
        'p6': p6
    }

    with open(file_path, 'w') as file:
        json.dump(schedule, file)

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

letter_day_int = input("Enter the letter day: ").upper()

if letter_day_int in letter_days:
    letter_day = letter_days[letter_day_int]
else:
    print("Invalid letter day")
    letter_day = None

if letter_day:
    schedules = {
        "Monday": f"8:30-9:30: {letter_day[0]}\n9:35-10:00: Assembly\n10:05-11:05: {letter_day[1]}\n11:10-12:10: {letter_day[2]}\n12:15-1:00: Lunch\n1:05-2:05: {letter_day[3]}\n2:10-2:30: Office Hours\n2:35-3:35: {letter_day[4]}",
        "Tuesday": f"8:30-9:30: {letter_day[0]}\n9:35-10:00: Advisory\n10:05-11:05: {letter_day[1]}\n11:10-12:10: {letter_day[2]}\n12:15-1:00: Lunch\n1:05-2:05: {letter_day[3]}\n2:10-3:10: {letter_day[4]}\n3:15-4:15: Clubs",
        "Wednesday": f"9:00-10:00: {letter_day[0]}\n10:05-11:05: {letter_day[1]}\n11:10-12:10: {letter_day[2]}\n12:15-1:00: Lunch\n1:05-2:05: {letter_day[3]}\n2:10-2:30: Office Hours\n2:35-3:35: {letter_day[4]}",
        "Thursday": f"8:30-9:30: {letter_day[0]}\n9:35-10:00: Other\n10:05-11:05: {letter_day[1]}\n11:10-12:10: {letter_day[2]}\n12:15-1:00: Lunch\n1:05-2:05: {letter_day[3]}\n2:10-3:10: {letter_day[4]}\n3:15-3:45: Office Hours",
        "Friday": f"8:30-9:30: {letter_day[0]}\n9:35-10:00: Class Meeting\n10:05-11:05: {letter_day[1]}\n11:10-12:10: {letter_day[2]}\n12:15-1:00: Lunch\n1:05-2:05: {letter_day[3]}\n2:10-2:30: Clubs\n2:35-3:35: {letter_day[4]}"
    }

    week_day = input("Enter the day of the week: ").capitalize()

    if week_day in schedules:
        print(schedules[week_day])
    else:
        print("Invalid day of the week")
else:
    print("Please restart the program and enter a valid letter day.")