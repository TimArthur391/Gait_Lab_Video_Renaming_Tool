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


from tkinter import *
from tkinter import filedialog
from scrpt.tkvideo_tim import tkvideo
import os
import sys
from os import path
from shutil import copyfile
from datetime import datetime
from scrpt.db_connection import connect_to_database

def main() -> None:
    root.mainloop()

root = Tk()
root.title("Gait Lab Video Renaming Tool v1.3")
root.configure(background='#19232d')


def left_rename():
    if left_button.config('relief')[-1] == 'sunken':
        left_button.config(relief="raised", bg='#222b35')
    else:
        left_button.config(relief="sunken", bg='#FF5733')
        right_button.config(relief="raised", bg='#222b35')
        oppL_button.config(relief="raised", bg='#222b35')
        #oppR_button.config(relief="raised", bg='#222b35')
        rightSide_button.config(relief="raised", bg='#222b35')
        leftSide_button.config(relief="raised", bg='#222b35')
        #towards_button.config(relief="raised", bg='#222b35')
        #away_button.config(relief="raised", bg='#222b35')
        ICMS_button.config(relief="raised", bg='#222b35')
        MSES_button.config(relief="raised", bg='#222b35')
        lat_R_med_L_button.config(relief="raised", bg='#222b35')
        lat_L_med_R_button.config(relief="raised", bg='#222b35')

def right_rename():
    if right_button.config('relief')[-1] == 'sunken':
        right_button.config(relief="raised", bg='#222b35')
    else:
        right_button.config(relief="sunken", bg='#FF5733')
        left_button.config(relief="raised", bg='#222b35')
        #oppL_button.config(relief="raised", bg='#222b35')
        oppR_button.config(relief="raised", bg='#222b35')
        rightSide_button.config(relief="raised", bg='#222b35')
        leftSide_button.config(relief="raised", bg='#222b35')
        #towards_button.config(relief="raised", bg='#222b35')
        #away_button.config(relief="raised", bg='#222b35')
        ICMS_button.config(relief="raised", bg='#222b35')
        MSES_button.config(relief="raised", bg='#222b35')
        lat_R_med_L_button.config(relief="raised", bg='#222b35')
        lat_L_med_R_button.config(relief="raised", bg='#222b35')

def sagittal_rename():
    if sagittal_button.config('relief')[-1] == 'sunken':
        sagittal_button.config(relief="raised", bg='#222b35')
    else:
        sagittal_button.config(relief="sunken", bg='#FF5733')
        overhead_button.config(relief="raised", bg='#222b35')
        coronal_button.config(relief="raised", bg='#222b35')

def leftSide_rename():
    if leftSide_button.config('relief')[-1] == 'sunken':
        leftSide_button.config(relief="raised", bg='#222b35')
    else:
        leftSide_button.config(relief="sunken", bg='#FF5733')
        rightSide_button.config(relief="raised", bg='#222b35')
        oppL_button.config(relief="raised", bg='#222b35')
        #oppR_button.config(relief="raised", bg='#222b35')
        left_button.config(relief="raised", bg='#222b35')
        right_button.config(relief="raised", bg='#222b35')
        #towards_button.config(relief="raised", bg='#222b35')
        #away_button.config(relief="raised", bg='#222b35')
        ICMS_button.config(relief="raised", bg='#222b35')
        MSES_button.config(relief="raised", bg='#222b35')
        lat_R_med_L_button.config(relief="raised", bg='#222b35')
        lat_L_med_R_button.config(relief="raised", bg='#222b35')

def rightSide_rename():
    if rightSide_button.config('relief')[-1] == 'sunken':
        rightSide_button.config(relief="raised", bg='#222b35')
    else:
        rightSide_button.config(relief="sunken", bg='#FF5733')
        leftSide_button.config(relief="raised", bg='#222b35')
        #oppL_button.config(relief="raised", bg='#222b35')
        oppR_button.config(relief="raised", bg='#222b35')
        left_button.config(relief="raised", bg='#222b35')
        right_button.config(relief="raised", bg='#222b35')
        #towards_button.config(relief="raised", bg='#222b35')
        #away_button.config(relief="raised", bg='#222b35')
        ICMS_button.config(relief="raised", bg='#222b35')
        MSES_button.config(relief="raised", bg='#222b35')
        lat_R_med_L_button.config(relief="raised", bg='#222b35')
        lat_L_med_R_button.config(relief="raised", bg='#222b35')

