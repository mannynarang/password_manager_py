import tkinter
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
import pandas as pd
import random

info_list = []
window = tkinter.Tk()
window.title("Password Manager")

window.config(pady=40, padx=40)
canvas = tkinter.Canvas(width=200, height=200)
image = tkinter.PhotoImage(file="logo.png", )
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1, sticky="W")

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = tkinter.Entry(width=34)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2, sticky="W")
email_input = tkinter.Entry(width=43)
email_input.grid(row=2, column=1, columnspan=2, sticky="W")
email_input.insert(0, "manny@email.com")
password_input = tkinter.Entry(width=24)
password_input.grid(row=3, column=1, sticky="W")


def search():
    try:
        with open("data.json", mode="r") as file_data:
            data = json.load(file_data)

        # result ={key:value for (key,value) in data.items() if value="manny"}
    except FileNotFoundError:
        tkinter.messagebox.showinfo(title="info", message="No saved passwords")
    else:
        print(data)

        try:
            website = website_input.get()
            email = email_input.get()
            lookup = data[website]
            pw = [lookup['password'] for key, value in lookup.items() if value == email]
            empty = []
            if pw == empty:
                print("data not found")
                tkinter.messagebox.showinfo(title="Password info", message="Password not found")
            else:
                tkinter.messagebox.showinfo(title="Password info", message="".join(pw))
        except KeyError:
            tkinter.messagebox.showinfo(title="Password info", message="Password not found")


def save_info():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email,
            "password": password,

        }
    }

    if len(website) != 0 and len(email) != 0 and len(password) != 0:

        ok = tkinter.messagebox.askokcancel(title=website,
                                            message=f"These are the details you have entered: \nEmail:{email}"
                                                    f"\nPassword:{password} ")

        if ok:
            # df = pd.DataFrame([website, email, password],
            #
            #                   index=["Website", "Email", "Password"], columns=["Category"])
            # df.to_csv("info.txt", mode="a")
            # website_input.delete(0, tkinter.END)
            # password_input.delete(0, tkinter.END)
            try:
                with open("data.json", mode="r") as data_file:
                    # reading old data
                    data = json.load(data_file)
                    # updating old data with new data

            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    # writing new data
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", mode="w") as data_file:
                    data.update(new_data)
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, tkinter.END)
                password_input.delete(0, tkinter.END)
                # print(data)
                # print(data['amazon']['email'])

    else:
        tkinter.messagebox.showwarning(title="Warning", message="You can not leave any field empty")


def password_gen():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_input.insert(0, f"{password}")
    pyperclip.copy(password)
    print(f"Your password is: {password_list}")


generate_password = tkinter.Button(text="Generate Password", command=password_gen)
generate_password.grid(row=3, column=1, sticky="E")
search = tkinter.Button(text="Search", command=search)
search.grid(row=1, column=1, sticky="E")

add_button = tkinter.Button(text="Add", width=36, command=save_info)
add_button.grid(row=4, column=1, sticky="W")

window.mainloop()
