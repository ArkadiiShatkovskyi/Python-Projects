def collatz_sequence(number):
	temp_Number = number
	result = str(temp_Number) + ', ' 
	while temp_Number != 1:
		if temp_Number % 2 == 0:
			temp_Number = int(temp_Number / 2)
		else:
			temp_Number = int(temp_Number * 3) + 1
		result += str(temp_Number) + ', '
	return result[:-2]

if __name__ == '__main__':
	print(collatz_sequence(17))