from tkinter import *
import time

window = Tk()
window.geometry("500x250")


def for_current_time():
    current_time = time.strftime("%H:%M:%S")
    # print(current_time)
    clock_label.config(text=current_time)  # aur yha pr text add kr diya clock_label ko config krke
    # for running of timer continuously we call for_current_time() function every 200 micro seconds
    clock_label.after(200, for_current_time)


clock_label = Label(window, font="times 50 bold", bg="white")
# in this clock_label i have not set the text so i can set it further by using config
clock_label.grid(row=2, column=2, pady=25, padx=100)
for_current_time()

label_heading = Label(window, text="Digital Clock", font="times 24 bold")
label_heading.grid(row=0, column=2)

label3 = Label(text="hours   minutes    seconds", font="times 15 bold")
label3.grid(row=3, column=2)

for_current_time()
window.mainloop()
