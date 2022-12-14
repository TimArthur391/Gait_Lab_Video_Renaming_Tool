# Main Script of the:
#
# Gait_Lab_Video_Renaming_Tool

print(
    """
---------------------------------------------------------
--------------------------HELLO--------------------------
---------------------------------------------------------
-------------THE INTERFACE IS JUST LOADING---------------
---------------------------------------------------------
---PLEASE REPORT ANY ISSUES TO TIMOTHY.ARTHUR1@NHS.NET---
---------------------------------------------------------
"""
)

import tkinter
import tkinter.filedialog as tkk
tk = tkinter
from scrpt.tkvideo_tim import tkvideo
import os
import sys
from shutil import copyfile
from datetime import datetime
import scrpt.database_connection as db
import scrpt.renaming_tools as rt
import json

def main() -> None:
    root.mainloop()

def change_button_relief_on_click(button_name):
    current_relief = button_names[button_name][0].config('relief')[-1]
    if current_relief == 'sunken':
        button_names[button_name][0].config(relief="raised", bg='#222b35')
    elif current_relief == 'raised':
        buttons_to_raise = rt.get_button_names(button_name)
        button_names[button_name][0].config(relief="sunken", bg='#FF5733')
        for button in buttons_to_raise:
            button_names[button][0].config(relief="raised", bg='#222b35')
    else:
        print('Something has gone wrong')
    
def format_name():
    video_name_box.delete(0, tk.END)
    filename = ''
    error_list = []
    orthotic = str(orthotic_box.get())
    if not orthotic:
        print('You have not entered an orthotic device')
    else:
        filename += orthotic.strip()

    for button in button_names.keys():
        if button_names[button][0].config('relief')[-1] == 'sunken':
            filename += ' ' + button_names[button][1]

    #VICON NUMBER
    vicon_number = str(vicon_number_box.get())
    if not vicon_number:
        print('You have not entered a Vicon number')
    else:
        filename += ' ' + vicon_number.strip()

    #TRIAL NUMBER
    trial_number = str(trial_number_box.get())
    if not trial_number:
        print('You have not entered a trial number')
    else:
        filename += trial_number.strip()

    #HOSPITAL NUMBER
    hospital_number = str(hospital_number_box.get())
    if not hospital_number:
        print('You have not entered a hospital number')
    else:
        filename += ' ' + hospital_number.strip()

    #DATE
    film_date = str(date_box.get())
    if not film_date:
        print('You have not entered a date')
    else:
        filename += ' ' + film_date.strip()

    if filename != '':
        video_name_box.insert(0, filename)
        next_button.config(state=tk.ACTIVE, relief="raised")
    else:
        video_name_box.insert(0, filename)
        next_button.config(state=tk.DISABLED)
    
def open_files():
    global selected_video
    global video_names
    global video_locations
    
    filenames_box.delete(0, tk.END)

    root.filename = tkk.askopenfilenames(initialdir="C:", title="Select files", filetypes=[
        ("all video format", ".avi"),
        ("all video format", ".mp4")
        ]) #gives the entire file location
    
    selected_video = 0
    video_names = rt.get_video_names(root.filename)
    video_locations = rt.get_video_file_directories(root.filename)
    
    filenames_box.insert(0, ' '.join(video_names))
  
    if video_names:
        global trial_numbers
        
        trial_numbers = rt.get_trial_numbers(root.filename)
        video_date = rt.get_session_datetime(root.filename)
        vicon_number = rt.get_vicon_number(root.filename)

        vicon_number_box.delete(0, tk.END)
        vicon_number_box.insert(0, vicon_number)
        date_box.delete(0, tk.END)
        date_box.insert(0, video_date)            

        my_label.grid_forget()
        for button in button_names.keys():
            button_names[button][0].config(state=tk.ACTIVE)

        next()