def towards_rename():
    if towards_button.config('relief')[-1] == 'sunken':
        towards_button.config(relief="raised", bg='#222b35')
    else:
        towards_button.config(relief="sunken", bg='#FF5733')
        away_button.config(relief="raised", bg='#222b35')
        #oppL_button.config(relief="raised", bg='#222b35')
        #oppR_button.config(relief="raised", bg='#222b35')
        #left_button.config(relief="raised", bg='#222b35')
        #right_button.config(relief="raised", bg='#222b35')
        #rightSide_button.config(relief="raised", bg='#222b35')
        #leftSide_button.config(relief="raised", bg='#222b35')
        ICMS_button.config(relief="raised", bg='#222b35')
        MSES_button.config(relief="raised", bg='#222b35')
        lat_R_med_L_button.config(relief="raised", bg='#222b35')
        lat_L_med_R_button.config(relief="raised", bg='#222b35')

def away_rename():
    if away_button.config('relief')[-1] == 'sunken':
        away_button.config(relief="raised", bg='#222b35')
    else:
        away_button.config(relief="sunken", bg='#FF5733')
        towards_button.config(relief="raised", bg='#222b35')
        #oppL_button.config(relief="raised", bg='#222b35')
        #oppR_button.config(relief="raised", bg='#222b35')
        #left_button.config(relief="raised", bg='#222b35')
        #right_button.config(relief="raised", bg='#222b35')
        #rightSide_button.config(relief="raised", bg='#222b35')
        #leftSide_button.config(relief="raised", bg='#222b35')
        ICMS_button.config(relief="raised", bg='#222b35')
        MSES_button.config(relief="raised", bg='#222b35')
        lat_R_med_L_button.config(relief="raised", bg='#222b35')
        lat_L_med_R_button.config(relief="raised", bg='#222b35')

def coronal_rename():
    if coronal_button.config('relief')[-1] == 'sunken':
        coronal_button.config(relief="raised", bg='#222b35')
    else:
        coronal_button.config(relief="sunken", bg='#FF5733')
        overhead_button.config(relief="raised", bg='#222b35')
        sagittal_button.config(relief="raised", bg='#222b35')

def feet_rename():
    if feet_button.config('relief')[-1] == 'sunken':
        feet_button.config(relief="raised", bg='#222b35')
    else:
        feet_button.config(relief="sunken", bg='#FF5733')

def standing_rename():
    if standing_button.config('relief')[-1] == 'sunken':
        standing_button.config(relief="raised", bg='#222b35')
    else:
        standing_button.config(relief="sunken", bg='#FF5733')

def overhead_rename():
    if overhead_button.config('relief')[-1] == 'sunken':
        overhead_button.config(relief="raised", bg='#222b35')
    else:
        overhead_button.config(relief="sunken", bg='#FF5733')
        sagittal_button.config(relief="raised", bg='#222b35')
        coronal_button.config(relief="raised", bg='#222b35')

def MSES_rename():
    if MSES_button.config('relief')[-1] == 'sunken':
        MSES_button.config(relief="raised", bg='#222b35')
    else:
        MSES_button.config(relief="sunken", bg='#FF5733')
        #ICMS_button.config(relief="raised", bg='#222b35')
        oppL_button.config(relief="raised", bg='#222b35')
        oppR_button.config(relief="raised", bg='#222b35')
        #left_button.config(relief="raised", bg='#222b35')
        #right_button.config(relief="raised", bg='#222b35')
        #rightSide_button.config(relief="raised", bg='#222b35')
        #leftSide_button.config(relief="raised", bg='#222b35')
        #towards_button.config(relief="raised", bg='#222b35')
        #away_button.config(relief="raised", bg='#222b35')
        lat_R_med_L_button.config(relief="raised", bg='#222b35')
        lat_L_med_R_button.config(relief="raised", bg='#222b35')

