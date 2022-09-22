#buttons = "left", "right", "sagittal", "left_side", "right_side", "towards", "away",
#                    "coronal", "feet", "stand", "overhead", "mses", "icms", "opp_right", "opp_left", 
#                    "lat_l_med_r", "lat_r_med_l"
table = dict()
table["left"] = ["right", "opp_left", "right_side", 
                    "left_side", "icms", "mses", "lat_r_med_l", "lat_l_med_r"]
table["right"] = ["left", "opp_right", "right_side", 
                    "left_side", "icms", "mses", "lat_r_med_l", "lat_l_med_r"]
table["sagittal"] = ["overhead", "coronal"]
table["left_side"] = ["right", "left", "opp_left", "right_side", 
                        "icms", "mses", "lat_r_med_l", "lat_l_med_r"]
table["right_side"] = ["right", "left", "opp_right", "left_side", 
                        "icms", "mses", "lat_r_med_l", "lat_l_med_r"]
table["towards"] = ["away", "icms", "mses", "lat_r_med_l", "lat_l_med_r"]
table["away"] = ["towards", "icms", "mses", "lat_r_med_l", "lat_l_med_r"]
table["coronal"] = ["overhead", "sagittal"]
table["overhead"] = ["coronal", "sagittal"]
table["mses"] = ["opp_left", "opp_right", "lat_r_med_l", "lat_l_med_r"]
table["icms"] = ["opp_left", "opp_right", "lat_r_med_l", "lat_l_med_r"]
table["opp_right"] = ["opp_left", "right", "right_side", 
                        "lat_r_med_l", "lat_l_med_r"]
table["opp_left"] = ["opp_right", "left", "left_side", 
                        "lat_r_med_l", "lat_l_med_r"]
table["lat_l_med_r"] = ["left", "right", "left_side", "right_side", "towards", "away",
                        "mses", "icms", "opp_right", "opp_left", "lat_r_med_l"]
table["lat_r_med_l"] = ["left", "right", "left_side", "right_side", "towards", "away",
                        "mses", "icms", "opp_right", "opp_left", "lat_l_med_r"]
table["stand"] = []
table["feet"]= []

def get_button_names(button_name):
    return table[button_name]

def get_video_names(filenames):
    video_names = []
    for file in filenames:
        split_filename = file.split('/')
        filename_position = len(split_filename)-1
        filename = split_filename[filename_position]
        video_names.append(filename)

    return video_names

def get_video_file_directories(filenames):
    video_locations = []
    for file in filenames:
        formatted_file_location = file.replace('/','\\')
        video_locations.append(formatted_file_location)

    return video_locations

def get_trial_numbers(filenames):
    trial_numbers = []
    for video in get_video_names(filenames):
        video_elements = video.split('.') #Vicon_numberTrialnumber, camera config, YYYYMMDDHHMMSS
        if len(video_elements) == 4:
            vicon_trial_len = len(video_elements[0])
            vicon_trial = str(video_elements[0])
            trial_number = vicon_trial[vicon_trial_len-2:vicon_trial_len]
            trial_numbers.append(trial_number)

    return trial_numbers

def get_session_datetime(filenames):
    video_date = ''
    for video in get_video_names(filenames):
        video_elements = video.split('.') #Vicon_numberTrialnumber, camera config, YYYYMMDDHHMMSS
        if len(video_elements) == 4:
            date_time_element = str(video_elements[2])
            if date_time_element != 'overlay':
                year_element = date_time_element[0:4]
                month_element = date_time_element[4:6]
                day_element = date_time_element[6:8]
                video_date = day_element + '-' + month_element + '-' + year_element
        
    return video_date

def get_vicon_number(filenames):
    vicon_number = ''
    for video in get_video_names(filenames):
        video_elements = video.split('.') #Vicon_numberTrialnumber, camera config, YYYYMMDDHHMMSS
        if len(video_elements) == 4:
            vicon_trial_len = len(video_elements[0])
            vicon_trial = str(video_elements[0])
            vicon_number = vicon_trial[0:vicon_trial_len-2]

    return vicon_number
