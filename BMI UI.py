import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("🏋️ BMI Calculator")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#1E1E1E")

           # --- Title ---
        tk.Label(
            root, text="Body Mass Index (BMI)", 
            font=("Segoe UI", 20, "bold"), bg="#1E1E1E", fg="white"
        ).pack(pady=20)

        # --- Weight Input ---
        tk.Label(root, text="Weight (kg):", bg="#1E1E1E", fg="#DADADA", font=("Segoe UI", 12)).pack()
        self.weight_entry = tk.Entry(root, font=("Segoe UI", 14), bg="#2C2C2C", fg="white", bd=0, justify="center")
        self.weight_entry.pack(pady=10, ipady=5)

         # --- Height Input ---
        tk.Label(root, text="Height (cm):", bg="#1E1E1E", fg="#DADADA", font=("Segoe UI", 12)).pack()
        self.height_entry = tk.Entry(root, font=("Segoe UI", 14), bg="#2C2C2C", fg="white", bd=0, justify="center")
        self.height_entry.pack(pady=10, ipady=5)

        # --- Calculate Button ---
        calc_button = tk.Button(
            root, text="Calculate BMI", command=self.calculate_bmi,
            font=("Segoe UI", 14, "bold"), bg="#00A8E8", fg="white",
            activebackground="#007EA7", activeforeground="white", bd=0, width=18, height=2
        )
        calc_button.pack(pady=20)

        # --- Result Display ---
        self.result_label = tk.Label(root, text="", bg="#1E1E1E", fg="white", font=("Segoe UI", 16, "bold"))
        self.result_label.pack(pady=10)

        # --- Category Label ---
        self.category_label = tk.Label(root, text="", bg="#1E1E1E", fg="#B0BEC5", font=("Segoe UI", 14))
        self.category_label.pack(pady=5)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height_cm = float(self.height_entry.get())
            height_m = height_cm / 100

            bmi = round(weight / (height_m ** 2), 2)
            self.result_label.config(text=f"Your BMI: {bmi}")

            # Determine category
            if bmi < 18.5:
                category = "Underweight 😕"
                color = "#F39C12"
            elif 18.5 <= bmi < 24.9:
                category = "Normal ✅"
                color = "#2ECC71"
            elif 25 <= bmi < 29.9:
                category = "Overweight ⚠️"
                color = "#F1C40F"
            else:
                category = "Obese 🚨"
                color = "#E74C3C"

            self.category_label.config(text=f"Category: {category}", fg=color)

        except ValueError:
            messagebox.showwarning("Input Error", "Please enter valid numbers for height and weight!")

if __name__ == "__main__":
    root = tk.Tk()
    BMICalculator(root)
    root.mainloop()
