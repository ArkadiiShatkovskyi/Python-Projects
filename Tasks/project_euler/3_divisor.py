import copy

def divisor(number):
	divisors = []
	temp_num = number
	while not check_if_end(divisors, temp_num):
		res = div_number(temp_num)
		if res is None:
			return divisors
		temp_num = int(res[1])
		divisors.append(res[0])
	return divisors

def div_number(number):
	if number != 0:
		for i in range(2, number):
			if number % i == 0:
				return [i, number/i]
		return [number, 0]

def check_if_end(divisors, number):
	result = 1
	for el in divisors:
			result = result * el
	return result == number

if __name__ == '__main__':
	result = divisor(103245)
	print(str(result))