import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Create main window
root = tk.Tk()
root.title("Product Calculator")

# Labels
label1 = tk.Label(root, text="Enter first number:")
label1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label2 = tk.Label(root, text="Enter second number:")
label2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

# Button
calculate_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calculate_button.pack()

# Result label
result_label = tk.Label(root, text="Product:")
result_label.pack()

# Run the app
root.mainloop()