def next():
    global selected_video
    global my_label
    global old_time
    global new_time

    if selected_video == 0:
        old_time = datetime.now()
        if trial_numbers:
            trial_number_box.delete(0, tk.END)
            trial_number_box.insert(0, trial_numbers[selected_video])

        my_label.grid_forget()
        my_label = tk.Label(root)
        my_label.grid(row = 0, column = 0, rowspan = 11, sticky = tk.W, padx=(4,4))
        path = os.path.join(os.path.dirname(sys.executable), video_locations[selected_video])
        player = tkvideo(path, my_label, loop = 0)
        player.play()
    elif selected_video >= len(video_locations):
        new_time=datetime.now()
        my_label.grid_forget()
        video_name_final = str(video_name_box.get()) + '.AVI'


        directory = os.path.dirname(video_locations[selected_video-1])
        old_file = os.path.join(directory, video_names[selected_video-1])
        new_file = os.path.join(directory, video_name_final)
        copyfile(old_file, new_file)
        
        time_diff = new_time - old_time
        duration = round(time_diff.total_seconds(),2)
        username=os.getlogin()
        dAte=datetime.now().strftime("%Y-%m-%d")
        tIme=datetime.now().strftime("%H:%M:%S")
        print(username, dAte, tIme, video_names[selected_video-1], video_name_final, duration)

        SQL_statement = ("INSERT INTO usage_log (USERNAME, DATE, TIME, FILENAME0, FILENAME1, DURATION) VALUES (%s, %s, %s, %s, %s, %s)")
        data = (username, dAte, tIme, video_names[selected_video-1], video_name_final, duration)
        database_name = 'videorenamer'
        db.post_request(SQL_statement, data, database_name)
        
        next_button.config(state=tk.DISABLED)
        skip_button.config(state=tk.DISABLED)
        replay_button.config(state=tk.DISABLED)
        print(
"""
---------------------------------------------------------
--YOU HAVE NOW RENAMED ALL THE VIDEOS THAT YOU SELECTED--
---------------------------------------------------------
---YOU CAN CLOSE THIS PROGRAM OR SELECT MORE VIDEOS TO---
-------------------------RENAME--------------------------
---------------------------------------------------------
"""
        )
    else:
        new_time = datetime.now()
        my_label.grid_forget()
        video_name_final = str(video_name_box.get()) + '.AVI'

        if trial_numbers:
            trial_number_box.delete(0, tk.END)
            trial_number_box.insert(0, trial_numbers[selected_video])

        directory = os.path.dirname(video_locations[selected_video-1])
        old_file = os.path.join(directory, video_names[selected_video-1])
        new_file = os.path.join(directory, video_name_final)
        copyfile(old_file, new_file)
        
        time_diff = new_time - old_time
        duration = round(time_diff.total_seconds(),2)
        username=os.getlogin()
        dAte=datetime.now().strftime("%Y-%m-%d")
        tIme=datetime.now().strftime("%H:%M:%S")
        print(username, dAte, tIme, video_names[selected_video-1], video_name_final, duration)

        SQL_statement = ("INSERT INTO usage_log (USERNAME, DATE, TIME, FILENAME0, FILENAME1, DURATION) VALUES (%s, %s, %s, %s, %s, %s)")
        data = (username, dAte, tIme, video_names[selected_video-1], video_name_final, duration)
        database_name = 'videorenamer'
        db.post_request(SQL_statement, data, database_name)
        
        old_time = datetime.now()

        my_label = tk.Label(root)
        my_label.grid(row = 0, column = 0, rowspan = 11, sticky = tk.W, padx=(4,4))
        path = os.path.join(os.path.dirname(sys.executable), video_locations[selected_video])
        player = tkvideo(path, my_label, loop = 0)
        player.play()

    selected_video += 1
    next_button.config(state=tk.DISABLED, relief="raised")

def skip():
    global selected_video
    global my_label
    global old_time

    if selected_video >= len(video_locations):

        my_label.grid_forget()
        next_button.config(state=tk.DISABLED)
        skip_button.config(state=tk.DISABLED)
        replay_button.config(state=tk.DISABLED)
        print(
"""
---------------------------------------------------------
--YOU HAVE NOW RENAMED ALL THE VIDEOS THAT YOU SELECTED--
---------------------------------------------------------
---YOU CAN CLOSE THIS PROGRAM OR SELECT MORE VIDEOS TO---
-------------------------RENAME--------------------------
---------------------------------------------------------
"""
        )
    else:
        my_label.grid_forget()

        if trial_numbers:
            trial_number_box.delete(0, tk.END)
            trial_number_box.insert(0, trial_numbers[selected_video])   

        my_label = tk.Label(root)
        my_label.grid(row = 0, column = 0, rowspan = 11, sticky = tk.W, padx=(4,4))
        path = os.path.join(os.path.dirname(sys.executable), video_locations[selected_video])
        player = tkvideo(path, my_label, loop = 0)
        player.play()
        old_time = datetime.now()

    selected_video += 1
    next_button.config(state=tk.DISABLED, relief="raised")

def replay():
    global selected_video
    global my_label
    selected_video -= 1
    my_label.grid_forget()
    my_label = tk.Label(root)
    my_label.grid(row = 0, column = 0, rowspan = 11, sticky = tk.W, padx=(4,4))
    path = os.path.join(os.path.dirname(sys.executable), video_locations[selected_video])
    player = tkvideo(path, my_label, loop = 0)
    player.play()
    selected_video += 1

def get_info_from_application_JSON_file():
    with open("helpers\\application_information.JSON", "r") as read_file:
        application_information = json.load(read_file)

    return application_information

