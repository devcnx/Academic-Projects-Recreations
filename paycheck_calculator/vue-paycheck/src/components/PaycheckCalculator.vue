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
    import { ref } from 'vue';

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

    const isValidInput = (value) => value !== '' && !isNaN(value);
    const isValidInputGreaterThanZero = (value) => isValidInput(value) && parseFloat(value) > 0;

    const clearElementValue = (element) => element.value = '';
    const clearAllAutoPopulatedInputs = () => {
        const autoPopulatedInputs = [grossPay, taxes, netPay];
        autoPopulatedInputs.forEach((input) => clearElementValue(input));
    }

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