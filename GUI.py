from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=500)


label=Label(text="Sample label", font=('Arial',24,'bold'))
label["text"]="Hello"
label.grid(row=0,column=0) #.pack() places it on the screen

def btn_clicked():
    label["text"] = input.get()
button=Button(text="Click me" ,command=btn_clicked)
# button.pack(side="left")
button.grid(row=2,column=2)

button=Button(text="Click me" ,command=btn_clicked)
# button.pack(side="left")
button.grid(row=0,column=3)

input=Entry(width=15)
input.grid(row=3,column=4)


window.mainloop() #This ensures that the window is listening for user input
