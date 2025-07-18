import tkinter as tk
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
cycle_count = 0
TIMER = None

#--Window size
WINDOW_WITH = 400
WINDOW_HEIGHT = 500

# Time reset
def timer_reset():
    '''
    reset timer function
    The function resets both the timer and session progres
    '''
    global TIMER
    global cycle_count
    timer_window.after_cancel(TIMER)
    checkmark_label['text'] = ""
    work_cycle_marker_label['text'] = "TIMER"
    canvas.itemconfig(timer_text, text="00:00")
    cycle_count =0
    start_btn['state'] = tk.NORMAL

#Timer
def start_timer():
    '''
    Call count_down() and set value of start time for timer
    The function sets work_cycle_marker_label depending on the number of cycles
    '''
    reset_btn['state'] = tk.NORMAL
    global cycle_count
    cycle_count += 1
    if cycle_count == 0 or cycle_count % 2 == 1:
        work_cycle_marker_label['text'] = "WORK"
        work_cycle_marker_label['fg'] = GREEN
        count_down(WORK_MIN*60)
    elif cycle_count % 2 == 0:
        work_cycle_marker_label['text'] = "BREAK"
        work_cycle_marker_label['fg'] = PINK
        count_down(SHORT_BREAK_MIN*60)
    elif cycle_count % 8 == 0:
        work_cycle_marker_label['text'] = "BREAK"
        work_cycle_marker_label['fg'] = RED
        count_down(LONG_BREAK_MIN*60)

#Countdown
def count_down(count):
    '''
    :param: count -> int (milliseconds)
    The function sets timer label of timer and change it every 1000 milliseconds,
    if the count is 0, the start_timer() is called and number of session checkmarks is increased
    '''
    global cycle_count
    global TIMER
    start_btn['state'] = tk.DISABLED
    count_min = count // 60
    count_sec = count % 60
    if count_min < 10:
        count_min = "0" + str(count_min)
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    time_set_text = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text, text=time_set_text)
    if count > 0:
        TIMER = timer_window.after(1000, count_down, count-1)
    if count == 0:
        start_timer()
        checkmark_label['text'] = (cycle_count // 2) * "✔"
        if cycle_count % 2 == 0:
            timer_window.state('normal')
            timer_window.lift()
            timer_window.attributes('-topmost', True)
        else:
            timer_window.attributes('-topmost', False)

#UI
#-- window settings
timer_window = tk.Tk()
timer_window.title("Pomodoro Timer")
timer_window.config(padx=10, pady=10, bg=YELLOW)


#-- background settings
canvas = tk.Canvas(timer_window, width=WINDOW_WITH, height=WINDOW_HEIGHT, bg =YELLOW, highlightthickness=0)
tomato_tomer_img = tk.PhotoImage(file="timer.png")
tomato_tomer_img = tomato_tomer_img.subsample(2, 2)
canvas.create_image(200, 250, image=tomato_tomer_img)

#timer label
timer_text = canvas.create_text(200, 306, text = "00:00", fill= "white", font=(FONT_NAME, 65,"normal"))
canvas.grid(column=1, row=1)


#-- widgets:
work_cycle_marker_label = tk.Label(timer_window, text="",font=(FONT_NAME, 20,"bold"),bg=YELLOW)
work_cycle_marker_label.grid(column=1, row=0)

checkmark_label = tk.Label(timer_window, text="",font=(FONT_NAME, 20,"bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

# start button setup
start_btn = tk.Button(timer_window, text="START", command=start_timer)
start_btn.config(width=7, bg=PINK, fg='white',highlightthickness=0, font=(FONT_NAME, 12,"bold"), borderwidth=1)
start_btn.grid(column=1, row=2, sticky=tk.W)

# reset button setup
reset_btn = tk.Button(timer_window, text="RESET", command=timer_reset)
reset_btn.config(width=7, bg=PINK, fg='white',highlightthickness=0, font=(FONT_NAME, 12,"bold"), borderwidth=0)
reset_btn['state'] = tk.DISABLED
reset_btn.grid(column=1, row=2,sticky=tk.E)


timer_window.mainloop()
