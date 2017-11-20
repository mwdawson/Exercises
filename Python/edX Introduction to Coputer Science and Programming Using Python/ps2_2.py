# Instructions:
# Now write a program that calculates the minimum fixed monthly payment
# needed in order pay off a credit card balance within 12 months. 
# By a fixed monthly payment, we mean a single number which does not change each month,
# but instead is a constant amount that will be paid each month.
# In this problem, we will not be dealing with a minimum monthly payment rate.
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

monthlyInterestRate = annualInterestRate / 12

def getEndingBalance(balance, monthlyPayment) :
	"""
	Input:
	monthlyPayment - an positive int, which is a multiple of 10 and
	represents the monthly payment
	Returns:
	The ending balance for the given monthly payment
	"""
	i = 1
	while i <= 12:
		interest = (balance - monthlyPayment) * monthlyInterestRate
		balance = balance + interest - monthlyPayment
		i += 1

	return balance

monthlyPayment = 0
endingBalance = getEndingBalance(balance, monthlyPayment)
while(endingBalance > 0):
	monthlyPayment += 10
	endingBalance = getEndingBalance(balance, monthlyPayment)

print("Lowest Payment: " + str(monthlyPayment))


