#Create a decorator function
def decorator_function(org_function):
	print("First, called decorator_function via decorated_function variable initialization")
	def wrapper_function():
		print("Second, wrapper function returned")
		return org_function()
	#A wrapper function return as soon as decorator function called... Wrapper function executed and returns..
	return wrapper_function

def call_org():
	print("Third, I should be executed by some inner_function return value")
	print("Fourth, hmmm... calling org_function via decorator_function")

#expanded form of decorator function instead of using "@"
decorated_function=decorator_function(call_org)
decorated_function()