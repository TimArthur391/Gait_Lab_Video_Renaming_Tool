# Gait Lab Video Renaming Tool

As part of our daily routine at ORLAU (Robert Jones and Agnes Hunt Orthopaedic Hospital), we have to export videos from Vicon Nexus and rename these in a certain format. This was a tedious process that required the user to 'right click > rename > figure out what the name had to be > type out the name' for upwards of 20 videos.

This python tool, based upon tkinter and tkinter_video, provides the user with a GUI to significantly speed up the process. The tool is intended to be downloaded off of a central server on local machines. Also implemented in the tool:
(1) usage data is collected from whomever uses the app locally and sent to a central MySQL server,
(2) an automatic update process that is trigger when a new version of the tool is published on our department code repository server and a MySQL table is updated.

This project was my first attempt at using GitHub and Git for change control.
