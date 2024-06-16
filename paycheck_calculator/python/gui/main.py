"""
    Paycheck Calculator - Python GUI Application
    Date: Saturday, June 15th, 2024
    Author: Brittaney Perry-Morgan

    This module contains the main functionality of the Paycheck Calculator GUI application in Python.
    The application calculates the gross pay, taxes, and net pay based on the number of hours worked and the hourly 
    rate. The user can enter the number of hours worked and the hourly rate in the GUI, and the application displays
    the calculated pay details after the user clicks the 'Calculate' button. The tax rate is set to 18%, and overtime
    pay is calculated at 1.5 times the hourly rate for hours worked over 40 hours. The main functionality includes 
    functions to validate user input, calculate pay details, and display the results in the GUI. The application 
    provides a simple graphical user interface for interacting with the user. The module includes Python's Tkinter
    library, and the Themed Tkinter (ttk) module is used for styling the GUI components. 

    The following functions are defined in this module:
        - is_valid_float(value): Checks if the input value can be converted to a float. 
        - is_valid_float_greater_than_zero(value): Checks if the input value is a valid float greater than zero. 
        - calculate_gross_pay(hours_worked, hourly_rate): Calculates the gross pay based on the hours worked and rate.
        - calculate_taxes(gross_pay): Calculates the taxes based on the gross pay and the tax rate. 
        - calculate_net_pay(gross_pay, taxes): Calculates the net pay based on the gross pay and taxes.
        - display_pay_details(gross_pay, tax_amount, net_pay): Displays the pay details to the user.
        - calculate(): Event handler for the 'Calculate' button click.
        - setup_gui(root): Sets up the graphical user interface for the application. 
    """

import tkinter as tk
from tkinter import messagebox

TAX_RATE = 18.0
TAX_RATE_PERCENTAGE = TAX_RATE / 100
MAX_STANDARD_HOURS = 40
OVERTIME_RATE = 1.5