def ICMS_rename():
    if ICMS_button.config('relief')[-1] == 'sunken':
        ICMS_button.config(relief="raised", bg='#222b35')
    else:
        ICMS_button.config(relief="sunken", bg='#FF5733')
        #MSES_button.config(relief="raised", bg='#222b35')
        oppL_button.config(relief="raised", bg='#222b35')
        oppR_button.config(relief="raised", bg='#222b35')
        #left_button.config(relief="raised", bg='#222b35')
        #right_button.config(relief="raised", bg='#222b35')
        #rightSide_button.config(relief="raised", bg='#222b35')
        #leftSide_button.config(relief="raised", bg='#222b35')
        #towards_button.config(relief="raised", bg='#222b35')
        #away_button.config(relief="raised", bg='#222b35')
        lat_R_med_L_button.config(relief="raised", bg='#222b35')
        lat_L_med_R_button.config(relief="raised", bg='#222b35')

def oppR_rename():
    if oppR_button.config('relief')[-1] == 'sunken':
        oppR_button.config(relief="raised", bg='#222b35')
    else:
        oppR_button.config(relief="sunken", bg='#FF5733')
        oppL_button.config(relief="raised", bg='#222b35')
        #MSES_button.config(relief="raised", bg='#222b35')
        #ICMS_button.config(relief="raised", bg='#222b35')
        #left_button.config(relief="raised", bg='#222b35')
        right_button.config(relief="raised", bg='#222b35')
        rightSide_button.config(relief="raised", bg='#222b35')
        #leftSide_button.config(relief="raised", bg='#222b35')
        #towards_button.config(relief="raised", bg='#222b35')
        #away_button.config(relief="raised", bg='#222b35')
        lat_R_med_L_button.config(relief="raised", bg='#222b35')
        lat_L_med_R_button.config(relief="raised", bg='#222b35')

def oppL_rename():
    if oppL_button.config('relief')[-1] == 'sunken':
        oppL_button.config(relief="raised", bg='#222b35')
    else:
        oppL_button.config(relief="sunken", bg='#FF5733')
        oppR_button.config(relief="raised", bg='#222b35')
        #MSES_button.config(relief="raised", bg='#222b35')
        #ICMS_button.config(relief="raised", bg='#222b35')
        left_button.config(relief="raised", bg='#222b35')
        #right_button.config(relief="raised", bg='#222b35')
        #rightSide_button.config(relief="raised", bg='#222b35')
        leftSide_button.config(relief="raised", bg='#222b35')
        #towards_button.config(relief="raised", bg='#222b35')
        #away_button.config(relief="raised", bg='#222b35')
        lat_R_med_L_button.config(relief="raised", bg='#222b35')
        lat_L_med_R_button.config(relief="raised", bg='#222b35')

def lat_L_med_R_rename():
    if lat_L_med_R_button.config('relief')[-1] == 'sunken':
        lat_L_med_R_button.config(relief="raised", bg='#222b35')
    else:
        lat_L_med_R_button.config(relief="sunken", bg='#FF5733')
        lat_R_med_L_button.config(relief="raised", bg='#222b35')
        oppL_button.config(relief="raised", bg='#222b35')
        oppR_button.config(relief="raised", bg='#222b35')
        MSES_button.config(relief="raised", bg='#222b35')
        ICMS_button.config(relief="raised", bg='#222b35')
        left_button.config(relief="raised", bg='#222b35')
        right_button.config(relief="raised", bg='#222b35')
        rightSide_button.config(relief="raised", bg='#222b35')
        leftSide_button.config(relief="raised", bg='#222b35')
        towards_button.config(relief="raised", bg='#222b35')
        away_button.config(relief="raised", bg='#222b35')

