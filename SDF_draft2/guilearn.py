from tkinter import *
from tkinter import font as tkFont

def processButton():
    text1.delete("1.0", END)
    text1.insert(END, "Hello GUI, My name is John Doe")

win = Tk()
win.title("My first GUI in python")
frame1=Frame(win)
frame1.pack()

font1 = tkFont.Font(family = "Arial", size = 30, weight = "bold")

text1 = Text(win)
text1.pack()
#line below is EVENT-DRIVEN PROGRAMMING
btnShow=Button(frame1, text = "Click Me", font = font1, height = 3, width = 10, fg = "red", activebackground = "yellow", command = processButton)
btnShow.grid(row = 1, column = 1)



win.configure(bg = "lightblue")
win.geometry(f'{500}x{600}+{400}+{100}')
win.mainloop()