#Create a function make_counter() that returns a function that, when called, increments and returns a counter variable. The counter should start at 0 and increment by 1 each time the function is called.

def make_counter():
	counter = 0
	def increment():
		nonlocal counter;
		counter += 1
		print(counter)
	return increment

result = make_counter()
result()

result()

result()
