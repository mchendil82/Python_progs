x=2
y=3

res=lambda x,y: True if x > y else False

print(res) # lambda is function shorter version and it return a function.  This print function memory id somehting like: <function <lambda> at 0x01BD7FA0>
print(res(x,y)) #this prints actual results "False"

res1=lambda x,y: print("true") if x > y else print("false")  #we are not returning anything here but we are just printing here
print(res1(x,y)) #Since lambda is function it always returns value.. But here we are justing print "true" or "false".. By default lambda will return "None" and also prints the value. At the same,
                # we can't comebine return something and print something like this, "lambda x,y: x print(true) if x > y else print("false") y".. we are trying to return x or y based on expression but it will thrown error 
                # as lambda can accept either return or some print/other statements.

n=[4,3,2,1]
print(list(map(lambda  x: x*x, n))) #map applies a function to all elements in a list and return map iterable list object

print(list(filter(lambda x: x > 3, n))) #filter will also apply function on the list values but filter results based on expression and only provide list actual values which turns to be turn
print(list(map(lambda x: x > 3, n))) #same expression is also applied to map function, wchih applies each elment but gives all as boolean value rather actual values because we are evulating values 
                                     #but map will be perfect for calcuations as it is mandated to provide all results for each element.. consider we are using, "if condition"

#both fileter and maps also returns iterable object

from functools import reduce

l=[1,2,3,4,5]

#factorial results for reduce function. it picks x,y from list element gets product of x and y and then applies same product to the next element
print(reduce(lambda x,y: x*y, l))

#calculate factorial of a variable using reduce
x=5
import functools, operator
functools.reduce(lambda x,y: x*y, range(1, x))








