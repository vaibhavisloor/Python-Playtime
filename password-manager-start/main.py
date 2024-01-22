from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- 

# ---------------------------- SAVE PASSWORD ------------------------------- 

#---------------------------- UI SETUP ------------------------------- 

window =Tk()
window.title("Password Generator")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100,112,image=password_image)
canvas.pack()

window.mainloop()