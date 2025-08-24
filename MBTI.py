import tkinter as tk
from tkinter import messagebox

class MBTITest:
    def __init__(self, root):
        self.root = root
        self.root.title("Full MBTI Personality Test")
        self.root.geometry("600x400")

        # Questions (text, option1, option2, pair)
        # pair indicates which MBTI dimension this question belongs to
        self.questions = [
            # E vs I
            ("You feel energized by social gatherings.", "Agree (E)", "Disagree (I)", "EI"),
            ("You enjoy starting conversations.", "Agree (E)", "Disagree (I)", "EI"),
            ("You prefer being the center of attention.", "Agree (E)", "Disagree (I)", "EI"),
            ("You need quiet time to recharge after socializing.", "Disagree (E)", "Agree (I)", "EI"),
            ("You think best while talking to others.", "Agree (E)", "Disagree (I)", "EI"),
            ("You are more talkative than reflective.", "Agree (E)", "Disagree (I)", "EI"),
            ("You enjoy large parties over quiet evenings.", "Agree (E)", "Disagree (I)", "EI"),
            ("You prefer deep one-on-one talks over group chats.", "Disagree (E)", "Agree (I)", "EI"),
            
            # S vs N
            ("You focus on details rather than big ideas.", "Agree (S)", "Disagree (N)", "SN"),
            ("You trust experience more than theory.", "Agree (S)", "Disagree (N)", "SN"),
            ("You enjoy practical tasks more than abstract ideas.", "Agree (S)", "Disagree (N)", "SN"),
            ("You often notice small details others miss.", "Agree (S)", "Disagree (N)", "SN"),
            ("You are more future-oriented than present-focused.", "Disagree (S)", "Agree (N)", "SN"),
            ("You prefer imagination over facts.", "Disagree (S)", "Agree (N)", "SN"),
            ("You are drawn to abstract theories.", "Disagree (S)", "Agree (N)", "SN"),
            ("You value creativity over tradition.", "Disagree (S)", "Agree (N)", "SN"),
            
            # T vs F
            ("You make decisions based on logic, not emotions.", "Agree (T)", "Disagree (F)", "TF"),
            ("You value truth over harmony.", "Agree (T)", "Disagree (F)", "TF"),
            ("You are more analytical than empathetic.", "Agree (T)", "Disagree (F)", "TF"),
            ("You are direct rather than tactful.", "Agree (T)", "Disagree (F)", "TF"),
            ("You put fairness before feelings.", "Agree (T)", "Disagree (F)", "TF"),
            ("You often prioritize compassion over logic.", "Disagree (T)", "Agree (F)", "TF"),
            ("You care more about people than efficiency.", "Disagree (T)", "Agree (F)", "TF"),
            ("You avoid conflict to keep peace.", "Disagree (T)", "Agree (F)", "TF"),
            
            # J vs P
            ("You prefer a planned schedule to spontaneity.", "Agree (J)", "Disagree (P)", "JP"),
            ("You like making lists and checking tasks off.", "Agree (J)", "Disagree (P)", "JP"),
            ("You dislike leaving decisions open-ended.", "Agree (J)", "Disagree (P)", "JP"),
            ("You like to have things decided early.", "Agree (J)", "Disagree (P)", "JP"),
            ("You are flexible and go with the flow.", "Disagree (J)", "Agree (P)", "JP"),
            ("You adapt quickly when plans change.", "Disagree (J)", "Agree (P)", "JP"),
            ("You find routines boring.", "Disagree (J)", "Agree (P)", "JP"),
            ("You prefer keeping options open.", "Disagree (J)", "Agree (P)", "JP"),
        ]

        self.answers = []
        self.current_q = 0

        # UI
        self.label = tk.Label(root, text="", font=("Arial", 14), wraplength=500)
        self.label.pack(pady=30)

        self.btn1 = tk.Button(root, text="", width=40, command=lambda: self.answer("opt1"))
        self.btn1.pack(pady=10)

        self.btn2 = tk.Button(root, text="", width=40, command=lambda: self.answer("opt2"))
        self.btn2.pack(pady=10)

        self.show_question()

    def show_question(self):
        q, opt1, opt2, _ = self.questions[self.current_q]
        self.label.config(text=f"Q{self.current_q+1}: {q}")
        self.btn1.config(text=opt1)
        self.btn2.config(text=opt2)

    def answer(self, choice):
        _, opt1, opt2, pair = self.questions[self.current_q]
        if choice == "opt1":
            self.answers.append((pair, opt1.split()[-1]))  # E/S/T/J
        else:
            self.answers.append((pair, opt2.split()[-1]))  # I/N/F/P

        self.current_q += 1
        if self.current_q < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        # Count letters
        counts = {"E":0,"I":0,"S":0,"N":0,"T":0,"F":0,"J":0,"P":0}
        for pair, letter in self.answers:
            counts[letter] += 1

        # Build MBTI type
        mbti = ""
        mbti += "E" if counts["E"] >= counts["I"] else "I"
        mbti += "S" if counts["S"] >= counts["N"] else "N"
        mbti += "T" if counts["T"] >= counts["F"] else "F"
        mbti += "J" if counts["J"] >= counts["P"] else "P"

        messagebox.showinfo("Your MBTI Result", f"✅ Your MBTI type is: {mbti}")
        self.root.quit()

# Run App
root = tk.Tk()
app = MBTITest(root)
root.mainloop()
