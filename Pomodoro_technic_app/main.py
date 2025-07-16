import tkinter as tk
import time
# Constants
#--colors
PINK = "#FFA27F"
RED = "#FF0000"
GREEN = "#97BE5A"
YELLOW = "#FFE8C5"
#--text
FONT_NAME = "Courier-Bold"
#--time intervals
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Time reset

#Timer
def start_timer():
    '''
    :return: nothing
    call count_down() and set value of start time for timer
    '''
    count_down(5*60)

#Countdown
def count_down(count):
    '''
    :param count: int (milliseconds)
    :return: nothing
    set timer label of timer and change it every 1000 milliseconds
    '''
    count_min = count // 60
    count_sec = count % 60
    if count_min < 10:
        count_min = "0" + str(count_min)
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    time_set_text = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text, text=time_set_text)
    if count > 0:
        timer_window.after(1000, count_down, count-1)

#UI
#-- window settings
timer_window = tk.Tk()
timer_window.title("Pomodoro Timer")
timer_window.config(padx=10, pady=10, bg=YELLOW)


#-- background settings
canvas = tk.Canvas(timer_window, width=400, height=500, bg =YELLOW, highlightthickness=0)
tomato_tomer_img = tk.PhotoImage(file="timer.png")
tomato_tomer_img = tomato_tomer_img.subsample(2, 2)
canvas.create_image(200, 250, image=tomato_tomer_img)
timer_text = canvas.create_text(200, 306, text = "00:00", fill= "white", font=(FONT_NAME, 35,"normal"))
canvas.grid(column=1, row=1)


#-- widgets:
checkmark_label = tk.Label(timer_window, text="✔",font=(FONT_NAME, 15,"bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

start_btn = tk.Button(timer_window, text="START", command=start_timer)
start_btn.config(width=7, bg=PINK, fg='white',highlightthickness=0, font=(FONT_NAME, 12,"bold"), borderwidth=1)
start_btn.grid(column=1, row=2, sticky=tk.W)

reset_btn = tk.Button(timer_window, text="RESET", command=timer_window.destroy)
reset_btn.config(width=7, bg=PINK, fg='white',highlightthickness=0, font=(FONT_NAME, 12,"bold"), borderwidth=0)
reset_btn.grid(column=1, row=2,sticky=tk.E)

timer_window.mainloop()
