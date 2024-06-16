import tkinter as tk
from tkinter import ttk

MIN_YEAR = 1800
MAX_YEAR = 2100
MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]


def create_window(title, width, height):
    """
    Create a GUI window with the specified title, width, and height.

    Args:
        title: The title of the window.
        :param title: str
        width: The width of the window.
        :param width: int
        height: The height of the window.
        :param height: int

    Returns: The created window.
    """
    window = tk.Tk()
    window.title(title)
    window.geometry(f'{width}x{height}')
    window.resizable(False, False)
    return window


def create_dropdown_menu(window, options, row, column, padx=5, pady=5):
    """
    Create a dropdown menu in the specified row and column of the window with the given options.

    Args:
        window: The GUI window in which to create the dropdown menu.
        :param window: tk.Tk
        options: The list of options for the dropdown menu.
        :param options: list[str]
        row: The row in which to place the dropdown menu.
        :param row: int
        column: The column in which to place the dropdown menu.
        :param column: int
        padx: The horizontal padding around the dropdown menu.
        :param padx: int
        pady: The vertical padding around the dropdown menu.
        :param pady: int

    Returns: The created dropdown menu.
    """
    dropdown_menu = ttk.Combobox(window, values=options)
    dropdown_menu.grid(row=row, column=column, padx=padx, pady=pady)
    return dropdown_menu


def is_leap_year(year):
    """
    Determine if the given year is a leap year.

    Args:
        year: The year to check.
        :param year: int

    Returns: True if the given year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def get_days_in_month(month_number, year):
    """
    Get the number of days in the month based on the month number and year.

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


def update_display(year, month):
    """
    Update the display with the selected year and month, including the number of days in the selected month.

    Args:
        year: The selected year.
        :param year: str
        month: The selected month.
        :param month: str

    Returns: None
    """
    if not year or not month:
        display_text.set("Please select both a year and a month.")
        return

    try:
        month_number = MONTHS.index(month) + 1
        days_in_month = get_days_in_month(month_number, int(year))
        display_text.set(f'Selected Month: {month}\nSelected Year: {year}\nNumber of Days: {days_in_month}')
    except ValueError:
        display_text.set("Invalid selection. Please try again.")


def main():
    """
    Create the GUI window, define the dropdown menus, and handle the event loop.

    Returns: None
    """
    window = create_window('Month Selector', 350, 200)

    years = [str(year) for year in range(MIN_YEAR, MAX_YEAR + 1)]
    months = MONTHS

    # Center the layout
    frame = ttk.Frame(window, padding="10")
    frame.grid(row=0, column=0, sticky="nsew")
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    ttk.Label(frame, text="Select a Year:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    year_menu = create_dropdown_menu(frame, years, 0, 1, padx=5, pady=5)

    ttk.Label(frame, text="Select a Month:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    month_menu = create_dropdown_menu(frame, months, 1, 1, padx=5, pady=5)

    select_button = ttk.Button(frame, text='Select', command=lambda: update_display(year_menu.get(), month_menu.get()))
    select_button.grid(row=2, column=0, columnspan=2, pady=10)

    global display_text
    display_text = tk.StringVar()
    display_label = ttk.Label(frame, textvariable=display_text, justify="center")
    display_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    window.mainloop()


if __name__ == '__main__':
    main()
