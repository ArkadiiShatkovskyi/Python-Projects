import math

def difference(first_num, second_num):
		return square_of_the_sum(first_num, second_num) - sum_of_the_squares(first_num, second_num)

def sum_of_the_squares(n1, n2):
	res = 0
	for n in range(n1, n2 + 1):
		res = res + math.pow(n, 2)
	return res

def square_of_the_sum(n1, n2):
	res = 0
	for n in range(n1, n2 + 1):
		res = res + n
	return math.pow(res, 2)

if __name__ == '__main__':
	print(int(difference(1, 1000)))