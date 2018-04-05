#Create a decorator function
def decorator_function(passed_by_decorator_to_call_wrapper):
	print("First, called decorator_function via decorated_function variable initialization")
	def wrapper_function():
		print("Second, wrapper function returned")
		return passed_by_decorator_to_call_wrapper()
	#A wrapper function return as soon as decorator function called... Wrapper function executed and returns..
	return wrapper_function

def function_to_call_wrapper():
	#pass
	print("Third, I should be executed by some inner_function return value")
	print("Fourth, hmmm... calling org_function via decorator_function")

#expanded form of decorator function instead of using "@"
decorateeeeed_function=decorator_function(function_to_call_wrapper)
decorateeeeed_function()