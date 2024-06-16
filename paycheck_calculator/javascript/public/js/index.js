"use strict";

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

    const getInputValue = (element) => element.value;
    const getInputNumberValue = (element) => parseFloat(getInputValue(element));

    const isValidInput = (value) => value !== "" && !isNaN(value);
    const isValidInputGreaterThanZero = (value) => isValidInput(value) && parseFloat(value) > 0;

    const displayError = (element, message) => { element.textContent = message; }
    const clearError = (element) => { element.textContent = "\u00A0"; }

    const clearElementValue = (element) => { element.value = ""; }
    const clearAllAutoPopulatedInputs = () => {
        const autoPopulatedInputs = [grossPay, taxes, netPay];
        autoPopulatedInputs.forEach((input) => clearElementValue(input));
    }

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

    const calculateGrossPay = (hours, rate) => {
        if (hours <= MAX_STANDARD_HOURS) {
            return hours * rate;
        } else {
            return (MAX_STANDARD_HOURS * rate) + ((hours - MAX_STANDARD_HOURS) * rate * OVERTIME_RATE);
        }
    }

    const calculateTaxAmount = (grossPay, taxRate) => grossPay * taxRate;
    const calculateNetPay = (grossPay, taxAmount) => grossPay - taxAmount;

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