def get_application_title_string():
    application_information = get_info_from_application_JSON_file()
    application_version = application_information["applicationVersion"]
    application_name = application_information["applicationName"]
    application_title = application_name.replace('_', ' ') + ' ' + str(application_version)
    
    return application_title

#Initialise tkinter
root = tk.Tk()
root.title(get_application_title_string())
root.configure(background='#19232d')
root.iconbitmap('helpers\\Camcorder_Pro_icon-icons.com_54204.ico')

#Create and use a grid to organise the tkinter widgets
my_label = tk.Label(root)
my_label.grid(row = 0, column = 0, rowspan = 11, sticky = tk.W, padx=(4,4))

#Create the instances of each tkinter widget
#   Labels
orthotic_box_label = tk.Label(root,        text="Condition:", bg='#19232d', fg="#ffffff", font=18)
filenames_box_label = tk.Label(root,       text="Videos:", bg='#19232d', fg="#ffffff", font=18)
hospital_number_box_label = tk.Label(root, text="Hosp no:", bg='#19232d', fg="#ffffff", font=18)
vicon_number_box_label = tk.Label(root,    text="Vicon no:", bg='#19232d', fg="#ffffff", font=18)
date_box_label = tk.Label(root,            text="Date:", bg='#19232d', fg="#ffffff", font=18)
trial_number_box_label = tk.Label(root,    text="Trial no:", bg='#19232d', fg="#ffffff", font=18)

