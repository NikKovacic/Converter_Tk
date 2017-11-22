# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox

root = Tk()

#  title
root.title("Converter")
#  greeting
greeting = Label(root, text="Please enter a number of kilometers that you'd like to convert into miles:")
greeting.pack()
#  entry field
entry_num = Entry(root)
entry_num.pack()


def converter():
    try:
        x = int(entry_num.get()) * 0.621371
        result_text = "{0} km is {1} miles.".format(int(entry_num.get()), x)
    except Exception or ValueError:
        result_text = "ERROR!\nPlease check if you entered the number!"

    tkMessageBox.showinfo("Result", result_text)


button = Button(root, text="Convert", command=converter, bg="blue", fg="white")
button.pack()
root.mainloop()