def lat_R_med_L_rename():
    if lat_R_med_L_button.config('relief')[-1] == 'sunken':
        lat_R_med_L_button.config(relief="raised", bg='#222b35')
    else:
        lat_R_med_L_button.config(relief="sunken", bg='#FF5733')
        lat_L_med_R_button.config(relief="raised", bg='#222b35')
        oppL_button.config(relief="raised", bg='#222b35')
        oppR_button.config(relief="raised", bg='#222b35')
        MSES_button.config(relief="raised", bg='#222b35')
        ICMS_button.config(relief="raised", bg='#222b35')
        left_button.config(relief="raised", bg='#222b35')
        right_button.config(relief="raised", bg='#222b35')
        rightSide_button.config(relief="raised", bg='#222b35')
        leftSide_button.config(relief="raised", bg='#222b35')
        towards_button.config(relief="raised", bg='#222b35')
        away_button.config(relief="raised", bg='#222b35')

def format_name():
    video_name_box.delete(0, END)
    filename = ''
    error_list = []
    orthotic = str(orthotic_box.get())
    if not orthotic:
        print('You have not entered an orthotic device')
    else:
        filename += orthotic.strip()

    if standing_button.config('relief')[-1] == 'sunken':
        filename += ' Stand'

    if feet_button.config('relief')[-1] == 'sunken':
        filename += ' Feet'

    if overhead_button.config('relief')[-1] == 'sunken':
        filename += ' Overhead' 
    
    if sagittal_button.config('relief')[-1] == 'sunken':
        filename += ' Sag' 

    if left_button.config('relief')[-1] == 'sunken':
        filename += ' L'

    if right_button.config('relief')[-1] == 'sunken':
        filename += ' R'

    if rightSide_button.config('relief')[-1] == 'sunken':
        filename += ' Right side'

    if leftSide_button.config('relief')[-1] == 'sunken':
        filename += ' Left side'

    if ICMS_button.config('relief')[-1] == 'sunken':
        filename += ' IC-MS'

    if MSES_button.config('relief')[-1] == 'sunken':
        filename += ' MS-ES'

    if oppL_button.config('relief')[-1] == 'sunken':
        filename += ' Opp L'

    if oppR_button.config('relief')[-1] == 'sunken':
        filename += ' Opp R'

    if lat_R_med_L_button.config('relief')[-1] == 'sunken':
        filename += ' Lat R Med L'

    if lat_L_med_R_button.config('relief')[-1] == 'sunken':
        filename += ' Lat L Med R'

    if coronal_button.config('relief')[-1] == 'sunken':
        filename += ' Cor' 

    if towards_button.config('relief')[-1] == 'sunken':
        filename += ' Twrds'

    if away_button.config('relief')[-1] == 'sunken':
        filename += ' Away'



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

    video_name_box.insert(0, filename)
    next_button.config(state=ACTIVE, relief="raised")
    
