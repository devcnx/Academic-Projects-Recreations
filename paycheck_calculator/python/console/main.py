"""
Paycheck Calculator - Python Console Application
Date: Saturday, June 15th, 2024
Author: Brittaney Perry-Morgan

This module contains the main functionality of the Paycheck Calculator console application in Python. 
The application calculates the gross pay, taxes, and net pay based on the number of hours worked and the hourly rate. 
The user is prompted to enter the number of hours worked and the hourly rate, and the application displays the
calculated pay details. The tax rate is set to 18%, and overtime pay is calculated at 1.5 times the hourly rate for
hours worked over 40 hours. There are four constant variables defined at the beginning of the module: TAX_RATE, 
TAX_RATE_PERCENTAGE, MAX_STANDARD_HOURS, and OVERTIME_RATE. The main functionality includes functions to validate user
input, calculate pay details, and display the results. The application provides a simple command-line interface for
interacting with the user. 

The following functions are defined in this module:
    - prompt_user(prompt): Prompts the user for input and returns the user's input.
    - is_valid_input(value): Checks if the input value is not an empty string. 
    - is_valid_float(value): Checks if the input value can be converted to a float. 
    - is_valid_float_greater_than_zero(value): Checks if the input value is a valid float greater than zero. 
    - get_valid_input(prompt, validation_function, error_message): Prompts the user for input and validates the input.
    - calculate_gross_pay(hours_worked, hourly_rate): Calculates the gross pay based on the hours worked and rate.
    - calculate_taxes(gross_pay): Calculates the taxes based on the gross pay and the tax rate. 
    - calculate_net_pay(gross_pay, taxes): Calculates the net pay based on the gross pay and taxes. 
    - display_pay_details(gross_pay, tax_amount, net_pay): Displays the pay details to the user. 
    
The main code block of the module interacts with the user to get the hours worked and hourly rate, calculates the pay
details, and displays the results to the user. The user is prompted to enter the hours worked and hourly rate, and the
application calculates the gross pay, taxes, and net pay based on the input values. The results are then displayed to
the user. 
"""

TAX_RATE = 18.0  # Tax rate
TAX_RATE_PERCENTAGE = TAX_RATE / 100  # Tax rate percentage
MAX_STANDARD_HOURS = 40  # Maximum standard hours for regular pay
OVERTIME_RATE = 1.5  # Overtime rate multiplier


def prompt_user(prompt):
    """ 
    Prompt the user for input and return the user's input. 

    Arguments:
        prompt: A prompt message. 
        :param prompt: str

    Returns: The user's input.
    """
    return input(prompt)


def is_valid_input(value):
    """
    Check if the input value is valid, meaning it's not an empty string. 

    Arguments:
        value: The input value to check. 
        :param value: str 
    """
    return value != ''


def is_valid_float(value):
    """
    Check if the input value can be converted to a float. 

    This function attempts to convert the input value to a float and returns True if successful,
    indicating that the input is a valid float. If the conversion raises a ValueError, it returns False.

    Args:
        value: The input value to check. 
        :param value: str

    Returns: True if the input value can be converted to a float, False otherwise.
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

    Returns: True if the input value is a valid float greater than zero, False otherwise. 
    """
    return is_valid_float(value) and float(value) > 0


def get_valid_input(prompt, validation_function, error_message):
    """
    Prompt the user for input and validate the input using the specified validation function. 

    This function prompts the user for input using the given prompt message and validates the input using the
    specified validation function. If the input is not valid, it displays the error message and prompts the user
    again until a valid input is provided. 

    Args:
        prompt: The prompt message to display to the user. 
        :param prompt: str

        validation_function: The function used to validate the input. 
        :param validation_function: function

        error_message: The error message to display if the input is invalid. 
        :param error_message: str

    Returns: The valid input value. 
    """
    value = prompt_user(prompt)
    while not validation_function(value):
        value = prompt_user(error_message)
    return float(value)


def calculate_gross_pay(hours_worked, hourly_rate):
    """
    Calculate the gross pay based on the hours worked and the hourly rate. 

    Args:
        hours_worked: The number of hours worked. 
        :param hours_worked: float

        hourly_rate: The hourly rate. 
        :param hourly_rate: float

    Returns: The calculated gross pay (e.g., standard pay + overtime pay, if applicable). Overtime pay is calculated at
    1.5 times the hourly rate for hours worked over 40 hours.
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

    Args:
        gross_pay: The gross pay amount. 
        :param gross_pay: float

    Returns: The calculated tax amount based on the gross pay and the tax rate.
    """
    return gross_pay * TAX_RATE_PERCENTAGE


def calculate_net_pay(gross_pay, taxes):
    """
    Calculate the net pay based on the gross pay and the taxes. 

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

    This function displays the gross pay, tax amount, and net pay to the user in a formatted manner.

    Args:
        gross_pay: The gross pay amount. 
        :param gross_pay: float

        tax_amount: The tax amount. 
        :param tax_amount: float

        net_pay: The net pay amount. 
        :param net_pay: float
    """
    print(f'\n{"-" * 40}')
    print(f'{"Gross Pay:":<15} ${gross_pay:,.2f}')
    print(f'{"Taxes:":<15} ${tax_amount:,.2f}')
    print(f'{"Net Pay:":<15} ${net_pay:,.2f}')
    print(f'{"-" * 40}\n')
    print('Thank you for using the Paycheck Calculator!')


if __name__ == '__main__':
    """
    Main code block of the Paycheck Calculator console application.
    """
    print('\nWelcome to the Paycheck Calculator!')
    print(f'{"-" * 40}\n')

    hours_worked = get_valid_input(
        'Enter the number of hours worked: ',
        lambda value: is_valid_input(value) and is_valid_float_greater_than_zero(value),
        'Invalid input. Please enter a valid number of hours worked: '
    )

    hourly_rate = get_valid_input(
        'Enter the hourly rate: ',
        lambda value: is_valid_input(value) and is_valid_float_greater_than_zero(value),
        'Invalid input. Please enter a valid hourly rate: '
    )

    gross_pay = calculate_gross_pay(hours_worked, hourly_rate)
    tax_amount = calculate_taxes(gross_pay)
    net_pay = calculate_net_pay(gross_pay, tax_amount)

    display_pay_details(gross_pay, tax_amount, net_pay)
