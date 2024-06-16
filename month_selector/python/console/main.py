"""
    Month Selector - Python Console Application 
    Date: Sunday, June 16th, 2024
    Author: Brittaney Perry-Morgan

    This module contains the main functionality of the Month Selector console application in Python. The application
    allows the user to select a year and a month from a list of options and displays the selected month and year. 
    The user is prompted to enter the year and select a month from the list of months. The application validates the
    user input and displays the selected month (by full name) and year to the user. The main functionality includes
    functions to validate user input, get the month name from the month number, and display the selected month, year,
    and number of days in the month. The application takes leap years into consideration when calculating the number of
    days in February. There are six constant variables defined at the beginning of the module: MIN_YEAR, MAX_YEAR, 
    MIN_MONTH, MAX_MONTH, MONTHS, and INSTRUCTIONS.
    
    The following functions are defined in this module:
        - display_start(): Displays the welcome message and instructions to the user.
        - prompt_user(prompt): Prompts the user for input and returns the user's input. 
        - is_valid_input(value): Checks if the input value is not an empty string. 
        - is_valid_integer(value): Checks if the input value can be converted to an integer. 
        - is_valid_year(value): Checks if the input value is a valid year within the specified range. 
        - get_valid_input(prompt, validation_function, error_message): Prompts the user for input and validates the
            input. 
        - is_leap_year(year): Checks if the given year is a leap year.
        - is_valid_month(value): Checks if the input value is a valid month within the specified range. 
        - get_month_name(month_number): Returns the full name of the month based on the month number. 
        - get_days_in_month(month_number, year): Returns the number of days in the month based on the month number
            and year. 
        - display_selected_month(month_name, year, days_in_month): Displays the selected month, year, and number of days
            in the month to the user. 
    """

MIN_YEAR = 1800
MAX_YEAR = 2100
MIN_MONTH = 1
MAX_MONTH = 2
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
INSTRUCTIONS = [
    f'Select a year between {MIN_YEAR} and {MAX_YEAR}.',
    f'Select a month between January and December, represented by the numbers 1 to 12.',
    'The application will display the selected month (by full name), year, and the number of days in the month.'
]


def display_start():
    """
    Display the welcome message and instructions to the user. 

    The function displays the welcome message and instructions to the user when the application starts. 
    The instructions provide guidance on selecting a year and a month, and the expected output. 

    Returns: None
    """
    print(f'\n{"Welcome to the Month Selector Application":^80}')
    print(f'{"-" * 80}\n')
    print(f'Instructions:')
    for index, instruction in enumerate(INSTRUCTIONS, start=1):
        print(f'{" " * 2}{index}. {instruction}')
    print('\n')


def prompt_user(prompt):
    """
    Prompt the user for input and return the user's input. 

    This function takes a prompt message as an argument and displays the prompt to the user. 

    Args:
        prompt: A prompt message.
        :param prompt: str

    Returns: The user's input.
    """
    return input(prompt)


def is_valid_input(value):
    """
    Check if the input value is not an empty string. 

    Args:
        value: The input value to check. 
        :param value: str

    Returns: True if the input value is not an empty string, False otherwise.
    """
    return value != ''


