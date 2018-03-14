n=int(input("Enter the n value"))
k=int(input("Enter the k value"))
sum=0
print("Enter the numbers:")
for i in range(n):
    a=int(input())
    if i<k:
        sum+=a
print(sum)
