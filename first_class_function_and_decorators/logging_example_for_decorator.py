import os
def my_logger(orig_func):
	os.mkdir('logs')
	import logging
	logging.basicConfig(filename='logs/{}.log'.format(orig_func.__name__), level=logging.DEBUG)


	def wrapper(*args, **kwargs):
		logging.debug(
			'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
		return orig_func(*args, **kwargs)
	return wrapper


@my_logger
def display_info(name, age):
	print('display function ran with arguments: '+name+", "+str(age))

display_info('chendil', 35)