try:
    import sys
    import scrpt.check_version_and_update as cvu
    

    if __name__ == '__main__':
        sys.exit(cvu.check_update())
except Exception as Argument:
    import time
    import os

    f = open("helpers\\log.txt", "a")

    # writing in the file
    f.write("\n" + time.strftime("%d %b %Y %H:%M:%S", time.gmtime()) + "    " + os.getlogin() + "    ERROR: " + str(Argument))
    
    # closing the file
    f.close()
    print("""
---------------------------------------------------------
------------------AN ERROR HAS OCCURED-------------------
---------------------------------------------------------
------------------THIS HAS BEEN LOGGED-------------------
---------------------------------------------------------
-----------PLEASE INFORM TIMOTHY.ARTHUR1@NHS.NET---------
---------------------------------------------------------
    """)
    time.sleep(5)