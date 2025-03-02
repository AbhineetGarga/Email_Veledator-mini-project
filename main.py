import re
import tkinter as tk
from tkinter import messagebox

class EmailValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Validator")
        self.root.geometry("400x250")
        self.root.configure(bg="#f0f0f0")

        # Title Label
        self.label = tk.Label(root, text="Email Validator", font=("Arial", 16, "bold"), bg="#f0f0f0")
        self.label.pack(pady=10)

        # Instruction Label
        self.label2 = tk.Label(root, text="Enter your email address:", font=("Arial", 12), bg="#f0f0f0")
        self.label2.pack()

        # Input Field
        self.entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.entry.pack(pady=5)

        # Validate Button
        self.validate_btn = tk.Button(root, text="Check Email", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.addressVal)
        self.validate_btn.pack(pady=10)

        # Quit Button
        self.quit_btn = tk.Button(root, text="Exit", font=("Arial", 12), bg="#f44336", fg="white", command=root.quit)
        self.quit_btn.pack(pady=5)

    def addressVal(self):
        email = self.entry.get()
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

        if re.match(pattern, email):
            messagebox.showinfo("Result", "✅ Valid Email Address!")
        else:
            messagebox.showerror("Result", "❌ Invalid Email Address!")

        self.entry.delete(0, tk.END)  # Clear input field for next entry

# Run the Tkinter application
if __name__ == "__main__":
    root = tk.Tk()
    app = EmailValidatorApp(root)
    root.mainloop()