#   Buttons
sagittal_button = tk.Button(root,    text="Sag",         command=lambda:[change_button_relief_on_click("sagittal"), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=tk.DISABLED)
left_button = tk.Button(root,        text="L",           command=lambda:[change_button_relief_on_click("left"), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=tk.DISABLED)
right_button = tk.Button(root,       text="R",           command=lambda:[change_button_relief_on_click("right"), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=tk.DISABLED)
leftSide_button = tk.Button(root,    text="Left side",   command=lambda:[change_button_relief_on_click("left_side"), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=tk.DISABLED)
rightSide_button = tk.Button(root,   text="Right side",  command=lambda:[change_button_relief_on_click("right_side"), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=tk.DISABLED)
coronal_button = tk.Button(root,     text="Cor",         command=lambda:[change_button_relief_on_click("coronal"), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=tk.DISABLED)
towards_button = tk.Button(root,     text="Twrds",       command=lambda:[change_button_relief_on_click("towards"), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=tk.DISABLED)
away_button = tk.Button(root,        text="Away",        command=lambda:[change_button_relief_on_click("away"), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=tk.DISABLED)
feet_button = tk.Button(root,        text="Feet",        command=lambda:[change_button_relief_on_click("feet"), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=tk.DISABLED)
standing_button = tk.Button(root,    text="Stand",       command=lambda:[change_button_relief_on_click("stand"), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=tk.DISABLED)
lat_L_med_R_button = tk.Button(root, text="Lat L Med R", command=lambda:[change_button_relief_on_click("lat_l_med_r"), format_name()], bg='#222b35', fg="#ffffff", width=13, font=18, relief="raised", state=tk.DISABLED)
lat_R_med_L_button = tk.Button(root, text="Lat R Med L", command=lambda:[change_button_relief_on_click("lat_r_med_l"), format_name()], bg='#222b35', fg="#ffffff", width=13, font=18, relief="raised", state=tk.DISABLED)
overhead_button = tk.Button(root,    text="Overhead",    command=lambda:[change_button_relief_on_click("overhead"), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=tk.DISABLED)
oppL_button = tk.Button(root,        text="Opp L",       command=lambda:[change_button_relief_on_click("opp_left"), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=tk.DISABLED)
oppR_button = tk.Button(root,        text="Opp R",       command=lambda:[change_button_relief_on_click("opp_right"), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=tk.DISABLED)
ICMS_button = tk.Button(root,        text="IC-MS",       command=lambda:[change_button_relief_on_click("icms"), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=tk.DISABLED)
MSES_button = tk.Button(root,        text="MS-ES",       command=lambda:[change_button_relief_on_click("mses"), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=tk.DISABLED)
next_button = tk.Button(root,        text="Next video",  command=next, bg='#222b35', fg="#ffffff", font=18, relief="raised", width=25, state=tk.DISABLED)
skip_button = tk.Button(root,        text="Skip",        command=skip, bg='#222b35', fg="#ffffff", font=18, relief="raised", width=8, state=tk.DISABLED)
replay_button = tk.Button(root,      text="Replay",      command=replay, bg='#222b35', fg="#ffffff", font=18, relief="raised", width=8, state=tk.DISABLED)
file_open_button = tk.Button(root,   text="Browse",      command=open_files, bg='#222b35', fg="#ffffff", font=18, width=8)
button_names = {
        "stand": [standing_button, "Stand"], "feet": [feet_button, "Feet"], "overhead": [overhead_button, "Overhead"],
        "coronal": [coronal_button, "Cor"], "towards": [towards_button, "Twrds"], "away": [away_button, "Away"],
        "sagittal": [sagittal_button, "Sag"], "left": [left_button, "L"], "right": [right_button, "R"],  
        "left_side": [leftSide_button, "L side"], "right_side": [rightSide_button, "R side"], 
        "icms": [ICMS_button, "IC-MS"], "mses": [MSES_button, "MS-ES"], "opp_left": [oppL_button, "Opp L"], "opp_right": [oppR_button, "Opp R"],
        "lat_l_med_r": [lat_L_med_R_button, "Lat L Med R"], "lat_r_med_l": [lat_R_med_L_button, "Lat R Med L"], "skip": [skip_button, ""], "replay": [replay_button, ""]   
    }

#   Entry text boxes
video_name_box = tk.Entry(     root, width=50, bg='#222b35', fg="#ffffff", font=10, insertbackground="#ffffff")
orthotic_box = tk.Entry(       root, width=35, bg='#222b35', fg="#ffffff", font=10, insertbackground="#ffffff")
filenames_box = tk.Entry(      root, width=25, bg='#222b35', fg="#ffffff", font=10, insertbackground="#ffffff")
hospital_number_box = tk.Entry(root, width=8,  bg='#222b35', fg="#ffffff", font=10, insertbackground="#ffffff")
date_box = tk.Entry(           root, width=8,  bg='#222b35', fg="#ffffff", font=10, insertbackground="#ffffff")
vicon_number_box = tk.Entry(   root, width=8,  bg='#222b35', fg="#ffffff", font=10, insertbackground="#ffffff")
trial_number_box = tk.Entry(   root, width=8,  bg='#222b35', fg="#ffffff", font=10, insertbackground="#ffffff")

#Placing the widgets onto the GUI ('my_label') grid
#   Opening files label, entry box and button positions
filenames_box_label.grid(row=0, column=1, pady=(2,2))
filenames_box.grid(      row=0, column=2, columnspan = 3, pady=(2,2))
file_open_button.grid(   row=0, column=5, pady=(2,8))
#   Entry box and Label positions
hospital_number_box_label.grid(row=1, column=1, pady=(8,2))
hospital_number_box.grid(      row=1, column=2, pady=(8,2))
vicon_number_box_label.grid(   row=1, column=4, pady=(8,2))
vicon_number_box.grid(         row=1, column=5, pady=(8,2))
date_box_label.grid(           row=2, column=1, pady=(2,16))
date_box.grid(                 row=2, column=2, pady=(2,16))
trial_number_box_label.grid(   row=2, column=4, pady=(2,16))
trial_number_box.grid(         row=2, column=5, pady=(2,16))
orthotic_box_label.grid(       row=4, column=1, pady=(16,4))
orthotic_box.grid(             row=4, column=2, columnspan = 4, pady=(16,4))
#   Button positions
sagittal_button.grid(   row=5, column=1, pady=(6,6))
coronal_button.grid(    row=5, column=2, pady=(6,6))
feet_button.grid(       row=5, column=5, pady=(6,6))
standing_button.grid(   row=5, column=4, pady=(6,6))
overhead_button.grid(   row=5, column=3, pady=(6,6))
left_button.grid(       row=7, column=1, pady=(2,6))
right_button.grid(      row=6, column=1, pady=(6,2))
oppL_button.grid(       row=7, column=2, pady=(2,6))
oppR_button.grid(       row=6, column=2, pady=(6,2))
leftSide_button.grid(   row=7, column=3, pady=(2,6))
rightSide_button.grid(  row=6, column=3, pady=(6,2))
towards_button.grid(    row=7, column=4, pady=(2,6))
away_button.grid(       row=6, column=4, pady=(6,2))
ICMS_button.grid(       row=7, column=5, pady=(2,6))
MSES_button.grid(       row=6, column=5, pady=(6,2))
lat_L_med_R_button.grid(row=8, column=1, columnspan = 3, pady=(6,6))
lat_R_med_L_button.grid(row=8, column=3, columnspan = 3, pady=(6,6))
#   video name and skip, next and replay button positions
video_name_box.grid(row=9,  column=1, columnspan=5, pady=(6,2))
next_button.grid(   row=10, column=2, columnspan=3, pady=(2,2))
skip_button.grid(   row=10, column=5, pady=(2,2))
replay_button.grid( row=10, column=1, pady=(2,2))

if __name__ == "__main__":
    main()