def is_valid_float(value):
    """
    Check if the input value can be converted to a float. 

    Args:
        value: The input value to check. 
        :param value: str

    Returns: True if the value can be converted to a float, False otherwise. 
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_valid_float_greater_than_zero(value):
    """
    Check if the input value is a valid float greater than zero. 

    Args:
        value: The input value to check. 
        :param value: str 

    Returns: True if the value is a valid float greater than zero, False otherwise.
    """
    return is_valid_float(value) and float(value) > 0


def calculate_gross_pay(hours_worked, hourly_rate):
    """
    Calculate the gross pay based on the hours worked and hourly rate. 

    The function calculates the gross pay based on the number of hours worked and the hourly rate. 
    If the hours worked are less than or equal to the maximum standard hours, the function calculates the pay
    as a product of hours worked and the hourly rate. If the hours worked exceed the maximum standard hours,
    the function calculates the standard pay for the maximum standard hours and adds the overtime pay for the 
    additional hours worked at the overtime rate. 

    Args:
        hours_worked: The number of hours worked. 
        :param hours_worked: float

        hourly_rate: The hourly rate. 
        :param hourly_rate: float

    Returns: The gross pay based on the hours worked and hourly rate (e.g., standard pay + overtime pay).
    """
    if hours_worked <= MAX_STANDARD_HOURS:
        return hours_worked * hourly_rate
    else:
        standard_pay = MAX_STANDARD_HOURS * hourly_rate
        overtime_hours = hours_worked - MAX_STANDARD_HOURS
        overtime_pay = overtime_hours * hourly_rate * OVERTIME_RATE
        return standard_pay + overtime_pay


def calculate_taxes(gross_pay):
    """
    Calculate the taxes based on the gross pay and the tax rate. 

    The function calculates the taxes based on the gross pay and the tax rate. The tax amount is calculated as the 
    product of the gross pay and the tax rate percentage constant. 

    Args:
        gross_pay: The gross pay amount. 
        :param gross_pay: float

    Returns: The calculated tax amount based on the gross pay and tax rate. 
    """
    return gross_pay * TAX_RATE_PERCENTAGE


def calculate_net_pay(gross_pay, taxes):
    """
    Calculate the net pay based on the gross pay and taxes. 

    The function calculates the net pay based on the gross pay and the taxes. The net pay is calculated as the 
    difference between the gross pay and the taxes. 

    Args:
        gross_pay: The gross pay amount. 
        :param gross_pay: float 

        taxes: The tax amount. 
        :param taxes: float

    Returns: The calculated net pay after deducting the taxes from the gross pay. 
    """
    return gross_pay - taxes


def display_pay_details(gross_pay, tax_amount, net_pay):
    """
    Display the pay details to the user. 

    The function displays the pay details to the user in the GUI. The pay details include the gross pay, tax amount, 
    and net pay. The function formats the pay details as a string and sets the result variable to display the 
    formatted pay details in the GUI. 

    Args:
        gross_pay: The gross pay amount.
        :param gross_pay: float

        tax_amount: The tax amount.
        :param tax_amount: float

        net_pay: The net pay amount.
        :param net_pay: float

    Returns: None
    """
    result_var.set(f"Gross Pay: ${gross_pay:,.2f}\nTaxes: ${tax_amount:,.2f}\nNet Pay: ${net_pay:,.2f}")


def calculate():
    """
    Event handler for the 'Calculate' button click.

    The function is called when the user clicks the 'Calculate' button in the GUI. It retrieves the input values 
    for the hours worked and hourly rate from the input fields, validates the input values, calculates the gross pay,
    taxes, and net pay based on the input values, and displays the pay details in the GUI. If the input values are 
    invalid, the function displays an error message to the user as a pop-up dialog. If the input values are valid,
    the function calculates the pay details and displays them in the GUI at the bottom of the window.
    """
    hours_worked = hours_var.get().strip()
    hourly_rate = rate_var.get().strip()

    if not hours_worked:
        messagebox.showerror("Invalid Input", "Please enter the number of hours worked.")
        return

    if not hourly_rate:
        messagebox.showerror("Invalid Input", "Please enter the hourly rate.")
        return

    if not is_valid_float_greater_than_zero(hours_worked):
        messagebox.showerror("Invalid Input", "Please enter a valid number of hours worked greater than zero.")
        return

    if not is_valid_float_greater_than_zero(hourly_rate):
        messagebox.showerror("Invalid Input", "Please enter a valid hourly rate greater than zero.")
        return

    hours_worked = float(hours_worked)
    hourly_rate = float(hourly_rate)

    gross_pay = calculate_gross_pay(hours_worked, hourly_rate)
    tax_amount = calculate_taxes(gross_pay)
    net_pay = calculate_net_pay(gross_pay, tax_amount)

    display_pay_details(gross_pay, tax_amount, net_pay)


def setup_gui(root):
    """
    Set up the graphical user interface for the application. 

    The function sets up the GUI components for the Paycheck Calculator application. It creates labels and input fields
    for the hourly rate and hours worked, a 'Calculate' button to trigger the pay calculation, and a label to display 
    the pay details after the calculation. The function uses the Tkinter library to create the GUI components and 
    layout for them in the application window. 

    Args:
        root: The root window of the application. 
        :param root: tk.Tk

    Returns: None
    """
    root.title("Paycheck Calculator")

    # Hourly Rate Input
    tk.Label(root, text="Hourly Rate:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    global rate_var
    rate_var = tk.StringVar()
    tk.Entry(root, textvariable=rate_var).grid(row=0, column=1, padx=10, pady=5)

    # Hours Worked Input
    tk.Label(root, text="Hours Worked:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    global hours_var
    hours_var = tk.StringVar()
    tk.Entry(root, textvariable=hours_var).grid(row=1, column=1, padx=10, pady=5)

    # Calculate Button
    tk.Button(root, text="Calculate", command=calculate).grid(row=2, column=0, columnspan=2, pady=10)

    # Result Display
    global result_var
    result_var = tk.StringVar()
    tk.Label(root, textvariable=result_var, justify="left").grid(row=3, column=0, columnspan=2, padx=10, pady=10)


if __name__ == '__main__':
    """
    Main code block of the Paycheck Calculator GUI application.
    """
    root = tk.Tk()
    setup_gui(root)
    root.mainloop()
