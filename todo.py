import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
from datetime import datetime
from typing import List, Dict, Optional
import uuid

class ModernButton(tk.Canvas):
    """Custom 3D-style button with gradient effects"""
    
    def __init__(self, parent, text, command=None, bg_color="#4A90E2", 
                 fg_color="white", width=120, height=40, **kwargs):
        super().__init__(parent, width=width, height=height, 
                        highlightthickness=0, bg=parent["bg"], **kwargs)
        
        self.text = text
        self.command = command
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.width = width
        self.height = height
        self.is_pressed = False
        
        self.create_3d_button()
        self.bind("<Button-1>", self.on_press)
        self.bind("<ButtonRelease-1>", self.on_release)
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)
        
    def create_3d_button(self):
        """Create 3D button effect with gradients"""
        self.delete("all")
        
        # Create gradient background
        for i in range(self.height):
            color_intensity = 1 - (i / self.height) * 0.3
            color = self.adjust_brightness(self.bg_color, color_intensity)
            self.create_line(0, i, self.width, i, fill=color, width=1)
        
        # Add 3D border effects
        if not self.is_pressed:
            # Top highlight
            self.create_line(0, 0, self.width, 0, fill="white", width=2)
            self.create_line(0, 0, 0, self.height, fill="white", width=2)
            # Bottom shadow
            self.create_line(self.width-1, 0, self.width-1, self.height, 
                           fill="black", width=2, stipple="gray50")
            self.create_line(0, self.height-1, self.width, self.height-1, 
                           fill="black", width=2, stipple="gray50")
        else:
            # Pressed effect
            self.create_line(0, 0, self.width, 0, fill="black", width=2, stipple="gray50")
            self.create_line(0, 0, 0, self.height, fill="black", width=2, stipple="gray50")
        
        # Add text
        self.create_text(self.width//2, self.height//2, text=self.text, 
                        fill=self.fg_color, font=("Segoe UI", 10, "bold"))
    
    def adjust_brightness(self, color, factor):
        """Adjust color brightness"""
        # Convert hex to RGB
        color = color.lstrip('#')
        rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        
        # Adjust brightness
        new_rgb = tuple(int(min(255, max(0, c * factor))) for c in rgb)
        
        # Convert back to hex
        return f"#{new_rgb[0]:02x}{new_rgb[1]:02x}{new_rgb[2]:02x}"
    
    def on_press(self, event):
        self.is_pressed = True
        self.create_3d_button()
        
    def on_release(self, event):
        self.is_pressed = False
        self.create_3d_button()
        if self.command:
            self.command()
            
    def on_hover(self, event):
        self.config(cursor="hand2")
        # Slightly brighten the button
        bright_color = self.adjust_brightness(self.bg_color, 1.1)
        self.bg_color = bright_color
        self.create_3d_button()
        
    def on_leave(self, event):
        self.config(cursor="")
        # Restore original color
        self.bg_color = self.adjust_brightness(self.bg_color, 0.9)
        self.create_3d_button()

