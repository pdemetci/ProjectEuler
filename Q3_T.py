"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
list_of_prime_factors = []
max_prime_factor = 1
number = 600851475143
sum_list=1
product = 1

for i in range (1,100000):
	if number % i == 0:
		number = number / i
		max_prime_factor = i
		list_of_prime_factors.append(i)

print list_of_prime_factors

for i in range(0,len(list_of_prime_factors)):
	product = product * list_of_prime_factors[i]
	if product == 600851475143:
		print max_prime_factor
		print "Woohoo!!! :D "