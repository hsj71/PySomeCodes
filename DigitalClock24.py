import tkinter as tk
from datetime import datetime

class CircularDigitalClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Circular Digital Clock")
        self.geometry("400x400")
        self.configure(bg="black")
        
        self.time_label = tk.Label(self, font=("Arial", 40), fg="white", bg="black")
        self.time_label.pack(pady=20)
        
        self.date_label = tk.Label(self, font=("Arial", 20), fg="white", bg="black")
        self.date_label.pack(pady=10)
        
        self.update_clock()
    
    def update_clock(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().strftime("%A, %d %B %Y")
        
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        
        self.time_label.after(1000, self.update_clock)

if __name__ == "__main__":
    app = CircularDigitalClock()
    app.mainloop()