class TaskCard(tk.Frame):
    """Modern 3D task card with interactive elements"""
    
    def __init__(self, parent, task_data, app, **kwargs):
        super().__init__(parent, **kwargs)
        self.task_data = task_data
        self.app = app
        self.is_completed = task_data.get('completed', False)
        
        self.configure(bg=parent["bg"], padx=5, pady=5)
        self.create_card()
    
    def create_card(self):
        """Create 3D card with modern styling"""
        # Card background with gradient effect
        self.card_canvas = tk.Canvas(self, width=500, height=80, 
                                   highlightthickness=0, bg=self["bg"])
        self.card_canvas.pack(fill="both", expand=True)
        
        # Create card background
        self.draw_card_background()
        
        # Task content
        self.create_task_content()
        
        # Bind click events
        self.card_canvas.bind("<Button-1>", self.on_card_click)
        self.bind("<Button-1>", self.on_card_click)
    
    def draw_card_background(self):
        """Draw 3D card background"""
        priority_colors = {
            'high': '#FF6B6B',
            'medium': '#FFD93D', 
            'low': '#6BCF7F'
        }
        
        base_color = priority_colors.get(self.task_data.get('priority', 'medium'), '#4A90E2')
        
        # Create gradient effect
        for i in range(80):
            color_intensity = 1 - (i / 80) * 0.2
            color = self.adjust_brightness(base_color, color_intensity)
            self.card_canvas.create_line(0, i, 500, i, fill=color, width=1)
        
        # Add 3D border
        if not self.is_completed:
            # Top and left highlights
            self.card_canvas.create_line(0, 0, 500, 0, fill="white", width=2)
            self.card_canvas.create_line(0, 0, 0, 80, fill="white", width=2)
            # Bottom and right shadows
            self.card_canvas.create_line(499, 0, 499, 80, fill="black", width=2, stipple="gray50")
            self.card_canvas.create_line(0, 79, 500, 79, fill="black", width=2, stipple="gray50")
        else:
            # Completed state - more subdued
            self.card_canvas.create_rectangle(2, 2, 498, 78, outline="#ccc", width=1)
    
    def create_task_content(self):
        """Create task text and controls"""
        # Checkbox
        checkbox_color = "#4A90E2" if not self.is_completed else "#ccc"
        self.checkbox = self.card_canvas.create_oval(15, 25, 45, 55, 
                                                   outline=checkbox_color, width=3)
        
        if self.is_completed:
            # Draw checkmark
            self.card_canvas.create_line(20, 40, 30, 50, fill="#4A90E2", width=3)
            self.card_canvas.create_line(30, 50, 40, 30, fill="#4A90E2", width=3)
        
        # Task text
        text_color = "#333" if not self.is_completed else "#999"
        font_style = ("Segoe UI", 12, "normal" if not self.is_completed else "italic")
        
        task_text = self.task_data.get('text', '')
        if len(task_text) > 50:
            task_text = task_text[:47] + "..."
        
        self.text_item = self.card_canvas.create_text(60, 25, text=task_text, 
                                                     fill=text_color, font=font_style, anchor="w")
        
        # Priority indicator
        priority = self.task_data.get('priority', 'medium')
        priority_colors = {'high': '#FF6B6B', 'medium': '#FFD93D', 'low': '#6BCF7F'}
        priority_text = {'high': 'HIGH', 'medium': 'MED', 'low': 'LOW'}
        
        self.priority_rect = self.card_canvas.create_rectangle(60, 40, 120, 60, 
                                                           fill=priority_colors[priority], 
                                                           outline="", radius=10)
        self.priority_text = self.card_canvas.create_text(90, 50, text=priority_text[priority], 
                                                         fill="white", font=("Segoe UI", 8, "bold"))
        
        # Action buttons
        if not self.is_completed:
            self.edit_btn = self.card_canvas.create_text(450, 30, text="✏️", font=("Segoe UI", 14))
            self.delete_btn = self.card_canvas.create_text(480, 30, text="🗑️", font=("Segoe UI", 14))
            
            self.card_canvas.tag_bind(self.edit_btn, "<Button-1>", self.on_edit)
            self.card_canvas.tag_bind(self.delete_btn, "<Button-1>", self.on_delete)
        
        # Date
        created_date = self.task_data.get('createdAt', '')
        if created_date:
            try:
                date_obj = datetime.fromisoformat(created_date.replace('Z', '+00:00'))
                date_str = date_obj.strftime("%b %d")
                self.card_canvas.create_text(450, 60, text=date_str, fill="#666", 
                                           font=("Segoe UI", 9), anchor="e")
            except:
                pass
    
    def adjust_brightness(self, color, factor):
        """Adjust color brightness"""
        color = color.lstrip('#')
        rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        new_rgb = tuple(int(min(255, max(0, c * factor))) for c in rgb)
        return f"#{new_rgb[0]:02x}{new_rgb[1]:02x}{new_rgb[2]:02x}"
    
    def on_card_click(self, event):
        """Handle card click - toggle completion"""
        # Check if click is on checkbox area
        if 15 <= event.x <= 45 and 25 <= event.y <= 55:
            self.app.toggle_task(self.task_data['id'])
    
    def on_edit(self, event):
        """Handle edit button click"""
        self.app.edit_task(self.task_data['id'])
    
    def on_delete(self, event):
        """Handle delete button click"""
        self.app.delete_task(self.task_data['id'])

