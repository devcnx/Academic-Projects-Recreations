<template>
    <div class="container mt-0 mb-4">
        <h3 class="text-center text-uppercase fw-light">Paycheck Calculator</h3>
    </div>

    <div class="container mt-2 w-75 mx-auto">
        <div class="row">
            <div class="col d-flex flex-column justify-content-center align-items-center">

                <div class="input-group mb-1">
                    <span class="input-group-text w-25 border-0">Hourly Rate</span>
                    <span class="input-group-text border-0">&nbsp;</span>
                    <input type="number" v-model="hourlyRate" class="form-control text-center"
                        placeholder="Enter the hourly rate" />
                </div>

                <small>
                    <p class="text-danger m-0">{{ hourlyRateError }}</p>
                </small>

                <div class="input-group mb-1">
                    <span class="input-group-text w-25 border-0">Hours</span>
                    <span class="input-group-text border-0">&nbsp;</span>
                    <input type="number" v-model="hoursWorked" class="form-control text-center"
                        placeholder="Enter the number of hours worked" />
                </div>

                <small>
                    <p class="text-danger m-0">{{ hoursWorkedError }}</p>
                </small>

                <div class="input-group mb-1">
                    <span class="input-group-text w-25 border-0">Tax Percentage</span>
                    <span class="input-group-text border-0">&nbsp;</span>
                    <input type="number" v-model="taxPercentage" class="form-control text-center" value="18.00"
                        readonly />
                    <span class="input-group-text border-0">%</span>
                </div>

                <hr class="w-100 border border-dark border-1">

                <div class="input-group mb-1">
                    <span class="input-group-text w-25 border-0">Gross Pay</span>
                    <span class="input-group-text border-0">$</span>
                    <input type="text" v-model="grossPay" class="form-control text-center" readonly />
                </div>

                <div class="input-group mb-1">
                    <span class="input-group-text w-25 border-0">Taxes</span>
                    <span class="input-group-text border-0">$</span>
                    <input type="text" v-model="taxes" class="form-control text-center" readonly />
                </div>

                <div class="input-group mb-1">
                    <span class="input-group-text w-25 border-0">Net Pay</span>
                    <span class="input-group-text border-0">$</span>
                    <input type="text" v-model="netPay" class="form-control text-center" readonly />
                </div>

                <button @click="calculatePaycheck" class="btn btn-primary w-100 text-uppercase">Calculate</button>

            </div>
        </div>
    </div>
</template>

<script setup>

    // Import the ref function from the Vue Composition API.
    import { ref } from 'vue';

    // Declare the reactive variables.
    const hourlyRate = ref('');
    const hoursWorked = ref('');
    const taxPercentage = ref(18.00);
    const grossPay = ref('');
    const taxes = ref('');
    const netPay = ref('');

    const hourlyRateError = ref('');
    const hoursWorkedError = ref('');

    const taxRate = 0.18;
    const maxStandardHours = 40;
    const overtimeRate = 1.5;

    /**
     * Check if the input value is valid. 
     * 
     * This function checks that the input value is not an empty string and is a number. If the input value is not
     * valid, the function returns false. Otherwise, it returns true. 
     * 
     * @param {String} value - The input value to check. 
     * @returns {Boolean} - True if the input value is valid, false otherwise. 
     */
    const isValidInput = (value) => value !== '' && !isNaN(value);

    /**
     * Check if the input value is greater than zero. 
     * 
     * This function checks that the input value is valid and greater than zero. If the input value is not valid or
     * less than or equal to zero, the function returns false. Otherwise, it returns true. 
     * 
     * @param {String} value - The input value to check.
     * @returns {Boolean} - True if the input value is valid and greater than zero, false otherwise.
     */
    const isValidInputGreaterThanZero = (value) => isValidInput(value) && parseFloat(value) > 0;

    /**
     * Clear the value of an input element. 
     * 
     * This function sets the value of the input element to an empty string. 
     * 
     * @param {HTMLInputElement} element - The input element to clear. 
     */
    const clearElementValue = (element) => element.value = '';

    /**
     * Clear the value of all auto-populated inputs. 
     * 
     * This function clears the value of the gross pay, taxes, and net pay inputs. 
     */
    const clearAllAutoPopulatedInputs = () => {
        const autoPopulatedInputs = [grossPay, taxes, netPay];
        autoPopulatedInputs.forEach((input) => clearElementValue(input));
    }

    /**
     * Calculate the paycheck. 
     * 
     * This function calculates the gross pay, taxes, and net pay based on the hourly rate, number of hours worked, and
     * tax percentage. If the hourly rate or number of hours worked is not valid, the function displays an error message
     * and clears the auto-populated inputs. If the inputs are valid, the function calculates the paycheck values and
     * displays them in the corresponding input elements of the form.
     * 
     * The gross pay is calculated as a product of the hourly rate and the number of hours worked. If the number of
     * hours worked exceeds the maximum standard hours, the function calculates the gross pay as the sum of the product
     * of the maximum standard hours and the hourly rate and the product of the overtime hours and the hourly rate
     * multiplied by the overtime rate. 
     * 
     * The taxes are calculated as a product of the gross pay and the tax rate. 
     * 
     * The net pay is calculated as the difference between the gross pay and the taxes. 
     * 
     * The paycheck values are displayed in the corresponding input elements of the form with two decimal places. 
     * 
     * The function does not return a value. 
     * 
     * @returns {Void}
     */
    const calculatePaycheck = () => {
        let isValid = true;

        if (!isValidInputGreaterThanZero(hourlyRate.value)) {
            hourlyRateError.value = 'Enter a valid hourly rate.';
            isValid = false;
            clearAllAutoPopulatedInputs();
        } else {
            hourlyRateError.value = '\u00A0';
        }

        if (!isValidInputGreaterThanZero(hoursWorked.value)) {
            hoursWorkedError.value = 'Enter a valid number of hours worked.';
            isValid = false;
            clearAllAutoPopulatedInputs();
        } else {
            hoursWorkedError.value = '\u00A0';
        }

        if (!isValid) { return; }

        const rate = parseFloat(hourlyRate.value);
        const hours = parseFloat(hoursWorked.value);

        const grossPayValue = hours <= maxStandardHours ? hours * rate : maxStandardHours * rate + (hours - maxStandardHours) * rate * overtimeRate;
        const taxesValue = grossPayValue * taxRate;
        const netPayValue = grossPayValue - taxesValue;

        grossPay.value = grossPayValue.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
        taxes.value = taxesValue.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
        netPay.value = netPayValue.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    }
</script>