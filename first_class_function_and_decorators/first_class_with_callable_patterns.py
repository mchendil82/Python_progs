#first_class functions and callable patterns

def outer_function():

	def inner_function(msg):
		print(msg)
#function retunred (note: without curl bracketes())
	return inner_function

#inner_function returned(returns a variable) here via outer function and it is our wrapper
#outer function is kind of a decorator around the wrapper and the wrapper can be changed or updated 
#without knowing to user who is using outer function
hi_func=outer_function()
bye_func=outer_function()


hi_func("hi - Result of hi function")
bye_func("bye- Result of bye function")