"use strict";

/**
 * Selects an element from the DOM using the provided selector. 
 * 
 * @param {string} selector - The CSS selector to use to select the element. 
 * @returns {Element} The element that was selected.
 *
 */
const $ = (selector) => document.querySelector(selector);

const TAX_RATE = 0.18;
const MAX_STANDARD_HOURS = 40;
const OVERTIME_RATE = 1.5;

document.addEventListener("DOMContentLoaded", () => {
    const hourlyRate = $("#hourlyRate");
    const hoursWorked = $("#hoursWorked");

    const hourlyRateError = $("#hourlyRateError");
    const hoursWorkedError = $("#hoursWorkedError");

    const grossPay = $("#grossPay");
    const taxes = $("#taxes");
    const netPay = $("#netPay");

    /**
     * Returns the value of the provided element. 
     * 
     * This function is used to get the value of an input element. 
     * 
     * @param {Element} element - The element to get the value from. 
     * @returns {string} - The value of the element. 
     */
    const getInputValue = (element) => element.value;

    /**
     * Returns the value of the provided element as a number (float).
     * 
     * This function is used to get the value of an input element and convert it to a number. 
     * 
     * @param {Element} element - The element to get the value from. 
     * @returns {float} - The value of the element as a number (float).
     */
    const getInputNumberValue = (element) => parseFloat(getInputValue(element));

    /**
     * Checks if the provided value is a valid input. 
     * 
     * This function checks that the value is not an empty string and that it is a number. If the value is not
     * a number, it will return false, otherwise it will return true.
     * 
     * @param {string} value - The value to check. 
     * @returns {boolean} - True if the value is a valid input, otherwise false.
     */
    const isValidInput = (value) => value !== "" && !isNaN(value);

    /**
     * Checks if the provided value is a valid input and greater than zero. 
     * 
     * This function checks that the value is a valid input and that it is greater than zero. If the value is not
     * a number or is less than or equal to zero, it will return false, otherwise it will return true. 
     * 
     * @param {string} value - The value to check. 
     * @returns {boolean} - True if the value is a valid input and greater than zero, otherwise false.
     */
    const isValidInputGreaterThanZero = (value) => isValidInput(value) && parseFloat(value) > 0;

    /**
     * Displays an error message in the provided element. 
     * 
     * This function sets the text content of the provided element to the provided message.
     * 
     * @param {Element} element - The element to display the error message in. 
     * @param {string} message - The error message to display. 
     * @returns {void}
     */
    const displayError = (element, message) => { element.textContent = message; }

    /**
     * Clears the error message from the provided element. 
     * 
     * This function sets the text content of the provided element to a non-breaking space (&nbsp;). This will
     * clear the error message from the element without removing the element from the DOM. 
     * 
     * @param {Element} element - The element to clear the error message from. 
     * @returns {void}
     */
    const clearError = (element) => { element.textContent = "\u00A0"; }

    /**
     * Clears the value of the provided element.
     * 
     * This function sets the value of the provided element to an empty string. This will clear the value from the
     * element without removing the element from the DOM. This is used for the auto-populated inputs (gross pay, taxes,
     * and net pay). 
     * 
     * @param {Element} element - The element to clear the value from. 
     * @returns {void}
     */
    const clearElementValue = (element) => { element.value = ""; }

    /**
     * Clears the values of all auto-populated inputs. 
     * 
     * This function clears the values of the gross pay, taxes, and net pay inputs. This is used when an error is 
     * displayed to the user. The function iterates over the auto-populated inputs and clears the value of each one.
     * 
     * @returns {void}
     */
    const clearAllAutoPopulatedInputs = () => {
        const autoPopulatedInputs = [grossPay, taxes, netPay];
        autoPopulatedInputs.forEach((input) => clearElementValue(input));
    }

    /**
     * Validates the input values. 
     * 
     * This function validates the hourly rate and hours worked inputs. It checks that the values are not empty strings,
     * that they are numbers, and that they are greater than zero. If the values are not valid, it will display an error
     * message to the user and clear the auto-populated inputs. If the values are valid, it will clear any error
     * messages that are displayed. 
     * 
     * @returns {boolean} - True if the inputs are valid, otherwise false.
     */
    const validateInputs = () => {
        let isValid = true;

        const rateValue = getInputNumberValue(hourlyRate);
        const hoursValue = getInputNumberValue(hoursWorked);

        if (!isValidInputGreaterThanZero(rateValue)) {
            displayError(hourlyRateError, "Enter a valid hourly rate.");
            isValid = false;
            clearAllAutoPopulatedInputs();
        } else {
            clearError(hourlyRateError);
        }

        if (!isValidInputGreaterThanZero(hoursValue)) {
            displayError(hoursWorkedError, "Enter a valid number of hours worked.");
            isValid = false;
            clearAllAutoPopulatedInputs();
        } else {
            clearError(hoursWorkedError);
        }

        return isValid;
    }

    /**
     * Calculates the gross pay. 
     * 
     * This function calculates the gross pay based on the hours worked and hourly rate. If the hours worked are less
     * than or equal to the maximum standard hours (40), the gross pay is calculated by multiplying the hours worked 
     * by the hourly rate. If the hours worked are greater than the maximum standard hours, the gross pay is calculated
     * by multiplying the maximum standard hours by the hourly rate and adding the product of the overtime hours and
     * the hourly rate multiplied by the overtime rate.
     * 
     * @param {float} hours - The number of hours worked. 
     * @param {float} rate - The hourly rate. 
     * @returns {float} - The gross pay.
     */
    const calculateGrossPay = (hours, rate) => {
        if (hours <= MAX_STANDARD_HOURS) {
            return hours * rate;
        } else {
            return (MAX_STANDARD_HOURS * rate) + ((hours - MAX_STANDARD_HOURS) * rate * OVERTIME_RATE);
        }
    }

    /**
     * Calculates the tax amount. 
     * 
     * This function calculates the tax amount based on the gross pay and tax rate. The tax amount is calculated by
     * multiplying the gross pay by the tax rate. 
     * 
     * @param {float} grossPay - The gross pay. 
     * @param {float} taxRate - The tax rate. 
     * @returns {float} - The tax amount. 
     */
    const calculateTaxAmount = (grossPay, taxRate) => grossPay * taxRate;

    /**
     * Calculates the net pay. 
     * 
     * This function calculates the net pay based on the gross pay and tax amount. The net pay is calculated by
     * subtracting the tax amount from the gross pay. 
     * 
     * @param {float} grossPay - The gross pay. 
     * @param {float} taxAmount - The tax amount. 
     * @returns {float} - The net pay. 
     */
    const calculateNetPay = (grossPay, taxAmount) => grossPay - taxAmount;

    /**
     * Displays the results of the calculation. 
     * 
     * This function displays the gross pay, tax amount, and net pay in the corresponding input elements. The values 
     * are formatted as currency using the toLocaleString method. They are set to undefined because the HTML already
     * includes the currency symbol. The minimumFractionDigits option is set to 2 to ensure that the values are
     * displayed with two decimal places. 
     * 
     * @param {float} gross - The gross pay. 
     * @param {float} tax - The tax amount. 
     * @param {float} net - The net pay. 
     * @returns {void}
     */
    const displayResults = (gross, tax, net) => {
        grossPay.value = gross.toLocaleString(undefined, { minimumFractionDigits: 2 });
        taxes.value = tax.toLocaleString(undefined, { minimumFractionDigits: 2 });
        netPay.value = net.toLocaleString(undefined, { minimumFractionDigits: 2 });
    }

    $("#calculate").addEventListener("click", () => {
        if (!validateInputs()) return;

        const rate = getInputNumberValue(hourlyRate);
        const hours = getInputNumberValue(hoursWorked);

        const gross = calculateGrossPay(hours, rate);
        const tax = calculateTaxAmount(gross, TAX_RATE);
        const net = calculateNetPay(gross, tax);

        displayResults(gross, tax, net);
    });
})