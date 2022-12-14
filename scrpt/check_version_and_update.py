import scrpt.database_connection as db
from scrpt.__main__ import main
import json
import subprocess
import socket
import sys
import importlib

#Run check_update()
#This calls the other sub-functions: get_version_from_database, get_info_from_application_JSON_file,
#update_program and launch_program

#launch_program will start the script which is in the applicationLaunchScript element of the JSON file
#be careful the path to the script is correct

def get_version_from_database(application_name):
    SQL_statement = "SELECT max(version_number) as version_number FROM version_log where APPLICATION = '" + application_name + "'"
    database_name = "version_control"
    query_results = db.get_request(SQL_statement, database_name)
    latest_version = query_results[0][0]
    print('Latest version available is', float(latest_version))

    return latest_version

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

def check_update():
    application_information = get_info_from_application_JSON_file()
    application_version = application_information["applicationVersion"]
    print('The current application version is', application_version)

    application_name = application_information["applicationName"]
    latest_version = get_version_from_database(application_name)

    if float(application_version) < float(latest_version):
        while True:
            answer = input(
"""
---------------------------------------------------------
--------------YOU ARE USING AN OLD VERION----------------
---------------------------------------------------------
-------------WOULD YOU LIKE TO UPDATE NOW?---------------
---------------------------------------------------------
------------TYPE 'Y' FOR YES AND 'N' FOR NO--------------
---------------------------------------------------------
"""
            )
            if answer.upper() in ('Y','N'):
                break
            else:
                print(
"""
---------------------------------------------------------
-----THAT WAS NOT A VALID RESULT, PLEASE TRY AGAIN-------
---------------------------------------------------------
"""
                )
                continue

        if answer.upper() == 'Y':
            update_program()

        elif answer.upper() == 'N':
            print(
"""
---------------------------------------------------------
----------NO PROBLEM, REMEMBER TO DO IT LATER------------
---------------------------------------------------------
"""
                )
            launch_program()

    else:
        launch_program()

def update_program():
    #install application
    host=socket.gethostname()
    if host == 'LAPTOP-KFBV6SUT':
        #This is Tim's laptop name (Test enviroment)
        application_information = get_info_from_application_JSON_file()
        installation_file_path = application_information['pathToInstallationBATFileTest']
        subprocess.run([installation_file_path])
    else:
        #This is for ORLAU computers
        application_information = get_info_from_application_JSON_file()
        installation_file_path = application_information['pathToInstallationBATFileProduction']
        subprocess.run([installation_file_path])

def launch_program():
    sys.exit(main())

if __name__ == '__main__':
    check_update()