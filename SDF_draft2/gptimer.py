from tkinter import *
import time
from tkinter import simpledialog
from tkinter import messagebox
import os

# Initialize the main application window
root = Tk()
root.title("Enhanced Timer")
root.geometry("500x700")
root.config(bg="#000")
root.resizable(False, False)

# Heading
heading = Label(root, text="Enhanced Timer", font="arial 30 bold", bg="#000", fg="#ea3548")
heading.pack(pady=10)

# Current time display
Label(root, font=("arial", 15, "bold"), text="Current time:", bg="papaya whip").place(x=65, y=70)
current_time = Label(root, font=("arial", 15, "bold"), text="", fg="#000", bg="#fff")
current_time.place(x=190, y=70)

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000, clock)

clock()

# Timer input fields
hrs, mins, secs = StringVar(), StringVar(), StringVar()
Entry(root, textvariable=hrs, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=30, y=155)
Entry(root, textvariable=mins, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=150, y=155)
Entry(root, textvariable=secs, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=270, y=155)
hrs.set("00"), mins.set("00"), secs.set("00")

Label(root, text="hours", font="arial 12", bg="#000", fg="#fff").place(x=105, y=200)
Label(root, text="mins", font="arial 12", bg="#000", fg="#fff").place(x=225, y=200)
Label(root, text="secs", font="arial 12", bg="#000", fg="#fff").place(x=345, y=200)

# Timer functionality
timer_running = False
paused_time = 0

# Timer alert with pop-up and system bell sound
def timer_alert():
    print("\a")  # System bell sound
    messagebox.showinfo("Time's Up", "The timer has finished!")

def start_timer():
    global timer_running, paused_time
    if not timer_running:
        timer_running = True
        countdown(int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(secs.get()))

def countdown(time_left):
    global timer_running, paused_time
    if time_left < 0 or not timer_running:
        timer_running = False
        return

    hrs.set(f"{time_left // 3600:02}")
    mins.set(f"{(time_left % 3600) // 60:02}")
    secs.set(f"{time_left % 60:02}")

    if time_left == 0:
        timer_alert()  # Trigger alert
    else:
        root.after(1000, lambda: countdown(time_left - 1))

def pause_timer():
    global timer_running, paused_time
    if timer_running:
        paused_time = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(secs.get())
        timer_running = False

def reset_timer():
    global timer_running
    timer_running = False
    hrs.set("00"), mins.set("00"), secs.set("00")

# Save and load timers
timers_file = "timers.txt"

def save_timer():
    remark = simpledialog.askstring("Save Timer", "Enter timer remark:")
    if remark:
        with open(timers_file, "a") as file:
            file.write(f"{remark}:{hrs.get()}:{mins.get()}:{secs.get()}\n")
        load_saved_timers()

def load_saved_timers():
    if not os.path.exists(timers_file):
        return

    with open(timers_file, "r") as file:
        lines = file.readlines()

    for widget in saved_timers_frame.winfo_children():
        widget.destroy()

    for line in lines:
        try:
            remark, h, m, s = line.strip().split(":")
            Button(saved_timers_frame, text=remark, bg="#ea3548", fg="#fff", command=lambda h=h, m=m, s=s: load_timer(h, m, s)).pack(pady=2)
        except ValueError:
            continue

def load_timer(h, m, s):
    hrs.set(h)
    mins.set(m)
    secs.set(s)

# Presets area
saved_timers_frame = Frame(root, bg="#000")
saved_timers_frame.pack(pady=10)

load_saved_timers()

# Buttons
Button(root, text="Start", bg="#ea3548", fg="#fff", width=10, height=2, command=start_timer).pack(side=LEFT, padx=10)
Button(root, text="Pause", bg="#ffa500", fg="#fff", width=10, height=2, command=pause_timer).pack(side=LEFT, padx=10)
Button(root, text="Reset", bg="#32cd32", fg="#fff", width=10, height=2, command=reset_timer).pack(side=LEFT, padx=10)
Button(root, text="Save Timer", bg="#0000ff", fg="#fff", width=10, height=2, command=save_timer).pack(side=LEFT, padx=10)

root.mainloop()
