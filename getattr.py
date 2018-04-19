class Test(object):
    hello="ttttt"
    def __init__(self):
        self.a = 'A'
        self.b = 'B'
        self.c=  'C'
        self.d=  'D'
        self.e=  'E'

    def __getattr__(self, name):
        a= 123456
        b= 000000
        return(a,b) 

t = Test()
print('object variables:'+ str(t.__dict__.values()))
print(t.a)
print(t.b)
print(t.c)
print(t.f)
print(type(t.hello))

print(getattr(t, 'd'))
print(getattr(t, 'f'))
print(hasattr(t, 'x'))

