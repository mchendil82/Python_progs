class emp:
	def __init__(self, first, last):
		self.firstname=first
		self.lastname=last
	def __getattr__(self, *args):
		self.email=self.firstname+self.lastname+"@gmail.com"
		return self.email
	@property
	def yyyy(self):
		self.email=self.firstname+self.lastname+"@yahoo.com"
		return "hi "+self.email
	@property
	def xxxx(self):
		self.email=self.firstname+self.lastname+"@rediff.com"
		return self.email

e=emp('konda','chendil')
print(e.firstname)
print(e.lastname)
print(e.email1)
print(e.email2)
print(e.yyyy)
print(e.xxxx)