import scrpt.database_connection as db
import json

#The developer should run this script to update the SQL database with the information in the
#'application_information.JSON' file

def main() -> None:
    with open("application_information.JSON", "r") as read_file:
        application_information = json.load(read_file)

    APPLICATION = application_information['applicationName']
    VERSION_NUMBER = application_information['applicationVersion']
    UPDATE_DATE = application_information['updateDate']


    database_name = "version_control"
    SQL_statement = "select RECORDID from version_log where APPLICATION = '{}' and VERSION_NUMBER = {}".format(APPLICATION, VERSION_NUMBER)
    query_results = db.get_request(SQL_statement, database_name)
    if query_results:
        #record already exists
        print('This version number already exists for this application, please check the JSON file and try again')
    else:
        SQL_statement = ("INSERT INTO version_log (APPLICATION, VERSION_NUMBER, UPDATE_DATE) VALUES (%s, %s, %s)")
        data = (APPLICATION, VERSION_NUMBER, UPDATE_DATE)
        db.post_request(SQL_statement, data, database_name)
        print('Database updated')

if __name__ == '__main__':
    main()