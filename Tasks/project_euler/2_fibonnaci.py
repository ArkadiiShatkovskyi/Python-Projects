
def fibonachi_rec(b1, b2, d, depth):
	num = b1 + b2
	if d == depth:
		print(num)
		return
	print(num)
	return fibonachi(b2, num, d+1, depth)

def fibonachi_iter(b1, b2, depth):
	for d in range(0, depth):
		num = b1 + b2
		print(num)
		b1 = b2
		b2 = num

if __name__ == '__main__':
	#fibonachi_rec(0, 1, 0, 10)
	fibonachi_iter(0, 1, 30)