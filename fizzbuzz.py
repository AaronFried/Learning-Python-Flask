import sys


if len(sys.argv) < 2:
	n = int(input("Maximum fizz buzz counter: "))
else:
	n = int(sys.argv[1])
	print("Working with {}".format(sys.argv[1]))
	

for count in range(1, n):
	if count % 3 == 0 and count % 5 == 0:
		print("Fizz buzz")
	elif count % 3 == 0:
		print("Fizz")
	elif count % 5 == 0:
		print("Buzz")
	else:
		print(count)