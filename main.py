from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint
import pyperclip
import json


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_name = website_entry.get()

    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)


    except FileNotFoundError:
        messagebox.showerror("Error", "No Data File Found")

    else:
        if website_name in data:
            email = data[website_name]["email"]
            password = data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Email: {email}\nPassword: {password} ")
        else:
            messagebox.showerror("Error", f"No details for {website_name} exists.")

    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    # Şifreyi oluşturduğumuzda direk cursorda görünmesi için bunu kullandık
    pyperclip.copy(password)
    pyperclip.paste()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty! ")
    else:
        try:
            with open(file="data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open(file="data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with adding new data
            data.update(new_data)

            with open(file="data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Creating Canvas
canvas = Canvas(width=200, height=200)
key_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=key_image)
canvas.grid(column=1, row=0)

# Website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# user_name label
user_name_label = Label(text="Email/Surname:")
user_name_label.grid(column=0, row=2)

# password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Website Entry
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

# email Entry
email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)


# password Entry
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Generate Password Button
generate_password_button = Button(text="Generate Password", command=generate_password, width=13)
generate_password_button.grid(row=3, column=2)

# Add Button
add_button = Button(text="Add", width=37, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Search Button
generate_password_button = Button(text="Search", command=find_password, width=13)
generate_password_button.grid(row=1, column=2)


window.mainloop()