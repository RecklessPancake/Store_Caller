# Store Caller

Simple program for some better QOL. 

Used to need to call stores by finding them on a printed Excel sheet and dial in the phone number.
This program chagned it to where all we needed to do is type in the store's 5 digit ID and it will populate the boxes with apporiate information and 
can also call the store with a single keypress.

Uses Tkinkter for a simple gui, connects to a SQL server hosting the Stores data, creates a SQL query based on the user's input.

Takes the tuple SQL response into variables and fills in apportiate text boxes. 

When the enter key is pressed it will make a GET request to the VOIP phone and intiate a call to which ever store was searched.

**Requirments**
- Tkinter
- win32gui, win32con
- mysql.connector
- requests
