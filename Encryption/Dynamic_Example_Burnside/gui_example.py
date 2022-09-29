from tkinter import *

root = Tk()

e =Entry(root)
e.pack()
e.insert(0, "Enter Your Message")

def myClick():
    myLabel = Label(root, text = "Your message is: " + e.get())
    myLabel.pack()

myButton = Button(root, text = 'Submit', command = myClick)
myButton.pack()

root.mainloop()