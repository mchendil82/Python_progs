def my_decorator(some_function):

	def wrapper():

		num = 10

		if num == 10:
			print("yes")
		else:
			print("No")

		some_function()
		
		print("Wrapper function executed: "+some_function.__name__)
        
	
	return wrapper

#if this module is executed directly.....
if __name__ == '__main__':
	@my_decorator
	#"__" double underscore is to differentiate or avoid conflict with built-in print function
	def __print():
		print("Decorator executed from main function")
	__print()

