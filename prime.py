number=int(raw_input())
for i in range(2, number):
			if number%i == 0:
				print(number, "is not a prime number")
				break
else:
			print(number, "is a prime number")
