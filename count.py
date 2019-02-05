def num_digits(n):
"""
>>> num_digits(12345)
5
>>> num_digits(0)
1
>>> num_digits(-12345)
5
"""
count = 0
if n == 0:
    count += 1
while n > 0 or n < 0:
    if n < 0:
        n = -1*n
    count += 1
    n = n/10
return count

if __name__=="__main__":
import doctest
doctest.testmod(verbose=True)
