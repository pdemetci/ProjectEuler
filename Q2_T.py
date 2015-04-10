"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four hundred, find the sum of the even-valued terms.
"""

sum = 0
i = 1
Fibonacci=[1]
for i in range(1,400):
	if i == 1:
		Fibonacci.append(1)
	else:
		Fibonacci.append(Fibonacci[i] + Fibonacci[i-1])
print Fibonacci