class test(object):
#   print(object.global())
   def __init__(self, arg):
    self.arg=arg
    print(arg)
   def display(self):
    print(self.arg)

obj=test("5")
obj.display()
