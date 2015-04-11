'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
largest_palindrome = 0

for i in range (100,999):
	for j in range (100,999):
		number = i * j
		number_string = str(number)
		if number_string[0] == number_string[-1] and number_string[1] == number_string[-2]:				#instead of one big line
			if number_string[2] == number_string[-3] and number_string[3] == number_string[-4]:
				if number > largest_palindrome:
					largest_palindrome = number
					first_factor = i
					second_factor = j

print largest_palindrome , first_factor , second_factor , ",woohoo! :D"