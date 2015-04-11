"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def is_prime(n):
	divisors=[]
	for i in range(2,n):
		if n%i == 0:
			divisors.append(i)
	if divisors == []:
		return True
	else: return False

def divisors(n):
	divisor=[]
	for i in range(2,n):
		if n%i == 0 and is_prime(i) :
			divisor.append(i)
	return max(divisor)

print divisors(3395)
