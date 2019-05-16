import math

def digit_sum(number, power):
	num = int(math.pow(number, power))
	numbers = [int(i) for i in str(num)]
	result = 0
	for n in numbers:
		result += n
	return result

if __name__ == '__main__':
	number = 2
	power = 1000
	print("Result of " + str(number) + "^" + str(power) + ": " 
		+ str(digit_sum(number, power)))