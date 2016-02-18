from rexp import RE
from rexp import Result
'''
Varify uniform fucntion is working correct
'''
class Uniform(RE):
	@staticmethod
	def init_types():
		return {"a":int,"b":int,"len":float}
	def __init__(self,a=0,b=1,len=0.5):
		RE.__init__(self)
		self.a=a
		self.b=b
		self.len=len
	def oneExp(self):
		return self.r.uniform(self.a,self.b)<self.a+self.len #is lay in ragion (a,a+len)
	def P(self):
		return self.len/(-self.a+self.b)
class Normal(RE):
	@staticmethod
	def init_types():
		return {"mv":int,"variance":int}
	def __init__(self,mv=0,variance=1):
		RE.__init__(self)
		self.mv=mv
		self.variance=variance
	def oneExp(self):
		return self.r.normal_distribution(self.mv,self.variance)<self.mv
	def P(self):
		return 0.5
