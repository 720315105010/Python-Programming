print("Enter 3 numbers")
num1=input()
num2=input()
num3=input()
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("Largest=",largest)
