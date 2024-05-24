BACKGROUND_COLOR = "#B1DDC6"


from tkinter import *
import pandas as pd
import random
import time

global a,b

def get_word():
    global a,b
    global flip_timer
    window.after_cancel(flip_timer)
    data=pd.read_csv("./data/french_words.csv")
    num=random.randint(0,data.shape[0]-1)
    a,b=data.iloc[num].values
    canvas.itemconfig(background_image,image=my_image)
    canvas.itemconfig(title_txt,text="French",fill="black")
    canvas.itemconfig(word_txt,text=a,fill="black")
    flip_timer=window.after(3000,func=get_meaning)


def get_meaning():
    global a,b
    canvas.itemconfig(title_txt,text="English",fill='white')
    canvas.itemconfig(word_txt,text=b,fill="white")
    canvas.itemconfig(background_image,image=back_image)



window=Tk()
window.title("Flashy")
window.config(padx=20,pady=20,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=get_meaning)

canvas=Canvas(width=790,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)

my_image=PhotoImage(file="./images/card_front.png")
back_image=PhotoImage(file="./images/card_back.png")

background_image = canvas.create_image(400,263,image=my_image)
title_txt = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
word_txt = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

check=PhotoImage(file="./images/right.png")
button=Button(image=check,highlightthickness=0,command=get_word)
button.grid(row=1,column=1)
wrong=PhotoImage(file="./images/wrong.png")
button1=Button(image=wrong,highlightthickness=0,command=get_word)
button1.grid(row=1,column=0)

get_word()

window.mainloop()
