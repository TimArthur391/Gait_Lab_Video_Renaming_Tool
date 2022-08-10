try:
    from scrpt.__main__ import main
    import sys

    if __name__ == '__main__':
        sys.exit(main())
except Exception as Argument:
    import time
    import os

    f = open("log.txt", "a")

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