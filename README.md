# Python_progs
Python Args and Kargs
===================
1) Python args and kargs are used to pass dynamic list of variables to a function
2) https://code.tutsplus.com/articles/understanding-args-and-kwargs-in-python--cms-29494
3) args and kargs are custom keyword and we can use any names but tradiationally "kargs" and "args" are used and easy for other developers identitfy....


self keyword:
============

1) self is keyword which indicates that object itself passed as default argument to a function when  a object is intialized outside of a class
2) self keyword can be in any name  but tradiationally this is the name used to commonly to store a object 
3) once the variables are stored in the object as intance variables  as self.variable=value rather just a variable=value inside the class function, it can be used throught class

__init__
========
Constructors are usually to intialize some default values to an object

1) __init__ is used default to intialize the object (kind of constructor but technically it is not constructor since constructor (say in c++)  should create and intialize by a function(constructor function) with same name of class )but whereas in python object is created by when you intialize instance and passed to a function or __init__ function which intialize the object with some variables

In general constructor is construct an object (creates object in a memory and allocate variables placement in the moemory.. See how in jave, declaration(pointer of memory address), Initialization (put the valuest to pointer referenced memory) and Instantiation (return memory address for direct use)). These all goes hand in hand togehter because constructor call function will look for "exactly class named function" and executest it to put the value in the object referenced memory (Initialization) and return the object with value (Instantiation) basically object with referenced memory address.

but in python when we say foo=Test(), see object referenced and created here already and then it is available to just intialize the values to fill the memory using __init__ function to initialize the values.


There are three pieces of terminology associated with this topic: declaration, initialization and instantiation.

**In Java:**

Instantiation

This is when memory is allocated for an object. This is what the new keyword is doing. A reference to the object that was created is returned from the new keyword.

Initialization

This is when values are put into the memory that was allocated. This is what the Constructor of a class does when using the new keyword.

A variable must also be initialized by having the reference to some object in memory passed to it.

Declaration

This is when you state to the program that there will be an object of a certain type existing and what the name of that object will be.

Example of Initialization and Instantiation on the same line

SomeClass s; // Declaration
s = new SomeClass(); // Instantiates and initializes the memory and initializes the variable 's'

Example of Initialization of a variable on a different line to memory

void someFunction(SomeClass other) {
    SomeClass s; // Declaration
    s = other; // Initializes the variable 's' but memory for variable other was set somewhere else
}
I would also highly recommend reading this article on the nature of how Java handles passing variables.

**But in python**

 in python everything is an object so there is no concept constructing an object
https://www.programiz.com/article/python-self-why

__call__ -> Generally Object is not callable... Unless you use __call__ the object can't be as function.... usecase would decorator object called as functions...
