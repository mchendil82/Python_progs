#first_class functions and callable patterns

def outer_function():

	def inner_function(msg):
		print(msg)
#function retunred (note: without curl bracketes())
	return inner_function

#inner_function returned here via outer function and it is our wrapper (i.e. is inner function)
#outer function is a decorator around the wrapper and and the wrapper can be changed or updated 
#without knowing to user who is using outer funtion
hi_func=outer_function()
bye_func=outer_function()


hi_func("hi - Result of hi function")
bye_func("bye- Result of bye function")