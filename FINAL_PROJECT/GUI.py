import tkinter as tk
from tkinter import messagebox, ttk


class GastosTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Gastos Tracker - PHP Budget Manager")
        self.root.geometry("650x550")
        self.root.resizable(True, True)

        # Data (same as your console version)
        self.expenses = []
        self.funds = 0.0

        self.setup_ui()
        self.update_display()

    def setup_ui(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Make window resizable
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)

        # Title
        title = ttk.Label(main_frame, text="=== Gastos Tracker (COMPLETE) ===",
                          font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # Funds display (like your console "Funds: PHP X.XX")
        self.funds_label = ttk.Label(main_frame, text="Funds: PHP 0.00",
                                     font=("Arial", 14, "bold"),
                                     foreground="#2E7D32")
        self.funds_label.grid(row=1, column=0, columnspan=3, pady=(0, 20))

        # Buttons (exactly like your menu 1,2,3,4)
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=2, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))

        ttk.Button(btn_frame, text="1. Add expense", command=self.add_expense_gui).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="2. View expenses", command=self.view_expenses_gui).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="3. Manage funds", command=self.manage_funds_gui).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="4. RESET ALL DATA", command=self.reset_all_gui).pack(side=tk.LEFT, padx=5)

        # Expenses table (like your for loop display)
        table_frame = ttk.LabelFrame(main_frame, text="Expenses List", padding="10")
        table_frame.grid(row=3, column=0, columnspan=3, pady=20, sticky=(tk.W, tk.E, tk.N, tk.S))
        table_frame.columnconfigure(0, weight=1)
        table_frame.rowconfigure(0, weight=1)

        # Table columns
        columns = ("Description", "Amount", "Balance")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

        self.tree.heading("Description", text="Description")
        self.tree.heading("Amount", text="Amount (PHP)")
        self.tree.heading("Balance", text="Balance After (PHP)")

        self.tree.column("Description", width=250)
        self.tree.column("Amount", width=120)
        self.tree.column("Balance", width=120)

        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Scrollbar for table
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

    def update_display(self):
        """Update funds label and table (like your main loop display)"""
        self.funds_label.config(text=f"💰 Funds: PHP {self.funds:.2f}")
        self.refresh_table()

    def refresh_table(self):
        """Refresh expenses table (like your for exp in expenses loop)"""
        # Clear table
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fill table (same logic as your for loop)
        total_spent = 0
        for exp in self.expenses:
            self.tree.insert("", tk.END, values=(
                exp["description"],
                f"{exp['amount']:.2f}",
                f"{self.funds:.2f}"  # Current balance
            ))
            total_spent += exp['amount']

    def add_expense_gui(self):
        """GUI version of your add_expense() function"""
        window = tk.Toplevel(self.root)
        window.title("1. Add expense")
        window.geometry("400x250")
        window.grab_set()

        ttk.Label(window, text="Enter expense description (e.g., 'Grocery'):", font=("Arial", 10)).pack(pady=10)
        desc_entry = ttk.Entry(window, width=30, font=("Arial", 11))
        desc_entry.pack(pady=5)
        desc_entry.focus()

        ttk.Label(window, text="Enter amount (PHP):", font=("Arial", 10)).pack(pady=(20, 5))
        amount_entry = ttk.Entry(window, width=30, font=("Arial", 11))
        amount_entry.pack(pady=5)

        def submit():
            try:
                description = desc_entry.get().strip()
                amount = float(amount_entry.get())

                # Same logic as your add_expense()
                if amount > self.funds:
                    messagebox.showerror("Error",
                                         f"Insufficient funds! Need PHP {amount:.2f}, have PHP {self.funds:.2f}")
                    return
                if not description:
                    messagebox.showerror("Error", "Please enter description!")
                    return

                # Add expense (same as your code)
                self.funds -= amount
                self.expenses.append({"description": description, "amount": amount})

                messagebox.showinfo("Success", f"✅ Expense added & deducted!\nRemaining: PHP {self.funds:.2f}")
                self.update_display()
                window.destroy()

            except ValueError:
                messagebox.showerror("Error", "Please enter valid amount!")

        ttk.Button(window, text="Add Expense", command=submit).pack(pady=20)

    def view_expenses_gui(self):
        """GUI version of your view_expenses() function"""
        if not self.expenses:
            messagebox.showinfo("Expenses", "No expenses recorded yet.")
            return

        # Same logic as your view_expenses()
        total = 0
        expense_text = "--- All Expenses ---\n\n"
        for exp in self.expenses:
            expense_text += f"{exp['description']}: PHP {exp['amount']:.2f}\n"
            total += exp['amount']
        expense_text += f"\nTotal spent: PHP {total:.2f}"

        messagebox.showinfo("View Expenses", expense_text)

    def manage_funds_gui(self):
        """GUI version of your fund_function()"""
        window = tk.Toplevel(self.root)
        window.title("3. Manage funds")
        window.geometry("400x300")
        window.grab_set()

        ttk.Label(window, text=f"Current funds: PHP {self.funds:.2f}",
                  font=("Arial", 12, "bold")).pack(pady=10)

        ttk.Label(window, text="Enter amount:").pack(pady=(20, 5))
        amount_entry = ttk.Entry(window, width=30, font=("Arial", 11))
        amount_entry.pack(pady=5)
        amount_entry.focus()

        ttk.Label(window, text="Action:").pack(pady=(20, 5))
        action_var = tk.StringVar(value="a")
        ttk.Radiobutton(window, text="Add (a)", variable=action_var, value="a").pack()
        ttk.Radiobutton(window, text="Deduct (d)", variable=action_var, value="d").pack()

        def apply():
            try:
                amount = float(amount_entry.get())
                action = action_var.get()

                # Same logic as your fund_function()
                if action == "a":
                    self.funds += amount
                    messagebox.showinfo("Success", f"Added PHP {amount:.2f}.\nNew balance: PHP {self.funds:.2f}")
                else:  # deduct
                    if amount <= self.funds:
                        self.funds -= amount
                        messagebox.showinfo("Success", f"Deducted PHP {amount:.2f}.\nNew balance: PHP {self.funds:.2f}")
                    else:
                        messagebox.showerror("Error", "Insufficient funds!")

                self.update_display()
                window.destroy()

            except ValueError:
                messagebox.showerror("Error", "Please enter valid amount!")

        ttk.Button(window, text="Apply", command=apply).pack(pady=20)

    def reset_all_gui(self):
        """GUI version of your reset_all()"""
        if messagebox.askyesno("Confirm", "ALL DATA RESET! Expenses cleared.\nFunds reset to PHP 0.00\n\nStart fresh?"):
            self.expenses = []
            self.funds = 0.0
            self.update_display()
            messagebox.showinfo("Reset", "Start fresh!")


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = GastosTracker(root)
    root.mainloop()
