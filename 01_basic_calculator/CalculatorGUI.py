import tkinter as tk
from Calculator import Calculate  # import your logic

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")

# Input fields
entry1_label = tk.Label(root, text="First Number:", font=("TimesNewRoman", 8))
entry1_label.pack(pady=2)
entry1 = tk.Entry(root)
entry1.pack(pady=5)
entry2_label = tk.Label(root, text="Second Number:", font=("TimesNewRoman", 8))
entry2_label.pack(pady=2)
entry2 = tk.Entry(root)
entry2.pack(pady=5)
entry3_label = tk.Label(root, text="Operator:", font=("TimesNewRoman", 8))
entry3_label.pack(pady=2)
entry3 = tk.Entry(root)
entry3.pack(pady=5)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Button to Calculate
def calculation():
    input1 = float(entry1.get())
    input2 = float(entry2.get())
    operator = entry3.get()
    result = Calculate(input1, input2, operator)
    result_label.config(text=f"Result: {result}")

button = tk.Button(root, text="Calculate", activeforeground='blue' ,command=calculation)
button.pack()

root.mainloop()
