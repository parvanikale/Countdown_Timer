import tkinter as tk
from tkinter import messagebox
import time
import winsound  # built-in Windows module to play .wav sound

# -------------------- Create GUI Window --------------------
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("300x200")

# -------------------- Input Fields --------------------
tk.Label(root, text="Hours:").grid(row=0, column=0)
tk.Label(root, text="Minutes:").grid(row=1, column=0)
tk.Label(root, text="Seconds:").grid(row=2, column=0)

hours_entry = tk.Entry(root)
minutes_entry = tk.Entry(root)
seconds_entry = tk.Entry(root)

hours_entry.grid(row=0, column=1)
minutes_entry.grid(row=1, column=1)
seconds_entry.grid(row=2, column=1)

# -------------------- Countdown Display --------------------
time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 24))
time_label.grid(row=4, column=0, columnspan=2)

# -------------------- Countdown Function --------------------
def start_countdown():
    try:
        total_seconds = int(hours_entry.get())*3600 + int(minutes_entry.get())*60 + int(seconds_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")
        return

    while total_seconds >= 0:
        mins, secs = divmod(total_seconds, 60)
        hrs, mins = divmod(mins, 60)
        time_label.config(text=f"{hrs:02d}:{mins:02d}:{secs:02d}")
        root.update()
        time.sleep(1)
        total_seconds -= 1

    # Play alarm when countdown finishes
    winsound.PlaySound("alarm.wav", winsound.SND_FILENAME)
    messagebox.showinfo("Time's up!", "Countdown finished!")

# -------------------- Start Button --------------------
start_button = tk.Button(root, text="Start", command=start_countdown)
start_button.grid(row=3, column=0, columnspan=2)

# -------------------- Run GUI --------------------
root.mainloop()