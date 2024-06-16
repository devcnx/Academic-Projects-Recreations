<?php

/** 
 * Paycheck Calculator 
 * 
 * This is a simple paycheck calculator that calculates the gross pay, taxes, and net pay based on the hourly rate and 
 * the number of hours worked. The tax rate is fixed at 18%. The calculator also takes into account overtime pay for
 * hours worked over 40 hours. 
 */

const TAX_RATE = 0.18;
const MAX_STANDARD_HOURS = 40;
const OVERTIME_RATE = 1.5;

/**
 * Check if the input is valid. 
 * 
 * This function checks if the input is not empty and is a number. If the input is valid, it returns true; otherwise,
 * it returns false.
 *
 * @param mixed $value - The input value to check. 
 * @return boolean - True if the input is valid, otherwise false.s
 */
function isValidInput($value)
{
    return !empty($value) && is_numeric($value);
}

/**
 * Check if the input is a valid number greater than zero. 
 * 
 * This function checks if the input is a valid number and is greater than zero. If the input is valid, it returns true,
 * otherwise, it returns false. Valid numbers are numbers that are not empty, are numeric, and are greater than zero. 
 * 
 * @param mixed $value - The input value to check. 
 * @return boolean - True if the input is a valid number greater than zero, otherwise false.
 */
function isValidInputNumberGreaterThanZero($value)
{
    return isValidInput($value) && $value > 0;
}

/**
 * Calculate the gross pay. 
 * 
 * This function calculates the gross pay based on the hourly rate and the number of hours worked. If the number of
 * hours worked is greater than the maximum standard hours, the function calculates the gross pay with overtime pay. 
 * 
 * @param float $hours - The number of hours worked. 
 * @param float $rate - The hourly rate. 
 * @return float - The gross pay.
 */
function calculateGrossPay($hours, $rate)
{
    if ($hours <= MAX_STANDARD_HOURS) {
        return $hours * $rate;
    } else {
        return (MAX_STANDARD_HOURS * $rate) + (($hours - MAX_STANDARD_HOURS) * $rate * OVERTIME_RATE);
    }
}

/**
 * Calculate the tax amount. 
 * 
 * This function calculates the tax amount based on the gross pay and the tax rate. The tax amount is calculated by
 * multiplying the gross pay by the tax rate. 
 * 
 * @param float $grossPay - The gross pay. 
 * @param float $taxRate - The tax rate.
 * @return float - The tax amount.
 */
function calculateTaxAmount($grossPay, $taxRate)
{
    return $grossPay * $taxRate;
}

/**
 * Calculate the net pay. 
 * 
 * This function calculates the net pay based on the gross pay and the tax amount. The net pay is calculated by
 * subtracting the tax amount from the gross pay. 
 * 
 * @param mixed $grossPay - The gross pay.
 * @param mixed $taxAmount - The tax amount.
 * @return float - The net pay.
 */
function calculateNetPay($grossPay, $taxAmount)
{
    return $grossPay - $taxAmount;
}

// Initialize the variables.
$grossPay = $taxes = $netPay = $hourlyRateError = $hoursWorkedError = "";
$validGrossPay = $validTaxes = $validNetPay = "";

// Check if the form is submitted. 
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $hourlyRate = $_POST['hourlyRate'];
    $hoursWorked = $_POST['hoursWorked'];

    $isValid = true;

    // Validate the hourly rate input.
    if (!isValidInputNumberGreaterThanZero($hourlyRate)) {
        $hourlyRateError = "Enter a valid hourly rate";
        $isValid = false;
    }

    // Validate the hours worked input.
    if (!isValidInputNumberGreaterThanZero($hoursWorked)) {
        $hoursWorkedError = "Enter a valid number of hours worked.";
        $isValid = false;
    }

    // If the inputs are valid, calculate the gross pay, taxes, and net pay.
    if ($isValid) {
        $hourlyRate = floatval($hourlyRate);
        $hoursWorked = floatval($hoursWorked);

        $grossPay = calculateGrossPay($hoursWorked, $hourlyRate);
        $taxes = calculateTaxAmount($grossPay, TAX_RATE);
        $netPay = calculateNetPay($grossPay, $taxes);

        // Store the valid values for redisplay
        $validGrossPay = number_format($grossPay, 2);
        $validTaxes = number_format($taxes, 2);
        $validNetPay = number_format($netPay, 2);
    }
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paycheck Calculator</title>
    <!-- Core Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>

<body class="m-0 p-0">
    <div class="container mt-1 mb-4 pt-3">
        <h3 class="text-center text-uppercase fw-light">Paycheck Calculator</h3>
    </div>

    <div class="container mt-2 w-50 mx-auto">
        <div class="row">
            <div class="col d-flex flex-column justify-content-center align-items-center">
                <form action="" method="POST" class="w-100">

                    <div class="input-group mb-1">
                        <span class="input-group-text w-25 border-0">Hourly Rate</span>
                        <span class="input-group-text border-0">&nbsp;</span>
                        <input type="number" name="hourlyRate" class="form-control text-center" value="<?= $_POST['hourlyRate'] ?? '' ?>" placeholder="Enter the hourly rate." required>
                    </div>

                    <small>
                        <p class="text-danger m-1"><?php echo isset($hourlyRateError) ? $hourlyRateError : '&nbsp;'; ?>
                        </p>
                    </small>

                    <div class="input-group mb-1">
                        <span class="input-group-text w-25 border-0">Hours Worked</span>
                        <span class="input-group-text border-0">&nbsp;</span>
                        <input type="number" name="hoursWorked" class="form-control text-center" value="<?= $_POST['hoursWorked'] ?? '' ?>" placeholder="Enter the number of hours worked." required>
                    </div>

                    <small>
                        <p class="text-danger m-0"><?php echo isset($hoursWorkedError) ? $hoursWorkedError : '&nbsp;'; ?>
                        </p>
                    </small>

                    <div class="input-group mb-1">
                        <span class="input-group-text w-25 border-0">Tax Percentage</span>
                        <span class="input-group-text border-0">&nbsp;</span>
                        <input type="number" name="taxPercentage" class="form-control text-center" value="18.00" readonly>
                        <span class="input-group-text border-0">%</span>
                    </div>

                    <hr class="w-100 border border-dark border-1">

                    <div class="input-group mb-1">
                        <span class="input-group-text w-25 border-0">Gross Pay</span>
                        <span class="input-group-text border-0">$</span>
                        <input type="text" id="grossPay" class="form-control text-center" value="<?php echo $validGrossPay; ?>" readonly>
                    </div>

                    <div class="input-group mb-1">
                        <span class="input-group-text w-25 border-0">Taxes</span>
                        <span class="input-group-text border-0">$</span>
                        <input type="text" id="taxes" class="form-control text-center" value="<?php echo $validTaxes; ?>" readonly>
                    </div>

                    <div class="input-group mb-1">
                        <span class="input-group-text w-25 border-0">Net Pay</span>
                        <span class="input-group-text border-0">$</span>
                        <input type="text" id="netPay" class="form-control text-center" value="<?php echo $validNetPay; ?>" readonly>
                    </div>

                    <div class="w-100">
                        <button type="submit" class="btn btn-primary mt-2 w-100">Calculate</button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <!-- Core Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>

</html>