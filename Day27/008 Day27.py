
import tkinter
from tkinter import Entry

window =tkinter.Tk()
window.title("GUI Testing")
window.minsize(width=500,height=300)
window.config(padx=100, pady=200)

def button_clicked():
    print("I got clicked")
    new_text=input.get()
    my_label.config(text=new_text)

# Label
my_label=tkinter.Label(text="Hello and Welcome",font=("Arial",20,"bold"))
my_label["text"] ="new text"
my_label.config(text="Hello and Welcome")
my_label.grid(column=0,row=0)
my_label.config(padx=50,pady=50)

#Button
button =tkinter.Button(text="Click me",command=button_clicked)
button.grid(column=1,row=1)

#Entry
input= Entry(width=15)
print(input.get())
input.grid(column=3,row=3 )

new_button =tkinter.Button(text="Click me",command=button_clicked)
new_button.grid(column=2,row=0)



















window.mainloop()


