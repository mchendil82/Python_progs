def kargs_args(*args, **kwargs):
    print(args)
    print(kwargs)

fname="konda chendil"
lname="munireddy"


kargs_args(fname="1",lname="2")
kargs_args("1","2")

#if we pass args and kargs in same function, technically either one is intialized based on data passed... if passed data is keyword argument then it kargs will intialzed else it is series of values args list is intialized
