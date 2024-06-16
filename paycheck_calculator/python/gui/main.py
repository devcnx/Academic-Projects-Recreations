import tkinter as tk
from tkinter import messagebox

TAX_RATE = 18.0
TAX_RATE_PERCENTAGE = TAX_RATE / 100
MAX_STANDARD_HOURS = 40
OVERTIME_RATE = 1.5


def is_valid_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_valid_float_greater_than_zero(value):
    return is_valid_float(value) and float(value) > 0


def calculate_gross_pay(hours_worked, hourly_rate):
    if hours_worked <= MAX_STANDARD_HOURS:
        return hours_worked * hourly_rate
    else:
        standard_pay = MAX_STANDARD_HOURS * hourly_rate
        overtime_hours = hours_worked - MAX_STANDARD_HOURS
        overtime_pay = overtime_hours * hourly_rate * OVERTIME_RATE
        return standard_pay + overtime_pay


def calculate_taxes(gross_pay):
    return gross_pay * TAX_RATE_PERCENTAGE


def calculate_net_pay(gross_pay, taxes):
    return gross_pay - taxes


def display_pay_details(gross_pay, tax_amount, net_pay):
    result_var.set(f"Gross Pay: ${gross_pay:,.2f}\nTaxes: ${tax_amount:,.2f}\nNet Pay: ${net_pay:,.2f}")


def calculate():
    hours_worked = hours_var.get()
    hourly_rate = rate_var.get()

    if not is_valid_float_greater_than_zero(hours_worked):
        messagebox.showerror("Invalid Input", "Please enter a valid number of hours worked.")
        return

    if not is_valid_float_greater_than_zero(hourly_rate):
        messagebox.showerror("Invalid Input", "Please enter a valid hourly rate.")
        return

    hours_worked = float(hours_worked)
    hourly_rate = float(hourly_rate)

    gross_pay = calculate_gross_pay(hours_worked, hourly_rate)
    tax_amount = calculate_taxes(gross_pay)
    net_pay = calculate_net_pay(gross_pay, tax_amount)

    display_pay_details(gross_pay, tax_amount, net_pay)


# GUI setup
root = tk.Tk()
root.title("Paycheck Calculator")

# Hourly Rate Input
tk.Label(root, text="Hourly Rate:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
rate_var = tk.StringVar()
tk.Entry(root, textvariable=rate_var).grid(row=0, column=1, padx=10, pady=5)

# Hours Worked Input
tk.Label(root, text="Hours Worked:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
hours_var = tk.StringVar()
tk.Entry(root, textvariable=hours_var).grid(row=1, column=1, padx=10, pady=5)

# Calculate Button
tk.Button(root, text="Calculate", command=calculate).grid(row=2, column=0, columnspan=2, pady=10)

# Result Display
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, justify="left").grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
