# example 1
def rev_str(my_str):
	for char in my_str[::-1]:
		yield char

for i in rev_str("hello world"):
	print(i)

print("\n--------------\n")

# example 2
def my_gen():
	n = 1
	# print(f"n value : {n}")
	yield n
	n += 1

	# print(f"n value : {n}")
	yield n
	n += 1

	# print(f"n value : {n}")
	yield n
	n += 1

	# print(f"n value : {n}")
	yield n
	n += 1

gen = my_gen()
for item in gen:
	print(item)
