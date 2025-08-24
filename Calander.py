import tkinter as tk
from tkinter import messagebox
import calendar
from datetime import datetime

class MiniCalendar:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Calendar")

        self.today = datetime.today()
        self.current_year = self.today.year
        self.current_month = self.today.month

        # Header: Month and Year
        self.header_label = tk.Label(root, font=("Arial", 16, "bold"))
        self.header_label.grid(row=0, column=1, columnspan=5, pady=5)

        # Navigation buttons
        tk.Button(root, text="<", command=self.prev_month, width=5).grid(row=0, column=0)
        tk.Button(root, text=">", command=self.next_month, width=5).grid(row=0, column=6)

        # Frame for calendar
        self.calendar_frame = tk.Frame(root)
        self.calendar_frame.grid(row=1, column=0, columnspan=7, padx=10, pady=10)

        self.draw_calendar()

    def draw_calendar(self):
        # Clear previous calendar
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        cal = calendar.Calendar(firstweekday=6)
        month_days = cal.monthdayscalendar(self.current_year, self.current_month)

        # Weekday headers
        days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for i, day in enumerate(days):
            tk.Label(self.calendar_frame, text=day, font=("Arial", 12, "bold")).grid(row=0, column=i, padx=5, pady=5)

        # Days
        for r, week in enumerate(month_days, start=1):
            for c, day in enumerate(week):
                if day == 0:
                    tk.Label(self.calendar_frame, text="", width=4, height=2).grid(row=r, column=c)
                else:
                    bg_color = "white"
                    fg_color = "black"

                    # Highlight today
                    if (day == self.today.day and
                        self.current_month == self.today.month and
                        self.current_year == self.today.year):
                        bg_color = "lightgreen"

                    # Weekends
                    if c == 0 or c == 6:
                        fg_color = "red"

                    day_btn = tk.Button(self.calendar_frame, text=str(day), width=4, height=2,
                                        bg=bg_color, fg=fg_color,
                                        command=lambda d=day: self.day_clicked(d))
                    day_btn.grid(row=r, column=c, padx=2, pady=2)

        # Update header
        self.header_label.config(text=f"{calendar.month_name[self.current_month]} {self.current_year}")

    def day_clicked(self, day):
        messagebox.showinfo("Selected Day", f"You clicked: {day}/{self.current_month}/{self.current_year}")

    def prev_month(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.draw_calendar()

    def next_month(self):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.draw_calendar()

# Run the app
root = tk.Tk()
app = MiniCalendar(root)
root.mainloop()
