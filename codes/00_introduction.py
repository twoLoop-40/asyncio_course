
def recur_fib(n):
	if n <= 1:
		return n
	else:
		return recur_fib(n-1) + recur_fib(n-2)


def main():
	fib = recur_fib(40)
	print('Hello world')


if __name__ == '__main__':
	main()