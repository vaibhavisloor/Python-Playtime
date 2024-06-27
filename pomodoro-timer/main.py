from tkinter import *
import math
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer_instance=None


# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
     window.after_cancel(timer_instance)
     canvas.itemconfig(timer_text,text="00:00")
     label1.config(text="Timer")
     check_marks.config(text="")
     
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer(repetitions=1):
        if repetitions % 2 != 0:
            time_sec = WORK_MIN * 60
            label1.config(text="Work",fg=GREEN)
        elif repetitions % 2 == 0:
            time_sec = SHORT_BREAK_MIN * 60
            label1.config(text="Break",fg=RED)
        elif repetitions == 8:
            time_sec = LONG_BREAK_MIN * 60
            label1.config(text="Break",fg=PINK)
        timer(time_sec, repetitions)

# ---------------------------- COUNTDOWN MECHANISM -------------------------------     
def timer(count,repetitions):
    mark=""
    count_mins = count/60
    count_sec = count % 60
    text = f"{str(math.floor(count_mins)).zfill(2)}:{str(count_sec).zfill(2)}"
    canvas.itemconfig(timer_text, text=text)
    if int(count) > 0: 
        global timer_instance
        timer_instance = window.after(1000,timer,count-1,repetitions)
    else:
        window.after(1000, start_timer, repetitions + 1)
        work_sessions = int(repetitions/2)
        for _ in range(work_sessions):
            mark+="✔"
        check_marks.config(text=mark)    
       
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

label1 = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,40,"bold"))
label1.grid(row=0,column=1)

canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="G:/Python-Playtime/pomodoro-timer/tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

start_button = Button(text="start",font=(FONT_NAME),highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)

check_marks = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20))
check_marks.grid(row=3,column=1)

reset_button = Button(text="restart",font=(FONT_NAME),highlightthickness=0,command=timer_reset)
reset_button.grid(row=2,column=2)





window.mainloop()