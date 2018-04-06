Decorator functions:
===================

1) Decorator functions are used to allow wrapper functions to change without to knowing the user
2) Mainly,it allows to access the scope of inner_functions or wrapper functions from outside
3) Thinks as Decorator function take everything inside its decorator function definition and paste it under function calling the wrapper(here function_to_call_wrapper) and that
function is executed both it's code and wrapper function code together... Hence  all the variables are scopped as internal and it is accessible by wrapper function passed "function_to_call_wrapper "and as well as, and "function_to_call_wrapper" see the wrapper function as internal scopped and it is able to callable......


Thus third point says that whatever we change in the wrapper function is dynamically applied by the decorator under the function defined beneath @decorator and it allows user to update  the code in the wrapper or decorator functions... 
