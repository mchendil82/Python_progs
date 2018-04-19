#This is use case of decorator to track how many function is called using decorator
#We call display function and decorator my_logger function calls and record how many time it is called by creating
#in the name of calling function... here it will create logs under "logs/display_info.log"



import os
def my_logger(orig_func):
	if not os.path.exists('logs'):
		os.mkdir('logs')
	import logging
	logging.basicConfig(filename='logs/{}.log'.format(orig_func.__name__), level=logging.DEBUG)


	def wrapper_logger(*args, **kwargs):
		logging.debug(
			'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
		return orig_func(*args, **kwargs)
	return wrapper_logger

import time
def my_timer(orig_func):
	def wrapper_timer(*args, **kwargs):
		t1=time.time()
		result=orig_func(*args, **kwargs)
		t2= time.time() - t1
		print('{} ran in: {} sec'.format(orig_func.__name__, t2))
		return result
	return wrapper_timer


#Here we have 2 decorators "my_logger" and "mytimer".. 
#and we are going to talk about a problem with stacking multiple decorators.. 

#The decorator which in lowest level (here it is @my_timer) is executed first and then next in queue.. 
#Here my_timer will be executed first and that function retunred or reuslts will be
#passed to next decorators which will give different results(to @my_logger)... 
#remember a decorator just copies the immediate below function code to decorator function

#expectation is here is my_logger and my_timer is to execute the immediate below (i.e. display_info function) produce results
#my_logger should create "display_info.log" (see 3rd line) but instead it will be "wrapper_timer.log" as my_timer decorator returns "wrapper_timer" as function name
#my_logger which creates the wrapper_timer.log... 

#if I (reverse it) stack "my_timer" first and "my_logger", display_info.log will be created but "wrapper_logger" function will be returned to timer decorator
#hence the print satement at 27 line will print wrapper_logger function "as ran" and returns and executes the wrapper_logger instead of wrapper_timer...

#comment either of decorator and see the difference... and enable both decorators and see the difference....



@my_logger
@my_timer
def display_info(name, age):
	time.sleep(1)
	print('display function ran with arguments: '+name+", "+str(age))

display_info('chendil', 35)