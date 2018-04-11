#Create a decorator function
'''def decorator_function(passed_by_decorator_to_call_wrapper):
	print("First, called decorator_function via decorated_function variable initialization")
	def wrapper_function(*args):
		print("printing args:"+ str(args))
		print("Second, wrapper function returned")
		return passed_by_decorator_to_call_wrapper(*args)
	#A wrapper function return as soon as decorator function called... Wrapper function executed and returns..
	return wrapper_function'''


class decorator_class(object):
	
    def __init__(self, orignal_function):
    	self.orignal_function=orignal_function

#__call__ makes object to be callable just like and so we are able via function_to_call_wrapper()
    def __call__(self, *args):
    	print(args)
    	print("call method executed")
    	return self.orignal_function(*args)


@decorator_class
def function_to_call_wrapper():
	#pass
	print("Third, I should be executed by some inner_function return value")
#calling wrapper function without args
function_to_call_wrapper()

#the above function_to_call_wrapper() is equal to intialize the class object as follows: function_to_callwrapper=decorator_class()

#setting up decorator for wrapper with arguments
@decorator_class
def function_to_call_wrapper(fname,lname):
	print("Name: "+fname + " "+lname)
#Calling wrapper function with *args so that function_to_call_wrapper() accepts dynamic number of arguments
function_to_call_wrapper("Konda Chendil","Munireddy")

#the above function_to_call_wrapper() is equal to intialize the class object as follows: function_to_callwrapper=decorator_class()
#with some attributes
