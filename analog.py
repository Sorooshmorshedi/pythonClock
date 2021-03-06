import tkinter as ui
import time
import math

window = ui.Tk()
window.title('soroosh Clock')
window.geometry("400x400")

def updateClock():
    hour = int(time.strftime('%I'))
    minute = int(time.strftime('%M'))
    sec = int(time.strftime('%S'))
    sec_x = sec_hand_len * math.sin(math.radians(sec * 6)) + center_x
    sec_y = -1 * sec_hand_len * math.cos(math.radians(sec * 6)) + center_y
    canvas.coords(sec_hand, center_x, center_y, sec_x, sec_y )

    minute_x = minute_hand_len * math.sin(math.radians(minute * 6)) + center_x
    minute_y= -1 * minute_hand_len * math.cos(math.radians(minute * 6)) + center_y
    canvas.coords(minute_hand, center_x, center_y, minute_x, minute_y )


    hour_x = hour_hand_len * math.sin(math.radians(hour * 30)) + center_x
    hour_y = -1 * hour_hand_len * math.cos(math.radians(hour * 30)) + center_y
    canvas.coords(hour_hand, center_x, center_y, hour_x, hour_y )

    window.after(1000, updateClock)


canvas = ui.Canvas(window, width=300, height=300, bg='black')
canvas.pack(expand=True, fill='both')

background = ui.PhotoImage(file='bg.png')
canvas.create_image(200, 200, image=background)

center_x = 200
center_y = 200
hour_hand_len = 60
minute_hand_len = 80
sec_hand_len = 95

sec_hand = canvas.create_line(200, 200, 200 + sec_hand_len , 200 + sec_hand_len, width=1.5 , fill='red')
minute_hand = canvas.create_line(200, 200, 200 + minute_hand_len , 200 + minute_hand_len, width=2, fill='white')
hour_hand = canvas.create_line(200, 200, 200 + hour_hand_len , 200 + hour_hand_len, width=2.5, fill='white')


updateClock()
window.mainloop()