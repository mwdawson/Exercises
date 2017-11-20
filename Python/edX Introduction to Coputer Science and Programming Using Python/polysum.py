# Instructions:
# A regular polygon has 'n' number of sides. Each side has length 's'.
# * The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
# * The perimeter of a polygon is: length of the boundary of the polygon
# Write a function called 'polysum' that takes 2 arguments, 'n' and 's'. 
# This function should sum the area and square of the perimeter of the regular polygon.
# The function returns the sum, rounded to 4 decimal places.

import math

def polysum(n, s):
	"""
	Input:
	n - an positive int representing the number of sides
	s - a positive int or float representing the length of each side
	Returns:
	The sum of the area and the squared perimeter or a regular polygon
	with n sides, each with length s
	"""

	# Calculate the perimeter squared and area
	perimeter_squared = (n*s)**2
	area = (0.25*n*s**2) / (math.tan(math.pi/n))

	# Round output to 4 decimal places
	output = round(perimeter_squared + area, 4)

	return output

