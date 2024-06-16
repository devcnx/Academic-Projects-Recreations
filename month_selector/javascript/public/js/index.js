"use strict";

/**
 * Selects an element from the DOM using the provided selector. 
 * 
 * @param {string} selector - The CSS selector to use to select the element. 
 * @returns {Element} - The element that was selected. 
 */
const $ = (selector) => document.querySelector(selector);

const MIN_YEAR = 1800;
const MAX_YEAR = 2100;
const MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
];

document.addEventListener("DOMContentLoaded", () => {
    const years = $("#years");
    const months = $("#months");
    const output = $("#output");

    // Populate the years dropdown with the years from 1800 to 2100. 
    for (let year = MIN_YEAR; year <= MAX_YEAR; year++) {
        const option = document.createElement("option");
        option.value = year;
        option.textContent = year;
        years.appendChild(option);
    }

    // Populate the months dropdown with the months.
    MONTHS.forEach((month, index) => {
        const option = document.createElement("option");
        option.value = index + 1;
        option.textContent = month;
        months.appendChild(option);
    })

    /**
     * Determine if a given year is a leap year. 
     * 
     * This function determines if a given year is a leap year. A leap year is a year that is divisible by 4, 
     * except for years that are divisible by 100 and not divisible by 400. 
     * 
     * @param {number} year - The year to check. 
     * @returns {boolean} - True if the year is a leap year, otherwise false.
     */
    const isLeapYear = (year) => {
        return (year % 4 === 0 && year % 100 !== 0 || year % 400 === 0);
    }

    /**
     * Get the number of days in the month for the given year and month. 
     * 
     * This function returns the number of days in the month for the given year and month. It takes into account
     * leap years for February. 
     * 
     * @param {number} month - The month to get the number of days for.
     * @param {number} year - The year to get the number of days for.
     * @returns {number} - The number of days in the month.
     */
    const getDaysInMonth = (month, year) => {
        if (month === 1 || month === 3 || month === 5 || month === 7 || month === 8 || month === 10 || month === 12) {
            return 31;
        } else if (month === 4 || month === 6 || month === 9 || month === 11) {
            return 30;
        } else if (month === 2) {
            return isLeapYear(year) ? 29 : 28;
        } else {
            return 0;
        }
    };

    /**
     * Update the output with the select year and month. 
     * 
     * This function updates the output with the selected year and month and the number of days in the month.
     * If either the year or month is not selected, it will display an error message. 
     * 
     * @returns {void}
     */

    const updateOutput = () => {
        const year = parseInt(years.value);
        const month = parseInt(months.value);

        if (isNaN(year) || isNaN(month)) {
            output.textContent = "Please select both a year and a month.";
            return;
        }

        const days = getDaysInMonth(month, year);
        const monthName = MONTHS[month - 1]; // Convert 1-based index to 0-based index

        output.textContent = `${monthName} of ${year} has ${days} days.`;
    };

    // Update the output when the year or month changes.
    years.addEventListener("change", (e) => {
        if (months.value) {
            updateOutput();
        }
    });

    // Update the output when the year or month changes.
    months.addEventListener("change", (e) => {
        if (years.value) {
            updateOutput();
        }
    });
})