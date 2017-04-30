# algorithm 1 from unit 1

numbers = [2, 7, 3, 9, 2]

while True:
	counter = 0

	for idx, number in enumerate(numbers):
	
		try:
			if numbers[idx] > numbers [idx + 1]:
				counter += 1
				numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]
				print(numbers, numbers)
		
		except:
			continue

	if counter == 0:
		print("Success!")
		print(numbers)
		print(counter)
		break



#	if numbers[0] > numbers[1]:
#		numbers[0], numbers[1] = numbers[1], numbers[0]
#		counter += 1
#	if numbers [1] > numbers[2]:
#		numbers[1], numbers[2] = numbers[2], numbers[1]
#		counter += 1
#	if numbers [2] > numbers[3]:
#		numbers[2], numbers[3] = numbers[3], numbers[2]
#		counter += 1
#	if numbers [3] > numbers[4]:
#		numbers[3], numbers[4] = numbers[4], numbers[3]
#		counter += 1