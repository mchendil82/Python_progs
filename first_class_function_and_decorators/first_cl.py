def parent(num):
	
	def first_child():
		return "Printing from the first_child() function"
	def second_child():
			return "Printing from the second_child() function"
	#first_child=1111
	try:
		assert num == 10
		return first_child
	except AssertionError:
		return second_child

foo=parent(10)
bar=parent(11)
print(foo)
print(bar)

print(foo())
print(bar())

#Assert samples
t=True
assert 10==10
assert t is False 