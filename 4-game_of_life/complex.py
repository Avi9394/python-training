class Complex:
	def __init__(self,real,i):
		self.real=real
		self.i=i
	def __str__(self):
		#return str(self.real) + ' + i' + str(self.i)
		return f"{self.real} + i{self.i}"
	def __eq__(self, other):
		return (self.real, self.i ) == (other.real , other.i)

	def __gt__(self, other):
		return (self.real**2 + self.i**2) > (other.real**2 + other.i **2)
	def __lt__(self, other):
		return (self.real**2 + self.i**2) < (other.real**2 + other.i **2)

c1 = Complex(1,2)
c2 = Complex(2,1)
c3 = Complex(3,2)
c4 = Complex(1,2)
print(str(c1))
print(str(c2))
print(str(c3))
print(str(c4))
print(c1 == c2) #False
print(c1 == c4) #True
print(c1 > c3) #False
print(c2 > c3) #False
print(c3 > c2) #True

print(c1 < c3) #True
print(c2 < c3) #True
print(c3 < c2) #False