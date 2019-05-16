import inflect

def count_numbers(number):
	p = inflect.engine()
	result = 0
	for i in range(1, number + 1):
		result += len(p.number_to_words(i).replace(" ", ""))
	return result

if __name__ == '__main__':
	number = 150
	print("Sum from 1 to " + str(number) + ": " + str(count_numbers(number)))