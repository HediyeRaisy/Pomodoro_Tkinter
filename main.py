import tkinter
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
t = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(t)
    timer.config(text= "Timer", fg=GREEN)
    canvas.itemconfig(time,text = "00:00")
    global reps
    reps=0
    check.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    global reps
    reps += 1
    if reps % 2 == 0:
        if reps % 8 == 0:
            counting(long_break)
            timer.config(text="Break", fg=RED)
        else:
            counting(short_break)
            timer.config(text="Break",fg=PINK)
    else:
        counting(work)
        timer.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counting(count):
    sec = count%60
    min = int(count/60)
    if sec < 10:
        sec = "0"+str(sec)
    canvas.itemconfig(time,text=f"{min}:{sec}")
    if count > 0:
        global t
        t = window.after(1000,counting , count-1)
    else:
        start_timer()
        global reps
        text = "✔"
        string = ""
        if reps % 2 == 0:
            for i in range(0,int(reps/2)):
                string += text
            check.config(text= string)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50,padx=100,bg=YELLOW)
canvas = Canvas(width=200,height= 300,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file= "tomato.png")
canvas.create_image(100,150,image= tomato_img)
time = canvas.create_text(100,150,text= "00:00",fill="white",font=(FONT_NAME,35,"bold"))
# counting(60)
# canvas.create_text(100,15,text="TIMER",fill=GREEN,font=(FONT_NAME,50))
canvas.grid(row=1 , column=1)
# canvas.pack()
timer = Label(text="Timer",font=(FONT_NAME,50),bg=YELLOW,fg=GREEN)

timer.grid(row=0,column=1)
# timer.pack()

start = Button(text="Start",highlightbackground=YELLOW,fg="black",command= start_timer)
start.grid(row=2 , column=0)
stop = Button(text="Reset",highlightbackground=YELLOW,fg="black",command=reset_timer)
stop.grid(row=2 , column=2)
check = Label(font=(FONT_NAME,20),bg=YELLOW,fg=GREEN)
check.grid(row=3 , column=1)
window.mainloop()