def open_files():
    global selected_video
    root.filename = filedialog.askopenfilenames(initialdir="C:", title="Select files", filetypes=[
        ("all video format", ".avi"),
        ("all video format", ".mp4")
        ]) #gives the entire file location
    filenames_box.delete(0, END)
    files= ""
    global video_names
    video_names = []
    global video_locations
    video_locations = []
    #print(root.filename)
    for file in root.filename:
        split_filename = file.split('/')
        filename_position = len(split_filename)-1
        filename = split_filename[filename_position]
        files = files + filename + " "
        video_names.append(filename)

        formatted_file_location = file.replace('/','\\')
        video_locations.append(formatted_file_location)
        #print(formatted_file_location)
    files = files.strip()
    filenames_box.insert(0, files)
    #print(video_locations)
    #print(video_names)
    selected_video = 0
    

    if video_names:
        global trial_numbers
        trial_numbers = []
        date_time_element = ''
        vicon_number = ''

        for video in video_names:
            video_elements = video.split('.') #Vicon_numberTrialnumber, camera config, YYYYMMDDHHMMSS
            if len(video_elements) == 4:
                vicon_trial_len = len(video_elements[0])
                vicon_trial = str(video_elements[0])
                vicon_number = vicon_trial[0:vicon_trial_len-2]
                trial_number = vicon_trial[vicon_trial_len-2:vicon_trial_len]
                trial_numbers.append(trial_number)
                date_time_element = str(video_elements[2])
                if date_time_element != 'overlay':
                    year_element = date_time_element[0:4]
                    month_element = date_time_element[4:6]
                    day_element = date_time_element[6:8]
                    video_date = day_element + '-' + month_element + '-' + year_element
                    date_box.delete(0, END)
                    date_box.insert(0, video_date)

        #print(trial_numbers)
        #print(vicon_number)
        
        vicon_number_box.delete(0, END)
        vicon_number_box.insert(0, vicon_number)            

        my_label.grid_forget()
        sagittal_button.config(state=ACTIVE, relief="raised", bg='#222b35', fg="#ffffff")
        left_button.config(state=ACTIVE, relief="raised", bg='#222b35', fg="#ffffff")
        right_button.config(state=ACTIVE, relief="raised", bg='#222b35', fg="#ffffff")
        leftSide_button.config(state=ACTIVE, relief="raised", bg='#222b35', fg="#ffffff")
        rightSide_button.config(state=ACTIVE, relief="raised", bg='#222b35', fg="#ffffff")
        coronal_button.config(state=ACTIVE, relief="raised", bg='#222b35', fg="#ffffff")
        towards_button.config(state=ACTIVE, relief="raised", bg='#222b35', fg="#ffffff")
        away_button.config(state=ACTIVE, relief="raised", bg='#222b35', fg="#ffffff")
        feet_button.config(state=ACTIVE, relief="raised", bg='#222b35', fg="#ffffff")
        standing_button.config(state=ACTIVE, relief="raised", bg='#222b35', fg="#ffffff")
        overhead_button.config(state=ACTIVE, relief="raised", bg='#222b35', fg="#ffffff")
        skip_button.config(state=ACTIVE, relief="raised")
        replay_button.config(state=ACTIVE, relief="raised")
        MSES_button.config(state=ACTIVE, relief="raised")
        ICMS_button.config(state=ACTIVE, relief="raised")
        oppR_button.config(state=ACTIVE, relief="raised")
        oppL_button.config(state=ACTIVE, relief="raised")
        lat_L_med_R_button.config(state=ACTIVE, relief="raised")
        lat_R_med_L_button.config(state=ACTIVE, relief="raised")
        next()
def next():
    global selected_video
    global my_label
    global old_time
    global new_time

    if selected_video == 0:
        old_time = datetime.now()
        if trial_numbers:
            trial_number_box.delete(0, END)
            trial_number_box.insert(0, trial_numbers[selected_video])

        my_label.grid_forget()
        my_label = Label(root)
        my_label.grid(row = 0, column = 0, rowspan = 11, sticky = W, padx=(4,4))
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
        connect_to_database(username, dAte, tIme, video_names[selected_video-1], video_name_final, duration)

        next_button.config(state=DISABLED)
        skip_button.config(state=DISABLED)
        replay_button.config(state=DISABLED)
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
            trial_number_box.delete(0, END)
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
        connect_to_database(username, dAte, tIme, video_names[selected_video-1], video_name_final, duration)
        old_time = datetime.now()

        my_label = Label(root)
        my_label.grid(row = 0, column = 0, rowspan = 11, sticky = W, padx=(4,4))
        path = os.path.join(os.path.dirname(sys.executable), video_locations[selected_video])
        player = tkvideo(path, my_label, loop = 0)
        player.play()

    selected_video += 1
    next_button.config(state=DISABLED, relief="raised")

def skip():
    global selected_video
    global my_label
    global old_time
    #print(selected_video)

    if selected_video >= len(video_locations):

        my_label.grid_forget()
        next_button.config(state=DISABLED)
        skip_button.config(state=DISABLED)
        replay_button.config(state=DISABLED)
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
            trial_number_box.delete(0, END)
            trial_number_box.insert(0, trial_numbers[selected_video])   

        my_label = Label(root)
        my_label.grid(row = 0, column = 0, rowspan = 11, sticky = W, padx=(4,4))
        path = os.path.join(os.path.dirname(sys.executable), video_locations[selected_video])
        player = tkvideo(path, my_label, loop = 0)
        player.play()
        old_time = datetime.now()

    selected_video += 1
    next_button.config(state=DISABLED, relief="raised")
