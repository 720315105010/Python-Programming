try:
	count=0
	n=int(raw_input())
	m=int(raw_input())
	for i in range (n,m+1):
		c=0
		for j in range (1,i+1):
			if (i%j==0):
				c=c+1
			else :
				pass
		if(c==2):
			count=count+1
	print count
except:
	print "Invalid" 
