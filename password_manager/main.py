import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

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

email_name_entry = tk.Entry(width=57)
email_name_entry.grid(row=2, column=1, columnspan=2, sticky=tk.W)

password_entry = tk.Entry(width=34)
password_entry.grid(row=3, column=1, sticky=tk.W)

#Buttons
generate_password_button = tk.Button(text="Generate Password",width=17)
generate_password_button.grid(row=3, column=2, columnspan=2, sticky=tk.W)

add_password_button = tk.Button(text="Add")
add_password_button.config(width=48)
add_password_button.grid(row=4, column=1, columnspan=2)
manager_window.mainloop()