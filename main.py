import tkinter as ui
import time

window = ui.Tk()
window.title('soroosh Clock')

def updateClock():
    hour = time.strftime('%I')
    minute = time.strftime('%M')
    sec = time.strftime('%S')
    am_or_pm = time.strftime('%p')
    time_text = hour + ':' + minute + ':' + sec + ' ' + am_or_pm
    clock_label.config(text=time_text)
    clock_label.after(1000, updateClock)


clock_label = ui.Label(window, text='00:00:00', font='Helvetica 72 bold',
                       fg='green', bg='black',pady=10, padx=10,)

clock_label.pack()
updateClock()
window.mainloop()