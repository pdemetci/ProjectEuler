"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
list_of_prime_factors = []
max_prime_factor = 1
number = 24
sum_list=1
product = 1

for i in range (1,1000000):
	if number % i == 0:
		number = number / i
		max_prime_factor = i
		list_of_prime_factors.append(i)

print list_of_prime_factors	

for i in range (0,len(list_of_prime_factors)-1):
	if list_of_prime_factors[i] % list_of_prime_factors[-i] == 0:
		list_of_prime_factors.remove(list_of_prime_factors[i-1])
		max_prime_factor = list_of_prime_factors[-1]

print list_of_prime_factors

for i in range(0,len(list_of_prime_factors)):
	product = product * list_of_prime_factors[i]
	if product == number:
		print max_prime_factor
		print "Woohoo!!! :D "