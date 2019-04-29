import math

def summary_prime(count):
	return sum(get_prime_number(count))

def get_prime_number(number):
	numbers = []
	testNum = 1
	while testNum < number:
		testNum = testNum + 1
		if if_prime_number(testNum):
			numbers.append(testNum)
	return numbers

def if_prime_number(number):
	for n in range(2, 11):
		if n != number and number % n == 0:
			return False
	return True

if __name__ == '__main__':
	print(summary_prime(2000000))
