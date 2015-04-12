"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def diff_sq(n):
	sum_sq=0
	sums=0
	for i in range(0,n):
		sum_sq+= (i**2)
		sums +=i
	return (sums**2) - sum_sq

print diff_sq(101)