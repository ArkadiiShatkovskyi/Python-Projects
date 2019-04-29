def getPalindromics():
	palindromics = []
	num1 = []
	num2 = []
	for n1 in range(100, 998):
		for n2 in range(100, 999):
			if isPalindromic(str(n1*n2)) and not isOnList(n1*n2, palindromics):
				num1.append(n1)
				num2.append(n2)
				palindromics.append(n1*n2)
	if len(palindromics) > 0:
		resultIndex = palindromics.index(max(palindromics))
		print("Result: " + str(num1[resultIndex]) + " * " + str(num2[resultIndex]) + 
			" = " + str(palindromics[resultIndex]))
	return -1

def isPalindromic(number):
	if len(number) % 2 != 0:
		return False
	else:
		fp = number[:int(len(number)/2)]
		sp = number[int(len(number)/2):]
		return fp == sp[::-1]

def isOnList(number, l):
	try:
		l.index(number)
	except ValueError as e:
		return False
	return True

if __name__ == '__main__':
	#isPalindrome(str(int(91*99)))
	getPalindromics()