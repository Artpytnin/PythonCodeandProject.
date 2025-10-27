import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext

# -----------------------------
# 📝 ฟังก์ชันพื้นฐาน
# -----------------------------
def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Untitled - Notepad")

def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        root.title(f"{file_path} - Notepad")

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"{file_path} - Notepad")
        messagebox.showinfo("Saved", "File saved successfully!")

def exit_app():
    if messagebox.askokcancel("Exit", "Do you really want to quit?"):
        root.destroy()

# -----------------------------
# ✏️ UI หลักของแอป
# -----------------------------
root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("800x600")
root.config(bg="#f0f0f0")

# สร้างพื้นที่พิมพ์ข้อความ
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, undo=True, font=("Consolas", 14))
text_area.pack(expand=True, fill='both', padx=5, pady=5)

# -----------------------------
# 🧭 แถบเมนูด้านบน
# -----------------------------
menu_bar = tk.Menu(root)

# เมนู File
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# เมนู Edit
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=text_area.edit_undo)
edit_menu.add_command(label="Redo", command=text_area.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: text_area.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: text_area.event_generate("<<Paste>>"))
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# เมนู Help
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Python Notepad v1.0\nBy Art"))
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

# -----------------------------
# 🚀 เริ่มต้นโปรแกรม
# -----------------------------
root.mainloop()
