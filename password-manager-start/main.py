from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- 

def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(6)]
    password_symbols = [random.choice(symbols) for _ in range(3)]
    password_numbers = [random.choice(numbers) for _ in range(3)]

    list  = password_letters+password_symbols+password_numbers
    random.shuffle(list)

    final_password = "".join(list)
    password_entry.delete(0,END)
    password_entry.insert(0,final_password)
     
# ---------------------------- SAVE PASSWORD ------------------------------- 
    
def save_information():
        if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0 :
              messagebox.showwarning(title="Required fields",message="Please dont leave any fields empty")
        else:      
            ok_bool = messagebox.askokcancel(title="Confirm your details",message=f"Website : {website_entry.get()}\nEmail : {email_entry.get()}\nPassword : {password_entry.get()}")
            if ok_bool == 1:
                with open("database.txt","a") as file:
                    file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
                    website_entry.delete(0,END)
                    password_entry.delete(0,END)

#---------------------------- UI SETUP ------------------------------- 

window =Tk()
window.title("Password Generator")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100,112,image=password_image)
canvas.grid(row=0,column=1)

website_label=Label(text="Website")
website_label.grid(row=1,column=0)
Email_label=Label(text="Email")
Email_label.grid(row=2,column=0)
Password_label=Label(text="Password")
Password_label.grid(row=3,column=0)

website_entry = Entry(width=50)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=50)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"viisloor@gmail.com")
password_entry = Entry(width=31)
password_entry.grid(row=3,column=1)

generate_password_button=Button(text="Generate password",width=15,command=gen_pass)
generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add",width=42,command=save_information)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()