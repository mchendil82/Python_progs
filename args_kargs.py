def kargs_args(*args, **kwargs):
    print(args)
    print(kwargs)

#name="konda chendil"
#lname="munireddy"


kargs_args(fname="1",lname="2")
kargs_args("1","2")

#if we pass args and kargs in same function, technically either one is intialized based on data passed... if passed data is keyword argument then it kargs will intialzed else it is series of values args list is intialized
#some interesting thing about args and krags https://stackoverflow.com/questions/61746117/how-to-pass-kwargs-with-the-same-name-as-a-positional-argument-of-a-function