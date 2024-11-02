#__getattr__ function=get by default store the variable with values defined in  __getattr__ function and 
#it will not throw the "Attribute not defined error".. 
#This can be used to store values by the user(kind of dynammically ) which is NOT defined in the program


#getattr propety decorators(python builtin property decorator function) set function allows to set or access function as attributes that way the function can
#be changed with knowing to user, safely... ideal use case of a "builtin decorator" function

class emp:
	def __init__(self, first, last):
		self.firstname=first
		self.lastname=last

	def __getattr__(self, *args):
		self.email=self.firstname+self.lastname+"@gmail.com"
		return "returned via __getattr__ function: "+self.email
	@property #getattr property butilin decorator function
	def print_yahoo_id(self):
		self.email=self.firstname+self.lastname+"@yahoo.com"
		return "returned via property geattr function: "+self.email
	@property #getattr property butilin decorator function
	def print_rediff_id(self):
		self.email=self.firstname+self.lastname+"@rediff.com"
		return "returned via property geattr function: " + self.email

e=emp('konda','chendil')
#get instance variables
print("Instance variables: " + e.firstname)
print("Instance variables: " + e.lastname)


#Here "email1" and "random_variable" are not defined hence __getattr__ function invovked and store the email value inside in it 
print(e.email1)
print(e.random_variable)

#calls gettr function via property methods.....
#The yahoo_id or rediff_id functions can be changed inside class function but user don't worry about change
#who is importing our "emp" class.. 
#Think about these property inside are directly set as proeprty without property decorators and if we want change it..
#all the users importing our class function or class will fail or need do to their code change which is cumbersome...

print(e.print_yahoo_id)
print(e.print_rediff_id)