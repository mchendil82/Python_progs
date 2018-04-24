#__getattr__ function=get by default and store the variable with values defined in  __getattr__ function and 
#it will not throw the "Attribute not defined error".. 
#This can be used to store values by the user(kind of dynammically ) which is NOT defined in the program


#getattr- A propety decorators(python builtin property decorator function) set function allows to set or access function as "attributes" that way the function can
#be changed with knowing to user safely... ideal use case of a "builtin decorator" function

#Setter - Usually Properties used as property decorators doesn't allow to set values outside @property function
#it will give "Attributes can't set error"... Hence we use setters

class emp(object):
	def __init__(self, first, last):
		self.firstname=first
		self.lastname=last


	@property
	def full_name(self):
		return "*****"+self.firstname+self.lastname

	@full_name.setter #setter function defined...
	def full_name(self, fullname):
		first, last = fullname.split(' ')
		self.firstname = first
		self.lastname = last
	
	def __getattr__(self, *args): #getattr built-in majic function for automatic variables assignment
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

e.email="konda_chendil@email.com"


#Here "email1" and "random_variable" are not defined hence __getattr__ function invovked and store the email value inside in it 
print(e.email1)
print(e.random_variable)

#calls gettr function via property methods.....
#The yahoo_id or rediff_id functions can be changed inside class function but user don't worry about change
#who is importing our "emp" class.. 
#Think about these properties inside are directly set as proeprty without property decorators and if we want change it..
#all the users importing our class function or class will fail or need do to their code change which is cumbersome...


#full_name is property decorator which doesn't allow set values outside of class or where it is defined
#and it is throws(attribute can't set error)
#Hence we setter property function as defined above...
e.full_name='sathya konda_chendil'

print("after setter variables: " + e.firstname)
print("after setter variables: " + e.lastname)

print(e.full_name)
print(e.print_yahoo_id)
print(e.print_rediff_id)