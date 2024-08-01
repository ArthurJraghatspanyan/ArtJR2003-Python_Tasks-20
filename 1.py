# Write a function make_multiplier_of(n) that takes an integer n and returns a function that multiplies its argument by n. Demonstrate its use with several examples.

def make_multiplier_of(n):
	def multiply(m):
		print(m * n)
	return(multiply)

res1 = make_multiplier_of(4)
res1(2)

res2 = make_multiplier_of(5)
res2(20)

res3 = make_multiplier_of(10)
res3(100)
