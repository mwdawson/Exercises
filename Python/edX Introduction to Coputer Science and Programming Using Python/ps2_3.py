# Instructions:
# Write a program that uses these bounds and bisection search 
# (for more info check out the Wikipedia page on bisection search)
# to find the smallest monthly payment to the cent (no more multiples of $10)
# such that we can pay off the debt within a year. 
# Try it out with large inputs, and notice how fast it is 
# (try the same large inputs in your solution to Problem 2 to compare!).
# Produce the same return value as you did in Problem 2.

monthlyInterestRate = annualInterestRate / 12

def getEndingBalance(balance, monthlyPayment) :
	"""
	Input:
	monthlyPayment - an positive float, with up to 2 decimals which
	represents the monthly payment
	Returns:
	The ending balance for the given monthly payment
	"""
	monthlyInterestRate = annualInterestRate / 12
	i = 1
	while i <= 12:
		interest = (balance - monthlyPayment) * monthlyInterestRate
		balance = balance + interest - monthlyPayment
		i += 1

	return round(balance, 2)

monthlyPaymentLowerBound = balance / 12
monthlyPaymentUpperBound = (balance*(1 + monthlyInterestRate)**12) / 12.0

monthlyPayment = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2
endingBalance = getEndingBalance(balance, monthlyPayment)

while abs(endingBalance) > 0.01:
	if endingBalance > 0.01:
		monthlyPaymentLowerBound = monthlyPayment
		monthlyPayment = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2
		endingBalance = getEndingBalance(balance, monthlyPayment)
	elif endingBalance < -0.01:
		monthlyPaymentUpperBound = monthlyPayment
		monthlyPayment = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2
		endingBalance = getEndingBalance(balance, monthlyPayment)

print("Lowest payment: " + str(round(monthlyPayment, 2)))
