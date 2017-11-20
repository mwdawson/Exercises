# Instructions:
# Write a program to calculate the credit card balance after one year 
# if a person only pays the minimum monthly payment required by the credit
# card company each month.
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal
# For each month, calculate statements on the monthly payment and remaining balance.
# At the end of 12 months, print out the remaining balance.

monthlyInterestRate = annualInterestRate / 12
i = 1
while i <= 12:
	minimumPayment = balance * monthlyPaymentRate
	interest = (balance - minimumPayment) * monthlyInterestRate
	balance = balance + interest - minimumPayment
	i += 1

print("Remaining balance: " + str(round(balance, 2)))

