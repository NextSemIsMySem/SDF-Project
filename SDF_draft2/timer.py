from tkinter import *
import time
import winsound
import json

#frame setting
root = Tk()
root.title("Timer")
root.geometry("400x600")
root.config(bg = "#000")
root.resizable(False,False)

heading=Label(root,text = "Timer",font = "arial 30 bold",bg = "#000",fg = "#ea3548")
heading.pack(pady=10)

#Clock that displays current time
Label(root, font = ("arial",15,"bold"), text="current time: ", bg = "papaya whip").place(x = 65, y = 70)

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    current_time.config(text = clock_time)
    current_time.after(1000, clock)

current_time = Label(root,font = ("arial", 15, "bold"),text = "", fg = "#000", bg = "#fff" )
current_time.place(x = 190, y = 70)
clock()

#timer buttons
hrs = StringVar()
Entry(root, textvariable = hrs, width = 2, font = "arial 50", bg = "#000", fg = "#fff", bd = 0).place(x = 30, y = 155)
hrs.set("00")

mins = StringVar()
Entry(root, textvariable = mins, width = 2, font = "arial 50", bg = "#000", fg = "#fff", bd = 0).place(x = 150, y = 155)
mins.set("00")

secs = StringVar()
Entry(root, textvariable = secs, width = 2, font = "arial 50", bg = "#000", fg = "#fff", bd = 0).place(x = 270, y = 155)
secs.set("00")

#timer display
Label(root,text = "hours", font = "arial 12", bg = "#000", fg = "#fff").place(x = 105, y = 200)
Label(root,text = "mins", font = "arial 12", bg = "#000", fg = "#fff").place(x = 225, y = 200)
Label(root,text = "secs", font = "arial 12", bg = "#000", fg = "#fff").place(x = 345, y = 200)

#countdown function
def Timer():
    times = int (hrs.get())*3600 + int(mins.get())*60 + int(secs.get())

    while times > -1:
        minute, second = (times // 60, times % 60)

        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)

        secs.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)

        if (times == 0):
            winsound.Beep(1000, 1000)
            secs.set("00")
            mins.set("00")
            hrs.set("00")

        times -= 1

#start button
button = Button(root, text = "Start", bg = "#ea3458", bd = 0, fg = "#fff", width = 20, height = 2, font = "arial 10 bold", command = Timer)
button.pack(padx = 5, pady = 40, side = BOTTOM)






root.mainloop()

