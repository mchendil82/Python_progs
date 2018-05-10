Decorator functions:
===================

1) Decorator functions are used to allow wrapper functions to change without to knowing the user

2) Mainly,it allows to access the scope of inner_functions or wrapper functions from outside

3) Thinks as Decorator function take everything inside its "function_to_call_wrapper" code (immediate function defined under decorator) and its variables passed as available to all the functions under decorator (passed first class function) before the wrapper function... and it return back to function_to_call_wrapper() which is called outside of decorator...  

In simple words, wrapper function get everything (including variables) from function_to_call_wrapper() and executes it's code and  function_to_call_wrapper code (which is executed via "return function_to_call_wrapper()" and it has to be defined like this, inside wrapper) and return back to original function_to_call_wrapper called outside (comibned result of wrapper function and function_to_call_wrapper())


Symbolic representation of decorator:
====================================
    
    def decorator(pass function_to_call_wrapper):
    
    <"some default code of decorator">
    
    <"code of  function_to_call_wrapper" > 
    
    //Pasted or include the code of "function_to_call_wrapper" by decorator (just like "include" concept when @decorator is defined outside and "function_to_call wrapper is also defined and it has to be called to execute wrapper function returned via decortor")..

    def wrapper():

    	< call  function_to_call_wrapper >
    	return function_to_call_wrapper() //execute the function and return by means "()"

    return wrapper //without executing it or just function is returned....

    @decorator
    def function_to_call_wrapper(if any arguments):
    <"some default code of function to call wrapper">             //@decorator and function_to_call_wrapper defined...
    
    function_to_call_wrapper() //to execute wrapper function returned via decortor (from "return wrapper as defined above")
 
	
















decorator function definition and paste it under function calling the wrapper(here function_to_call_wrapper) and that
function is executed both it's code and wrapper function code together... Hence  all the variables are scopped as internal and it is accessible by wrapper function passed "function_to_call_wrapper "and as well as, and "function_to_call_wrapper" see the wrapper function as internal scopped and it is able to callable......


Thus third point says that whatever we change in the wrapper function is dynamically applied by the decorator under the function defined beneath @decorator and it allows user to update  the code in the wrapper or decorator functions... 
