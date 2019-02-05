v=int(input())
for i in range(2,v):
	if (v%i==0):
		print(v," is not a prime number")
		break
	else:
		print(v," is prime number")
break
