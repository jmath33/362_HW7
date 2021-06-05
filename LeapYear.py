def leap(in_year):

	if((in_year % 4) == 0):
		if((in_year % 100) == 0):
			print("%d is not a leap year" %in_year)
			return 0
		else:
			print("%d is a leap year!" %in_year)
			return 1
	else:
		print("%d is not a leap year." %in_year)
		return 0
