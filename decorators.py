def my_decorator(func):
	def inner():
		print("This is a decorator message...")
		func()
	return inner

# # What happens under the hood
# def my_func():
# 	print("I'm a simple function...")
# my_func = my_decorator(my_func)

@my_decorator
def my_func():
	print("I'm a simple function...")
my_func()

