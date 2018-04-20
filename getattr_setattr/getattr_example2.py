class emp:
	def __init__(self, first, last):
		self.firstname=first
		self.lastname=last
	def __getattr__(self, *args):
		self.email=self.firstname+self.lastname+"@gmail.com"
		return "returned via __getattr__ function: "+self.email
	@property
	def print_yahoo_id(self):
		self.email=self.firstname+self.lastname+"@yahoo.com"
		return "returned via property geattr function: "+self.email
	@property
	def print_rediff_id(self):
		self.email=self.firstname+self.lastname+"@rediff.com"
		return "returned via property geattr function: " + self.email

e=emp('konda','chendil')
#get instance variables
print("Instance variables: " + e.firstname)
print("Instance variables: " + e.lastname)

#get by default store the variable with values defined in  __getattr__ function and 
#it will not "Attribute not defined error".. 
#This can be used to store values by the user(kind of dynammically ) which is NOT defined in the program
#Here "email1" and "random_variable" are not defined hence __getattr__ function invovked and store the email value inside in it 
print(e.email1)
print(e.random_variable)

#calls gettr function via property methods.....
print(e.print_yahoo_id)
print(e.print_rediff_id)