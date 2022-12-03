from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text,text="00:00")
    Timer.config(text="TIMER")
    check_mark.config(text=" ")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN *60
    if reps % 8==0:
        Timer.config(text="Long Break",fg="red")
        count_down(long_break_sec)
    elif reps % 2 ==0:
        Timer.config(text="Short Break", fg="pink")
        count_down(short_break_sec)
    else:
        Timer.config(text="WORK", fg="green")
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec in range(0,10):
        count_sec = f"{0}{count_sec}"
    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=" "
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
            check_mark.config(text=mark )
# ---------------------------- UI SETUP ------------------------------- #
# setting window
window = Tk()
window.title("Pomodoro GUI")
window.config(padx=50,pady=50, bg=YELLOW)

# setting canvas
canvas = Canvas(width=202,height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas_text = canvas.create_text(100, 135,text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1,column=1)


Timer = Label(text="TIMER",bg=YELLOW, fg="green", font=(FONT_NAME,40, "bold"))
Timer.grid(row=0,column=1)

check_mark = Label(bg=YELLOW, fg="green", font=(FONT_NAME,18, "bold"))
check_mark.grid(row=3, column=1)

start_button = Button(text="Start", fg="black", relief=GROOVE,command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", fg="black", relief=GROOVE,command=timer_reset)
reset_button.grid(row=2, column=2)


window.mainloop()
