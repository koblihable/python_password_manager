import tkinter as tk
from tkinter import END, messagebox
from tkinter import PhotoImage, StringVar
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list =[]
    password_list += [choice(letters) for i in range(randint(8, 10))]
    password_list += [choice(numbers) for i in range(randint(2, 4))]
    password_list += [choice(symbols) for i in range(randint(2, 4))]
    shuffle(password_list)

    password = ''.join(password_list)

    password_entry.insert(index=0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():

    email = email_entry.get()
    website = website_entry.get()
    password = password_entry.get()

    fields = {
        "email": len(email),
        "website": len(website),
        "password": len(password)
    }

    empty_fields = []

    for key in fields:
        if  fields[key] == 0:
            empty_fields.append(key)

    if len(empty_fields) > 0:
        is_ok = False
        message = f""
        for field in empty_fields:
            message += f"{field} cannot be empty\n"

        messagebox.showinfo(title="Aborting", message=message)

    else :
        is_ok = messagebox.askokcancel(title="Saving password", message=f"These are the details entered: \n"
                                                                f"Website: {website}\n"
                                                                f"Username: {email}\n"
                                                                f"Password: {password}\n"
                                                                f"Is it ok to save?")

        with open("data.txt", "a") as f:
            f.write(f"{website} | {email} | {password}\n")

        website_entry.delete(0, END)
        email_entry.delete(0, END)
        email_entry.insert(0, "lenka.koblih@gmail.com")
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas = tk.Canvas(width=250, height=250)
image = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=image)
canvas.grid(column=1, row=1)

website_label = tk.Label(text="Website")
website_label.config(font=("Courier", 12, "bold"), justify="center", width="15")
website_label.grid(row=2, column=0)

email_label = tk.Label(text="Email/Username")
email_label.config(font=("Courier", 12, "bold"), justify="center", width="15")
email_label.grid(row=3, column=0)

pw_label = tk.Label(text="Password")
pw_label.config(font=("Courier", 12, "bold"), justify="center", width="15")
pw_label.grid(row=4, column=0)

website_entry = tk.Entry(width=38, font=("Courier", 12), justify="left")
website_entry.focus()
website_entry.grid(row=2, column=1, columnspan=2)

email_entry = tk.Entry(width=38, font=("Courier", 12), justify="left")
email_entry.insert(0, "lenka.koblih@gmail.com")
email_entry.grid(row=3, column=1, columnspan=2)

password_entry = tk.Entry(width=25, font=("Courier", 12), justify="left")
password_entry.grid(row=4, column=1)

password_button = tk.Button(text="Generate Password", font=("Courier", 8), command=generate_password)
password_button.grid(row=4, column=2)

add_button = tk.Button(text="Add", width=36, font=("Courier", 12), justify="center", command=add_password)
add_button.grid(row=5, column=1, columnspan=2)




window.mainloop()


