n = 100
print("Fizz buzz counting up to " + str(n))

for count in range(1, n):
	if count % 3 == 0 and count % 5 == 0:
		print("Fizz buzz")
	elif count % 3 == 0:
		print("Fizz")
	elif count % 5 == 0:
		print("Buzz")
	else:
		print(count)