def replay():
    global selected_video
    global my_label
    selected_video -= 1
    my_label.grid_forget()
    my_label = Label(root)
    my_label.grid(row = 0, column = 0, rowspan = 11, sticky = W, padx=(4,4))
    path = os.path.join(os.path.dirname(sys.executable), video_locations[selected_video])
    player = tkvideo(path, my_label, loop = 0)
    player.play()
    selected_video += 1


my_label = Label(root)
my_label.grid(row = 0, column = 0, rowspan = 11, sticky = W, padx=(4,4))

video_name_box = Entry(root, bg='#222b35', fg="#ffffff", font=10, width=50, insertbackground="#ffffff")
orthotic_box = Entry(root, bg='#222b35', fg="#ffffff", font=10, width=35, insertbackground="#ffffff")

orthotic_box_label = Label(root, text="Condition:", bg='#19232d', fg="#ffffff", font=18)
filenames_box_label = Label(root, text="Videos:", bg='#19232d', fg="#ffffff", font=18)
hospital_number_box_label = Label(root, text="Hosp no:", bg='#19232d', fg="#ffffff", font=18)
vicon_number_box_label = Label(root, text="Vicon no:", bg='#19232d', fg="#ffffff", font=18)
date_box_label = Label(root, text="Date:", bg='#19232d', fg="#ffffff", font=18)
trial_number_box_label = Label(root, text="Trial no:", bg='#19232d', fg="#ffffff", font=18)

