import tkinter as tk
import pyperclip
from tkinter import messagebox
from string import ascii_letters
from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = list(ascii_letters)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '^', '&', '(', ')', '*', '+', '=']

def generate_a_password():
    password_entry.delete(0, tk.END)
    password_symbols = []
    [password_symbols.append(choice(letters)) for _ in range(randint(7, 12))]
    [password_symbols.append(choice(numbers)) for _ in range(randint(3, 8))]
    [password_symbols.append(choice(symbols)) for _ in range(randint(3, 8))]
    shuffle(password_symbols)
    password = "".join(password_symbols)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def safe_data_to_file():
    website_name = website_name_entry.get()
    user_email = email_name_entry.get()
    password = password_entry.get()
    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo(title='Ooops', message='Please don\'t leave any fields empty')
    else:
        is_true = messagebox.askokcancel(title=website_name, message=f"These are the details entered: "
                                                                     f"\nEmail: {user_email} \nPassword: {password} \nIs it ok to save?")
        if is_true:
            with open('sensitive_data.txt', 'a') as sensitive_data:
                sensitive_data.write(f"{website_name} | {user_email} | {password}\n")
                website_name_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #
manager_window = tk.Tk()
manager_window.title("Password Manager")
manager_window.config(padx=20, pady=20)
canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#labels
website_name_label = tk.Label(text="Website:")

website_name_label.grid(row=1, column=0, sticky=tk.E)

email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky=tk.E)

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0, sticky=tk.E)

#Entryes
website_name_entry = tk.Entry(width=57)
website_name_entry.grid(row=1, column=1, columnspan=2, sticky=tk.W)
website_name_entry.focus()

email_name_entry = tk.Entry(width=57)
email_name_entry.grid(row=2, column=1, columnspan=2, sticky=tk.W)
email_name_entry.insert(0, "<EMAIL>")

password_entry = tk.Entry(width=34)
password_entry.grid(row=3, column=1, sticky=tk.W)

#Buttons
generate_password_button = tk.Button(text="Generate Password",width=17, command=generate_a_password)
generate_password_button.grid(row=3, column=2, columnspan=2, sticky=tk.W)

add_password_button = tk.Button(text="Add",command=safe_data_to_file)
add_password_button.config(width=48)
add_password_button.grid(row=4, column=1, columnspan=2)
manager_window.mainloop()