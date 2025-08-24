import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Login")
root.geometry("300x180")

# Use a frame for padding
frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

# Username
ttk.Label(frame, text="Username:").grid(row=0, column=0, sticky="w", pady=5)
username = ttk.Entry(frame, width=25)
username.grid(row=0, column=1, pady=5)

# Password
ttk.Label(frame, text="Password:").grid(row=1, column=0, sticky="w", pady=5)
password = ttk.Entry(frame, show="*", width=25)
password.grid(row=1, column=1, pady=5)

# Button
login_btn = ttk.Button(frame, text="Login")
login_btn.grid(row=2, column=0, columnspan=2, pady=15)

root.mainloop()
