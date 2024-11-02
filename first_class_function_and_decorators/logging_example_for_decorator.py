#This is use case of decorator to track how many function is called using decorator
#We call display function and decorator first_logger_func_decorator function calls and record how many time it is called by creating
#in the name of calling function... here it will create logs under "logs/display_info.log"

from functools import wraps

import os
def first_logger_func_decorator(orig_func):
	if not os.path.exists('logs'):
		os.mkdir('logs')
	import logging
	logging.basicConfig(filename='logs/{}.log'.format(orig_func.__name__), level=logging.DEBUG)

	@wraps(orig_func)
	def first_func_wrapper(*args, **kwargs):
		logging.debug(
			'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
		return orig_func(*args, **kwargs)
	return first_func_wrapper

import time
def second_timer_func_decorator(orig_func):
	
	@wraps(orig_func)
	def second_func_wrapper(*args, **kwargs):
		t1=time.time()
		result=orig_func(*args, **kwargs)
		t2= time.time() - t1
		print('{} ran in: {} sec'.format(orig_func.__name__, t2))
		return result
	return second_func_wrapper


#Here we have 2 decorators "first_logger_func_decorator" and "second_timer_func_decorator".. 
#and we are going to talk about a problem with stacking multiple decorators...
# first_logger_func_decorator and second_timer_func_decorator should use "display info " function independently and execute
#but it will not see the reasons as follows:

#The decorator which in lowest level (here it is @second_timer_func_decorator) is executed first and then next in queue.. 
#Here second_timer_func_decorator will be executed first and that function returned or reuslts will be
#passed to next decorators which will give different results(to @first_logger_func_decorator)... 
#remember a decorator just copies the immediate below function code to decorator function
#or you can say that technically as follows:
# display_info=second_timer_func_decorator(display_info)
# and in turn:
# second_timer_func_decorator=first_logger_func_decorator(second_timer_func_decorator)... 
#which means process vice is wrong and which we don't want..

#expectation is here is first_logger_func_decorator and second_timer_func_decorator is to execute the immediate below (i.e. display_info function) produce results
#first_logger_func_decorator should create "display_info.log" (see 3rd line) but instead it will be "second_func_wrapper.log" as second_timer_func_decorator decorator returns "second_func_wrapper" as function name
#first_logger_func_decorator which creates the second_func_wrapper.log... 

#if I (reverse it) stack "second_timer_func_decorator" first and "first_logger_func_decorator", display_info.log will be created but "first_func_wrapper" function will be returned to timer decorator
#hence the print satement at 27 line will print "first_func_wrapper" function "as ran in the print staement" and returns and executes the first_func_wrapper instead of second_func_wrapper...

#comment either of decorator and see the difference... and enable both decorators and see the difference....

#(see previous commit befor seeing the below solution)
#to avoid decorator stacking issues, we use @wraps() to wrap each wrapper functions in it's own space and preserve details
#and execute indepedently..... rather passing result of one function to another function which is unnecessary... 


@first_logger_func_decorator
@second_timer_func_decorator
def display_info(name, age):
	time.sleep(1)
	print('display function ran with arguments: '+name+", "+str(age))

display_info('chendil', 35)