from tkinter import *

window=Tk()
window.title("Miles to Km")
window.minsize(width=500, height=200)
label = Label(text="Enter distance in miles : ",font=("Arial",15,"bold"))
label.place(x=20,y=20)


input=Entry(width=20)
input.insert(0, 0)
input.place(x=270,y=25)

mile=0
km=1.6*mile
label1=Label(text=f"{mile} miles in km is : {km}", font=("Arial",15,"bold"))
label1.place(x=15,y=100)

def btn_clicked():
    mile=float(input.get())
    km=1.6*mile
    label1["text"]=f"{mile} miles in km is : {km}"
    

submit=Button(text="Submit", width=52,command=btn_clicked)
submit.place(x=20,y=60)








window.mainloop()