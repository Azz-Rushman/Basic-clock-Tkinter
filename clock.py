from tkinter import *
from time import *


def update():   # Recursive Function instead of While Loop.
    time_string = strftime('%I:%M:%S %p')
    timeLabel.config(text=time_string)

    day_string = strftime('%A')
    day_label.config(text=day_string)

    date_string = strftime('%B %d, %Y')
    date_label.config(text=date_string)

    window.after(1000, update)  # Recursive Step.


window = Tk()

time_obj = localtime()

timeLabel = Label(window, font=('arial', 30,), fg='green', bg='black')
timeLabel.pack()

day_label = Label(window, font=('arial', 18))
day_label.pack()

date_label = Label(window, font=('arial', 20))
date_label.pack()

update()

window.mainloop()
