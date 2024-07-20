from tkinter import *
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

root = Tk()
root.title("Digital Clock")

time_label = Label(root, font=("Arial", 48), bg="black", fg="green")
time_label.pack()

update_time()

root.mainloop()
