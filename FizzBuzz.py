def FB(y):

	tracks = [0, 0, 0]


	for x in range(1, 101):
		
		if x % 3 == 0 and x % 5 == 0:
			print("FizzBuzz")
			tracks[2] = 1
			continue
		elif x % 3 == 0:
			print("Fizz")
			tracks[0] = 1
			continue
		elif x % 5 == 0:
			print("Buzz")
			tracks[1] = 1
			continue
		print(x)

	return tracks[y]

