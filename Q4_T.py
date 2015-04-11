'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


for i in range (100,999):
	for j in range (100,999):
		number = i * j
		number_string = str(number)
		if number_string[0] == number_string[-1] and number_string[1] == number_string[-2] and number_string[2] == number_string[-3]:
			largest_palindrome = number

print largest_palindrome , ",woohoo! :D"