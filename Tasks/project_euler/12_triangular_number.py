import math

def triangle_numbers(numbers):
	result = []
	for i in range(1, numbers + 1):
		number = int(0.5 * i * (i + 1))
		div = dividers(number)
		result.append(convert_to_str(number, div))
	return result

def dividers(number):
	divs = []
	for n in range(1, number + 1):
		if number % n == 0:
			divs.append(int(n))
	return divs

def convert_to_str(number, div_numbers):
	result = ""
	result += str(number) + ": "
	for n in div_numbers:
		result += str(n) + ", "
	return result[:len(result) - 2]

def to_string(string):
	for s in string:
		print(s + "\n")

if __name__ == '__main__':
	res = triangle_numbers(7)
	to_string(res)
