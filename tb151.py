from rexp import RE
from rexp import MEResult
import math
class E2(RE):
	def __init__(self,a=1,b=2,count=5):
		RE.__init__(self)
		self.a=a;
		self.b=b;
		self.count=count
	@staticmethod
	def init_types():
		return {"a":int,"b":int,"count":int}
	def test(self,count):
		self.count=count
		self.generate()
		self.moment_estimation()
		return MEResult([self.a,self.b],[self.a_,self.b_]);
	def generate(self):
		self.Xi=[]
		c=self.count
		sum=0.0
		while c>0:
			c-=1
			tmp=self.r.uniform(self.a,self.b)
			sum+=tmp
			self.Xi.append(tmp)
		self.MV=sum/self.count	
	def moment_estimation(self):
		sum=0
		for i in range(0,self.count):
			tmp=(self.Xi[i]-self.MV)
			sum+=(tmp*tmp)
		tmp=math.sqrt(float(3)/self.count * sum)
		self.a_=self.MV-tmp
		self.b_=self.MV+tmp
		
