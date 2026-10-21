import tkinter
from tkinter import Entry

window =tkinter.Tk()
window.title("GUI Testing")
window.minsize(width=500,height=300)

# Label

my_label=tkinter.Label(text="Hello and Welcome",font=("Arial",20,"bold"))
my_label.pack()

my_label["text"] ="new text"
my_label.config(text="Hello and Welcome")


#Buttton
def button_clicked():
    print("I got clicked")
    new_text=input.get()
    my_label.config(text=new_text)



button =tkinter.Button(text="Click me",command=button_clicked)
button.pack()


#Entry

input= Entry(width=15)
input.pack()
print(input.get())










window.mainloop()


