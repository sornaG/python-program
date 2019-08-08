a = int(input("Please Enter First Number of an A.P Series: : "))
n = int(input("Please Enter the Total Numbers in this A.P Series: : "))
d = int(input("Please Enter the Common Difference : "))

total = (n * (2 * a + (n - 1) * d)) / 2
tn = a + (n - 1) * d
i = a
print("\nThe tn Term of Arithmetic Progression Series = " , tn)
print("The Sum of Arithmetic Progression Series : ")
while(i <= tn):
    if(i != tn):
        print("%d + " %i, end = " ")
    else:
        print("%d = %d" %(i, total))
    i = i + d
