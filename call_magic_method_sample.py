#Implementing the __call__ magic method in a class causes its instances to become callables -- in other words, those instances now behave like functions. You can use the built-in function callable to test if a particular object is a callable (callable returns True for functions, methods, and objects that have __call__).

class Test(object):
    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        print('-'*80)

t = Test()
t(1, 2, 3)
t(a=1, b=2, c=3)
t(4, 5, 6, d=4, e=5, f=6)
