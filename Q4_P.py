"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 X 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n):
	n=str(n)
	n_list=[]
	n_reverse=n[::-1]
	n_reverse_list=[]
	for i in n:
		n_list.append(i)
	for x in n_reverse:
		n_reverse_list.append(x)
	for i in range(0,len(n_list)):
	 	if n_list[i] != n_reverse_list[i]:
	 		return False
	return True

def palindrome_from_3d_mult():
	palindromes=[]
	for i in range(100,1000):
		for x in range(100,1000):
			if is_palindrome(i*x)==True:
				palindromes.append(i*x)
	return max(palindromes)


print palindrome_from_3d_mult()


