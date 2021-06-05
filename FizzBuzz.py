def FB():

	#not really sure what's happening, its treating fizzbuzz as an integer instead of an array
	tracks = [0, 0, 0]


	for x in range(1, 101):
		
		if x % 3 == 0:
			print("Fizz")
			tracks[0] = 1
			continue
		print(x)

	return tracks