sagittal_button = Button(root, text="Sag", command=lambda:[sagittal_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)
left_button = Button(root, text="L", command=lambda:[left_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)
right_button = Button(root, text="R", command=lambda:[right_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)
leftSide_button = Button(root, text="Left side", command=lambda:[leftSide_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)
rightSide_button = Button(root, text="Right side", command=lambda:[rightSide_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)
coronal_button = Button(root, text="Cor", command=lambda:[coronal_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)
towards_button = Button(root, text="Twrds", command=lambda:[towards_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)
away_button = Button(root, text="Away", command=lambda:[away_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)
feet_button = Button(root, text="Feet", command=lambda:[feet_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)
standing_button = Button(root, text="Stand", command=lambda:[standing_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)
lat_L_med_R_button = Button(root, text="Lat L Med R", command=lambda:[lat_L_med_R_rename(), format_name()], bg='#222b35', fg="#ffffff", width=13, font=18, relief="raised", state=DISABLED)
lat_R_med_L_button = Button(root, text="Lat R Med L", command=lambda:[lat_R_med_L_rename(), format_name()], bg='#222b35', fg="#ffffff", width=13, font=18, relief="raised", state=DISABLED)
#lat_right_button = Button(root, text="Lat right", command=lambda:[lat_right_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)
#lat_left_button = Button(root, text="Lat left", command=lambda:[lat_left_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)
overhead_button = Button(root, text="Overhead", command=lambda:[overhead_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)
#med_button = Button(root, text="Overhead", command=lambda:[med_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)
#lat_button = Button(root, text="Overhead", command=lambda:[lat_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)
oppL_button = Button(root, text="Opp L", command=lambda:[oppL_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)
oppR_button = Button(root, text="Opp R", command=lambda:[oppR_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)
ICMS_button = Button(root, text="IC-MS", command=lambda:[ICMS_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)
MSES_button = Button(root, text="MS-ES", command=lambda:[MSES_rename(), format_name()], bg='#222b35', fg="#ffffff", width=8, font=18, relief="raised", state=DISABLED)


#format_name_button = Button(root, text="Format file name", command=format_name, bg='#222b35', fg="#ffffff", font=18, relief="raised", width=25, state=DISABLED)
next_button = Button(root, text="Next video", command=next, bg='#222b35', fg="#ffffff", font=18, relief="raised", width=25, state=DISABLED)
skip_button = Button(root, text="Skip", command=skip, bg='#222b35', fg="#ffffff", font=18, relief="raised", width=8, state=DISABLED)
replay_button = Button(root, text="Replay", command=replay, bg='#222b35', fg="#ffffff", font=18, relief="raised", width=8, state=DISABLED)

file_open_button = Button(root, text="Browse", command=open_files, bg='#222b35', fg="#ffffff", font=18, width=8)
filenames_box = Entry(root, width=25, bg='#222b35', fg="#ffffff", font=10, insertbackground="#ffffff")

hospital_number_box = Entry(root, width=8, bg='#222b35', fg="#ffffff", font=10, insertbackground="#ffffff")
date_box = Entry(root, width=8, bg='#222b35', fg="#ffffff", font=10, insertbackground="#ffffff")
vicon_number_box = Entry(root, width=8, bg='#222b35', fg="#ffffff", font=10, insertbackground="#ffffff")

trial_number_box = Entry(root, width=8, bg='#222b35', fg="#ffffff", font=10, insertbackground="#ffffff")

filenames_box_label.grid(row=0, column=1, pady=(2,2))
filenames_box.grid(row=0, column=2, columnspan = 3, pady=(2,2))
file_open_button.grid(row=0, column=5, pady=(2,8))

hospital_number_box_label.grid(row=1, column=1, pady=(8,2))
hospital_number_box.grid(row=1, column=2, pady=(8,2))
vicon_number_box_label.grid(row=1, column=4, pady=(8,2))
vicon_number_box.grid(row=1, column=5, pady=(8,2))
date_box_label.grid(row=2, column=1, pady=(2,16))
date_box.grid(row=2, column=2, pady=(2,16))
trial_number_box_label.grid(row=2, column=4, pady=(2,16))
trial_number_box.grid(row=2, column=5, pady=(2,16))

orthotic_box_label.grid(row=4, column=1, pady=(16,4))
orthotic_box.grid(row=4, column=2, columnspan = 4, pady=(16,4))

sagittal_button.grid(row=5, column=1, pady=(6,6))
coronal_button.grid(row=5, column=2, pady=(6,6))
feet_button.grid(row=5, column=5, pady=(6,6))
standing_button.grid(row=5, column=4, pady=(6,6))
overhead_button.grid(row=5, column=3, pady=(6,6))

#med_button.grid(row=6, column=2, pady=(2,2))
#lat_button.grid(row=6, column=4, pady=(2,2))

left_button.grid(row=7, column=1, pady=(2,6))
right_button.grid(row=6, column=1, pady=(6,2))
oppL_button.grid(row=7, column=2, pady=(2,6))
oppR_button.grid(row=6, column=2, pady=(6,2))
leftSide_button.grid(row=7, column=3, pady=(2,6))
rightSide_button.grid(row=6, column=3, pady=(6,2))
towards_button.grid(row=7, column=4, pady=(2,6))
away_button.grid(row=6, column=4, pady=(6,2))
ICMS_button.grid(row=7, column=5, pady=(2,6))
MSES_button.grid(row=6, column=5, pady=(6,2))



lat_L_med_R_button.grid(row=8, column=1, columnspan = 3, pady=(6,6))
#med_left_button.grid(row=8, column=2, pady=(6,6))
lat_R_med_L_button.grid(row=8, column=3, columnspan = 3, pady=(6,6))
#lat_left_button.grid(row=8, column=4, pady=(6,6))

video_name_box.grid(row=9, column=1, columnspan=5, pady=(6,2))
next_button.grid(row=10, column=2, columnspan=3, pady=(2,2))
skip_button.grid(row=10, column=5, pady=(2,2))
replay_button.grid(row=10, column=1, pady=(2,2))

#icon_path = path.abspath(path.join(path.dirname(__file__), 'Camcorder_Pro_icon-icons.com_54204.ico'))
root.iconbitmap('Camcorder_Pro_icon-icons.com_54204.ico')


if __name__ == "__main__":
    main()
