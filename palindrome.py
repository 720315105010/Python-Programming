n=int(raw_input())
sum=0
k=n
while(n!=0):

	a=n%10
	sum=sum*10+a
	n=n/10
if(sum==k):
	print("palindrome")
else:
	print("not palindrome")
	
