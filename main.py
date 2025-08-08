import tkinter as tk
from tkinter import messagebox
import csv

# Calculate Total, Percentage and Grade
def calculate_result():
    try:
        math = float(entry_math.get())
        science = float(entry_science.get())
        english = float(entry_english.get())
        total = math + science + english
        percent = total / 3

        if percent >= 90:
            grade = 'A'
        elif percent >= 75:
            grade = 'B'
        elif percent >= 50:
            grade = 'C'
        else:
            grade = 'Fail'

        return total, percent, grade
    except:
        messagebox.showerror("Error", "Please enter valid marks.")
        return None, None, None

# Submit function
def submit_result():
    name = entry_name.get()
    roll = entry_roll.get()
    total, percent, grade = calculate_result()

    if not name or not roll:
        messagebox.showwarning("Input Error", "Name and Roll Number are required.")
        return

    if total is not None:
        # Save to CSV
        with open('results.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name, roll, entry_math.get(), entry_science.get(), entry_english.get(), total, percent, grade])
        messagebox.showinfo("Success", "Result Saved Successfully!")
        clear_fields()

# Clear function
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_roll.delete(0, tk.END)
    entry_math.delete(0, tk.END)
    entry_science.delete(0, tk.END)
    entry_english.delete(0, tk.END)

# GUI
root = tk.Tk()
root.title("Student Result Management")
root.geometry("400x400")

tk.Label(root, text="Student Result Form", font=('Arial', 16, 'bold')).pack(pady=10)

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Roll No").pack()
entry_roll = tk.Entry(root)
entry_roll.pack()

tk.Label(root, text="Math Marks").pack()
entry_math = tk.Entry(root)
entry_math.pack()

tk.Label(root, text="Science Marks").pack()
entry_science = tk.Entry(root)
entry_science.pack()

tk.Label(root, text="English Marks").pack()
entry_english = tk.Entry(root)
entry_english.pack()

tk.Button(root, text="Submit", command=submit_result, bg="green", fg="white").pack(pady=10)
tk.Button(root, text="Clear Form", command=clear_fields, bg="gray", fg="white").pack()

root.mainloop()
