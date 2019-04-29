def get_prime_number(number):
	n = 0
	testNum = 1
	while n != number:
		testNum = testNum + 1
		if if_prime_number(testNum):
			n = n + 1
	print(testNum)

def if_prime_number(number):
	for n in range(2, 11):
		if n != number and number % n == 0:
			return False
	return True
	
if __name__ == '__main__':
	get_prime_number(10001)