class ModernTodoApp:
    """Main application class"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Modern 3D To-Do List")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        # Configure window
        self.root.minsize(600, 500)
        
        # Task storage
        self.tasks = []
        self.current_filter = "all"
        self.editing_task_id = None
        
        # Create UI
        self.setup_ui()
        
        # Load saved tasks
        self.load_tasks()
        
        # Start main loop
        self.root.mainloop()
    
    def setup_ui(self):
        """Setup modern UI with 3D effects"""
        # Header with gradient
        self.create_header()
        
        # Input section
        self.create_input_section()
        
        # Filter buttons
        self.create_filter_section()
        
        # Stats section
        self.create_stats_section()
        
        # Task list area
        self.create_task_list()
        
        # Scrollbar
        self.create_scrollbar()
    
    def create_header(self):
        """Create modern header with 3D effect"""
        header_frame = tk.Frame(self.root, height=80, bg="#2C3E50")
        header_frame.pack(fill="x", padx=10, pady=(10, 5))
        header_frame.pack_propagate(False)
        
        # Header canvas for 3D effect
        header_canvas = tk.Canvas(header_frame, bg="#2C3E50", highlightthickness=0)
        header_canvas.pack(fill="both", expand=True)
        
        # Create gradient header
        for i in range(80):
            color_intensity = 1 - (i / 80) * 0.3
            r = int(44 * color_intensity)
            g = int(62 * color_intensity)
            b = int(80 * color_intensity)
            color = f"#{r:02x}{g:02x}{b:02x}"
            header_canvas.create_line(0, i, 800, i, fill=color, width=1)
        
        # Title
        header_canvas.create_text(400, 40, text="🎯 Modern To-Do List", 
                                fill="white", font=("Segoe UI", 24, "bold"))
        
        # Add 3D border
        header_canvas.create_line(0, 0, 800, 0, fill="#34495E", width=2)
        header_canvas.create_line(0, 79, 800, 79, fill="#1A252F", width=2)
    
    def create_input_section(self):
        """Create input section with modern styling"""
        input_frame = tk.Frame(self.root, bg="#ECF0F1", height=100)
        input_frame.pack(fill="x", padx=10, pady=5)
        input_frame.pack_propagate(False)
        
        # Input canvas for 3D effect
        input_canvas = tk.Canvas(input_frame, bg="#ECF0F1", highlightthickness=0)
        input_canvas.pack(fill="both", expand=True)
        
        # Create card-like background
        input_canvas.create_rectangle(10, 10, 780, 90, fill="white", outline="#BDC3C7", width=2)
        input_canvas.create_line(10, 10, 780, 10, fill="white", width=2)
        input_canvas.create_line(10, 10, 10, 90, fill="white", width=2)
        input_canvas.create_line(780, 10, 780, 90, fill="#95A5A6", width=2, stipple="gray50")
        input_canvas.create_line(10, 90, 780, 90, fill="#95A5A6", width=2, stipple="gray50")
        
        # Input field
        self.task_input = tk.Entry(input_frame, font=("Segoe UI", 14), bd=0, 
                                 bg="white", fg="#2C3E50", width=40)
        self.task_input.place(x=30, y=30)
        
        # Priority selector
        self.priority_var = tk.StringVar(value="medium")
        priority_frame = tk.Frame(input_frame, bg="white")
        priority_frame.place(x=450, y=25)
        
        tk.Label(priority_frame, text="Priority:", bg="white", 
                font=("Segoe UI", 12), fg="#2C3E50").pack(side="left", padx=5)
        
        priorities = [("High", "high", "#E74C3C"), ("Medium", "medium", "#F39C12"), ("Low", "low", "#27AE60")]
        for text, value, color in priorities:
            rb = tk.Radiobutton(priority_frame, text=text, variable=self.priority_var, 
                              value=value, bg="white", fg=color, font=("Segoe UI", 10))
            rb.pack(side="left", padx=5)
        
        # Add button
        self.add_button = ModernButton(input_frame, "Add Task", self.add_task, 
                                     bg_color="#3498DB", width=120, height=35)
        self.add_button.place(x=650, y=30)
        
        # Bind enter key
        self.task_input.bind("<Return>", lambda e: self.add_task())
    
    def create_filter_section(self):
        """Create filter buttons with modern styling"""
        filter_frame = tk.Frame(self.root, bg="#f0f0f0", height=50)
        filter_frame.pack(fill="x", padx=10, pady=5)
        filter_frame.pack_propagate(False)
        
        # Filter buttons
        self.filter_buttons = {}
        filters = [("All Tasks", "all", "#3498DB"), ("Active", "active", "#E67E22"), 
                  ("Completed", "completed", "#27AE60")]
        
        for i, (text, filter_type, color) in enumerate(filters):
            btn = ModernButton(filter_frame, text, lambda f=filter_type: self.set_filter(f), 
                             bg_color=color, width=100, height=30)
            btn.pack(side="left", padx=10)
            self.filter_buttons[filter_type] = btn
    
    def create_stats_section(self):
        """Create statistics section"""
        stats_frame = tk.Frame(self.root, bg="#f0f0f0", height=40)
        stats_frame.pack(fill="x", padx=10, pady=5)
        stats_frame.pack_propagate(False)
        
        self.stats_label = tk.Label(stats_frame, text="Total: 0 | Completed: 0", 
                                  bg="#f0f0f0", fg="#2C3E50", font=("Segoe UI", 12))
        self.stats_label.pack(side="left", padx=20)
    
    def create_task_list(self):
        """Create scrollable task list area"""
        list_frame = tk.Frame(self.root, bg="#f0f0f0")
        list_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Canvas for tasks
        self.task_canvas = tk.Canvas(list_frame, bg="#f0f0f0", highlightthickness=0)
        self.task_canvas.pack(side="left", fill="both", expand=True)
        
        # Scrollable frame inside canvas
        self.scrollable_frame = tk.Frame(self.task_canvas, bg="#f0f0f0")
        self.canvas_window = self.task_canvas.create_window((0, 0), 
                                                           window=self.scrollable_frame,
                                                           anchor="nw",
                                                           width=self.task_canvas.winfo_width())
        
        # Bind canvas resize
        self.task_canvas.bind('<Configure>', self.on_canvas_configure)
        
        # Mouse wheel binding
        self.task_canvas.bind_all("<MouseWheel>", self.on_mousewheel)
    
    def create_scrollbar(self):
        """Create custom scrollbar"""
        scrollbar_frame = tk.Frame(self.root, bg="#f0f0f0", width=20)
        scrollbar_frame.pack(side="right", fill="y", padx=(0, 10), pady=5)
        
        self.scrollbar = tk.Canvas(scrollbar_frame, bg="#BDC3C7", width=16, 
                                  highlightthickness=0)
        self.scrollbar.pack(fill="y", expand=True)
        
        # Create gradient scrollbar
        for i in range(600):
            color_intensity = 1 - (i / 600) * 0.2
            r = int(189 * color_intensity)
            g = int(195 * color_intensity)
            b = int(199 * color_intensity)
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.scrollbar.create_line(0, i, 16, i, fill=color, width=1)
    
    def on_canvas_configure(self, event):
        """Handle canvas resize"""
        self.task_canvas.itemconfig(self.canvas_window, width=event.width)
    
    def on_mousewheel(self, event):
        """Handle mouse wheel scrolling"""
        self.task_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def add_task(self):
        """Add new task"""
        task_text = self.task_input.get().strip()
        if not task_text:
            messagebox.showwarning("Warning", "Please enter a task!")
            return
        
        task = {
            'id': str(uuid.uuid4()),
            'text': task_text,
            'completed': False,
            'priority': self.priority_var.get(),
            'createdAt': datetime.now().isoformat()
        }
        
        self.tasks.append(task)
        self.task_input.delete(0, tk.END)
        self.save_tasks()
        self.render_tasks()
    
    def toggle_task(self, task_id):
        """Toggle task completion"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = not task['completed']
                break
        
        self.save_tasks()
        self.render_tasks()
    
    def delete_task(self, task_id):
        """Delete task"""
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks()
        self.render_tasks()
    
    def edit_task(self, task_id):
        """Edit task (placeholder for future implementation)"""
        # This would open an edit dialog in a full implementation
        messagebox.showinfo("Info", "Edit functionality coming soon!")
    
    def set_filter(self, filter_type):
        """Set current filter"""
        self.current_filter = filter_type
        self.render_tasks()
    
    def get_filtered_tasks(self):
        """Get tasks based on current filter"""
        if self.current_filter == "active":
            return [task for task in self.tasks if not task['completed']]
        elif self.current_filter == "completed":
            return [task for task in self.tasks if task['completed']]
        else:
            return self.tasks
    
    def render_tasks(self):
        """Render all tasks"""
        # Clear existing tasks
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        filtered_tasks = self.get_filtered_tasks()
        
        if not filtered_tasks:
            # Show empty state
            empty_label = tk.Label(self.scrollable_frame, 
                                 text="No tasks found. Add a new task to get started!",
                                 bg="#f0f0f0", fg="#7F8C8D", font=("Segoe UI", 14))
            empty_label.pack(pady=50)
        else:
            # Render tasks
            for task in filtered_tasks:
                task_card = TaskCard(self.scrollable_frame, task, self, bg="#f0f0f0")
                task_card.pack(fill="x", padx=10, pady=5)
        
        self.update_stats()
    
    def update_stats(self):
        """Update statistics"""
        total = len(self.tasks)
        completed = len([task for task in self.tasks if task['completed']])
        
        self.stats_label.config(text=f"Total: {total} | Completed: {completed}")
    
    def save_tasks(self):
        """Save tasks to file"""
        try:
            with open("tasks.json", "w") as f:
                json.dump(self.tasks, f, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save tasks: {str(e)}")
    
    def load_tasks(self):
        """Load tasks from file"""
        try:
            if os.path.exists("tasks.json"):
                with open("tasks.json", "r") as f:
                    self.tasks = json.load(f)
                self.render_tasks()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load tasks: {str(e)}")
            self.tasks = []

if __name__ == "__main__":
    app = ModernTodoApp()
