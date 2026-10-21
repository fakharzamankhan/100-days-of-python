from tkinter import *
from tkinter import messagebox
from random import *
# import pyperclip
import json

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            search_email = data[website]['email']
            search_password = data[website]['password']
            messagebox.showinfo(title=website.title(), message=f"Email: {search_email}\nPassword: {search_password}")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    except KeyError:
        messagebox.showerror(title="Error", message="No details for the website exists")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    # pyperclip.copy(password)

    password_entry.insert(0, password)

def clear_info():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data ={
        website:{
            "email":email,
            "password":password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Labels
website_label=Label(text="Website:")
website_label.grid(column=0, row=1)
email_label=Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label=Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries
website_entry=Entry()
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry=Entry()
email_entry.grid(column=1, row=2)
email_entry.insert(0,"your_email@example.com")


password_entry=Entry()
password_entry.grid(column=1, row=3)

#Buttons
Generate_password=Button(text="Generate Password",command=generate_password)
Generate_password.grid(column=2, row=3)
add_button=Button(text="Add",width=35,command=save)
add_button.grid(row=6,column=1,columnspan=2)
search_button = Button(text="Search Website", command=find_password,width=13)
search_button.grid(row=1, column=2)
clear_button = Button(text="Clear Info", command=clear_info)
clear_button.grid(row=2, column=2)


window.mainloop()
