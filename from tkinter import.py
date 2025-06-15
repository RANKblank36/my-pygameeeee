# Import necessary libraries

from tkinter import *

# Create Window

root = Tk()

root.title('Login App')

root.geometry('400x400')

# Create a frame to organize elements better

frame = Frame(master=root, height=200, width=360, bg="#d0efff")

# Add widgets

# Add Label for Full Name

lbl1 = Label(frame, text="Full Name", bg="#3895D3", fg='white', width=12)

# Add Label for Email Id

lbl2 = Label(frame, text="Email Id", bg="#3895D3", fg='white', width=12)

# Add Label for Enter Password

lbl3 = Label(frame, text="Enter Password", bg="#3895D3", fg='white', width=12)

# Use Entry Widget to create a text box for user to enter details

name_entry = Entry(frame)

email_entry = Entry(frame)

pass_entry = Entry(frame, show="*") # 'show="*" hides the password characters

# Function to display message after account creation

def display():

# Get the name entered by the user

      name = name_entry.get()

# Create a greeting message

      greet = "Hey " + name

# Create a congratulatory message

      message = "\nCongratulations for your new account!"

# Insert the greeting into the textbox

      textbox.insert(END, greet)

# Insert the congratulatory message into the textbox

      textbox.insert(END, message)

textbox = Text(bg="#BEBEBE", fg="black")

btn = Button(text="Create Account", command=display, bg="red")

frame.place(x=20, y=0)

lbl1.place(x=20, y=20)

name_entry.place(x=150, y=20)

# Place the Email Id label and entry field

lbl2.place(x=20, y=80)

email_entry.place(x=150, y=80)

# Place the Password label and entry field

lbl3.place(x=20, y=140)

pass_entry.place(x=150, y=140)

# Place the Create Account button

btn.place(x=130, y=210)

textbox.place(y=250)

root.mainloop()