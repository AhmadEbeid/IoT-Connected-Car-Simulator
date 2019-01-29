
To run the dashboard go to the dashboard folder and run the 2 .bat files

To run the car simulators --> first run the dispatcher, then the predicts, then the transformer, after that you can run the car simulators with any order

The data used is all the same except for the VIN number

The Real Time Database used is firebse, it can be accessed by this link: https://testing-894c8.firebaseio.com/.json?print=pretty

You can also create a firebase database and change the url in the files, using a VSCode for example search for the url and change them with new firebase link
the firebase used is the old realtime firebase database not the new
the link will need to be changed in 3 files, 1- dispatcher.py, 2- main.57d8xxxxx.js, 3- deleteDatabaseData script

To delete all the data to start the simulation from the beginning run the deleteDatabaseData python script