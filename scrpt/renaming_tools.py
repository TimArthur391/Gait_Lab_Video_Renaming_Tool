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
