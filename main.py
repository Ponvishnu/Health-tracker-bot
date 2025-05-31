import tkinter as tk
from tkinter import messagebox
from nlp_parser import parse_health_input
from data_manager import log_data, get_daily_summary

class HealthTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Health Tracker Bot")
        self.root.geometry("500x400")

        self.label = tk.Label(root, text="Enter your health activity:", font=('Arial', 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        self.submit_btn = tk.Button(root, text="Submit", command=self.process_input)
        self.submit_btn.pack(pady=5)

        self.summary_btn = tk.Button(root, text="Show Today’s Summary", command=self.show_summary)
        self.summary_btn.pack(pady=5)

        self.output = tk.Text(root, height=10, width=60)
        self.output.pack(pady=10)

    def process_input(self):
        text = self.entry.get()
        parsed = parse_health_input(text)
        if parsed['metric'] != 'unknown' and parsed['value'] is not None:
            log_data(parsed['metric'], parsed['value'])
            self.output.insert(tk.END, f"✅ Logged {parsed['value']} for {parsed['metric']}\n")
        else:
            self.output.insert(tk.END, "⚠️ Could not understand the input.\n")

    def show_summary(self):
        summary = get_daily_summary()
        self.output.insert(tk.END, "\n📋 Today's Summary:\n")
        for metric, value in summary.items():
            self.output.insert(tk.END, f" - {metric.capitalize()}: {value}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthTrackerApp(root)
    root.mainloop()
