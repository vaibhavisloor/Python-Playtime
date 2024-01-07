from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=500)


label=Label(text="Sample label", font=('Arial',24,'bold'))
label.pack() #.pack() places it on the screen
label["text"]="Hello"

button=Button(text="Click me")
# button.pack(side="left")
button.pack()

window.mainloop() #This ensures that the window is listening for user input
