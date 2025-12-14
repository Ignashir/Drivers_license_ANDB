import tkinter as tk
from tkinter import messagebox

def save_credentials():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        try:
            with open("data.txt", "a") as file:
                file.write(f"Login: {username} | Password: {password}\n")
            
            entry_username.delete(0, tk.END)
            entry_password.delete(0, tk.END)
            
            messagebox.showinfo("Success", "Login saved to data.txt")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")
    else:
        messagebox.showwarning("Incomplete", "Please fill in both fields.")

# gui

root = tk.Tk()
root.title("Login Saver")
root.geometry("300x200")

label_username = tk.Label(root, text="Login:")
label_username.pack(pady=(20, 5))  

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

btn_submit = tk.Button(root, text="Submit", command=save_credentials)
btn_submit.pack(pady=20)

root.mainloop()