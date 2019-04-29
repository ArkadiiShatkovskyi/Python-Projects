
def smallest_divided_number(minDiv, maxDiv):
	number = maxDiv
	while not is_number_found(number, minDiv, maxDiv):
		number = number + maxDiv
	print(str(number) + " is the smallest number that can be divided by each of the numbers from " + str(minDiv) + " to " + str(maxDiv))

def is_number_found(number, minDiv, maxDiv):
	for d in range(minDiv, maxDiv):
		if number % d != 0:
			return False
	return True

if __name__ == '__main__':
	smallest_divided_number(1, 20)