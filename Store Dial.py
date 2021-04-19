import tkinter as tk
import win32gui, win32con
import mysql.connector
import requests
from requests.auth import HTTPBasicAuth

#Hide console
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)


root= tk.Tk()
#Create window
canvas1 = tk.Canvas(root, width = 350, height = 300)
canvas1.pack()

label1 = tk.Label(root, text='Store Dialer')
label1.config(font=('helvetica', 14))
canvas1.create_window(150, 25, window=label1)

label2 = tk.Label(root, text='Type store ID:')
label2.config(font=('helvetica', 10))
canvas1.create_window(50, 50, window=label2)

storeID = None

entry1 = tk.Entry (root, textvariable=storeID) 
canvas1.create_window(160, 50, window=entry1)

label2 = tk.Label(root, text='Store Name')
label2.config(font=('helvetica', 10))
canvas1.create_window(50, 85, window=label2)

entry2 = tk.Entry (root, width=40) 
canvas1.create_window(225, 85, window=entry2)
#entry2.bind("<Key>", lambda e: "break")

label3 = tk.Label(root, text='Address')
label3.config(font=('helvetica', 10))
canvas1.create_window(50, 110, window=label3)

entry3 = tk.Entry (root, width=40) 
canvas1.create_window(225, 110, window=entry3)
#entry3.bind("<Key>", lambda e: "break")

label4 = tk.Label(root, text='Phone #')
label4.config(font=('helvetica', 10))
canvas1.create_window(50, 135, window=label4)

entry4 = tk.Entry (root, width=40) 
canvas1.create_window(225, 135, window=entry4)
#entry4.bind("<Key>", lambda e: "break")

label5 = tk.Label(root, text='Email')
label5.config(font=('helvetica', 10))
canvas1.create_window(50, 160, window=label5)

entry5 = tk.Entry (root, width=40) 
canvas1.create_window(225, 160, window=entry5)
#entry5.bind("<Key>", lambda e: "break")

label6 = tk.Label(root, text='Manager')
label6.config(font=('helvetica', 10))
canvas1.create_window(50, 185, window=label6)

entry6 = tk.Entry (root, width=40) 
canvas1.create_window(225, 185, window=entry6)
#entry6.bind("<Key>", lambda e: "break")

#establishing the connection
conn = mysql.connector.connect(
   user='[redacted]', password='[redacted]', host='[redacted]', database='[redacted]')

cursor = conn.cursor()

global url
url = " "
number = None

def storeSearch(event=None):
    storeID = entry1.get()
    sql = "SELECT * FROM [redacted] WHERE ID="+ storeID

    cursor.execute(sql)

    id, name, address, number, email, manager = cursor.fetchone();
    
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')
    entry6.delete(0, 'end')
    
    entry2.insert(0, name)
    entry3.insert(0, address)
    entry4.insert(0, number)
    entry5.insert(0, email)
    entry6.insert(0, manager)

    global url
    url = "http://[VOIP Phone IP]/servlet?key=number="+number
    #print(url)
    print(len(storeID))
def storeCall(event=None):
    global url
    print(url)
    requests.get(url, auth=('[redacted]','[redacted]'))

def entryCheck(event=None):
    if len(entry1.get()) == 5:
        storeSearch()
            

button1 = tk.Button(text='Search', command=storeSearch, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(255, 50, window=button1)

button2 = tk.Button(text='Call', command=storeCall, bg='green', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(305, 50, window=button2)

root.bind('<Return>', storeCall)
root.bind('<Any-KeyPress>', entryCheck)





root.mainloop()