def is_valid_integer(value):
    """
    Checks if the input value can be converted to an integer. 

    This function attempts to convert the input value to an integer and returns True if successful, 
    indicating that the input is a valid integer. If the conversion raises a ValueError, it returns False. 

    Args:
        value: The input value to check. 
        :param value: str 

    Returns: True if the input value can be converted to an integer, False otherwise.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_valid_year(value):
    """
    Check if the input value is a valid year within the specified range. 

    The function checks if the input value can be converted to an integer and if it falls within the
    specified range of years. The function uses the constant values MIN_YEAR and MAX_YEAR to determine
    the valid range of years. MIN_YEAR is set to 1800 and MAX_YEAR is set to 2100.

    Args:
        value: The input value to check. 
        :param value: str 

    Returns: True if the input value is a valid year within the specified range, False otherwise.
    """
    return is_valid_integer(value) and MIN_YEAR <= int(value) <= MAX_YEAR


def get_valid_input(prompt, validation_function, error_message):
    """ 
    Prompt the user for input and validate the input using the specified validation function. 

    The function prompts the user for input using the specified prompt message and validates the input
    using the provided validation function. If the input is not valid, the function displays the error
    message and prompts the user again until a valid input is provided. If the validation function is
    valid, the function returns the input value. 

    Args:
        prompt: The prompt message to display to the user. 
        :param prompt: str 

        validation_function: The function used to validate the input value. 
        :param validation_function: function 

        error_message: The error message to display if the input is invalid. 
        :param error_message: str

    Returns: The valid input value. 
    """
    while True:
        value = prompt_user(prompt)
        if validation_function(value):
            return value
        else:
            print(error_message)


def is_leap_year(year):
    """
    Determine if the given year is a leap year. 

    The function checks if the given year is a leap year based on the following criteria:
        - The year is evenly divisible by 4. 
        - The year is not divisible by 100, unless it is also divisible by 400. 

    Args:
        year: The year to check. 
        :param year: int

    Returns: True if the given year is a leap year, False otherwise. 
    """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def is_valid_month(value):
    """
    Determine if the given month is a valid month within the specified range. 

    The function checks if the input value can be converted to an integer and if it falls within the
    specified range of months. The function uses the constant values MIN_MONTH and MAX_MONTH to determine
    the valid range of months. MIN_MONTH is set to 1, which is for January, and MAX_MONTH is set to 12, 
    which is for December. 

    Args:
        value: The input value to check. 
        :param value: str

    Returns: True if the input value is a valid month within the specified range, False otherwise. 
    """
    return is_valid_integer(value) and MIN_MONTH <= int(value) <= MAX_MONTH


def get_month_name(month_number):
    """
    Get the month named based on the month number. 

    The function returns the full name of the month based on the month number provided as an argument. 
    The function uses the MONTHS constant list to map the month number to the corresponding month name. 
    Because the list is zero-based, the month number is decremented by 1 to get the correct index. 

    Args:
        month_number: The month number. 
        :param month_number: int

    Returns: The full name of the month. 
    """
    return MONTHS[month_number - 1]


def get_days_in_month(month_number, year):
    """
    Get the number of days in the month based on the month number and year. 

    The function calculates the number of days in the month based on the month number and year provided as
    arguments. The function takes leap years into consideration when determining the number of days in February. 
    The function returns the number of days in the month. 

    Args:
        month_number: The month number. 
        :param month_number: int

        year: The year. 
        :param year: int

    Returns: The number of days in the month. 
    """
    if month_number in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month_number in [4, 6, 9, 11]:
        return 30
    elif month_number == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 0


def display_selected_month(month_name, year, days_in_month):
    """
    Display the selected month, year, and number of days in the month. 

    The function displays the selected month (by full name), year, and the number of days in the month to the user. 
    The function takes the month name, year, and number of days in the month as arguments and formats the output
    message accordingly. 

    Args:
        month_name: The full name of the month.
        :param month_name: str

        year: The year.
        :param year: str

        days_in_month: The number of days in the month. 
        :param days_in_month: int

    Returns: None
    """
    print(f'\nSelected Month: {month_name}')
    print(f'Selected Year: {year}')
    print(f'Days in the Month: {days_in_month}')
    print(f'\n')


def main():
    """
    Main code block of the Month Selector console application. 
    """
    display_start()
    while True:
        year = get_valid_input('Enter the year: ', is_valid_year,
                               f'{" " * 2}*** Enter a valid year between {MIN_YEAR} and {MAX_YEAR}.')
        month = get_valid_input('Enter the month (1-12): ', is_valid_month,
                                f'{" " * 2}*** Enter a valid month between 1 and 12.')
        month_name = get_month_name(int(month))
        days_in_month = get_days_in_month(int(month), int(year))
        display_selected_month(month_name, year, days_in_month)
        print('Thank you for using the Month Selector Application!')
        break


if __name__ == '__main__':
    main()
