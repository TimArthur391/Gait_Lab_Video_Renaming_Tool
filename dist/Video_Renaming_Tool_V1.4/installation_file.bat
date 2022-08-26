rem This file will allow the installation to be done through a single click in the Code_Repository
rem by the user. It will also be used to allow automatic updates to made. Follow the intructions
rem to edit this file accordingly

rem Be sure to update the name of the application and version number
echo RUNNING INSTALLATION OF 'Gait_Lab_Video_Renaming_Tool' VERSON '1.4'

rem this copies the installation file to the users documents. replace 'A:\ZIP_FILE_LOCATION' with
rem the file path of the application bundle or file.
xcopy /s A:\Code_repository\Matlab_Python_Code\Validated\25_Gait_Lab_Video_Renaming_Tool\Video_Renaming_Tool_V1.4.zip %userprofile%\Documents

rem this will extract the contents of the zip'd file into the documents folder. Be sure to change
rem the 'FILENAME.zip' in the line bellow with your zip'd file name
powershell -command "Expand-Archive -Force '%userprofile%\Documents\Video_Renaming_Tool_V1.4.zip' '%userprofile%\Documents'"

rem this will create a shortcut to the application you wish to run.
rem edit 'APPLICATION_shortcut.lnk' below to the name of the shortcut you want to create
rem edit 'Documents\FILENAME\APPLICATION_NAME.exe' below to the location of your application exectuable
rem edit 'Documents\FILENAME' below to the folder location of your application executable
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%userprofile%\Desktop\Video_Renaming_Tool_V1.4_shortcut.lnk');$s.TargetPath='%userprofile%\Documents\Video_Renaming_Tool_V1.3\Video_Renaming_Tool_V1.4.exe';$s.WorkingDirectory='%userprofile%\Documents\Video_Renaming_Tool_V1.4';$s.Save()"