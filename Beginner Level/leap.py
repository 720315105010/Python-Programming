print("Enter the Year:")
s=int(input())
if (s % 4) == 0 :
  if (s % 100) == 0 :
    if (s % 400) == 0 :
      print(s,"is a LEAP year")
else :
 print(s,"is not a leap year")
