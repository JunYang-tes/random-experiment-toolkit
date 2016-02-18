import random
import math
class RandomBase:
	def __init__(self):
		self.precious=15
	def normal_distribution(self,mean,variance):
		return mean+(self.standard()*variance)
	def uniform(self,a=0,b=1):
		if a>b:
			tmp=a
			a=b
			b=tmp
		return a+self.decimal()*(b-a)
	def standard(self):
		c=self.precious
		sum=0
		while c >0:
			c-=1
			sum+=self.decimal()
		return (sum-self.precious/2.0)/12  #uniform (0,1) ex=1 dx=1/12

class r1(RandomBase):
	def next(self,m):
		"""
		generate random int in range [0,m]
		"""
		return random.randint(0,m)
	def decimal(self):
		return random.random()
		
class r2(RandomBase):
	def next(self,m):
		import os
		return int(os.urandom(3).encode('hex'),16) % (m+1)
	def decimal(self):
		return self.next(1000000) / 1000000.0
		
class Result:
	def __init__(self,firedCnt=0,expCnt=0,eventName="",tValue=None):
		self.eventName=eventName
		self.firedCnt=firedCnt
		self.expCnt=expCnt
		self.tValue=tValue
	def display(self):
		print "Exp count:"+str(self.expCnt)
		print "Event "+self.eventName+" fired:"+str(self.firedCnt)+" times"
		print "Frequence of event is:"+str((self.firedCnt+0.0)/self.expCnt)
		if self.tValue is not None:
			print "P:"+str(self.tValue)
			print "Absolute error is:"+str(abs((self.firedCnt+0.0)/self.expCnt-self.tValue))
		return self
class MVResult:
	def __init__(self,value,tValue):
		self.value=value
		self.tValue=tValue
	def display(self):
		print "Mean value is:"+str(self.value)
		if self.tValue is not None:
			print "Expectation is :"+str(self.tValue)
			print "Absolute error is:"+str(abs(self.value-self.tValue))
class MEResult:#moment estimation result
	def __init__(self,params=[],estimations=[]):
		self.params=params
		self.estimations=estimations
	def display(self):
		print "Moment estimation"
		c=len(self.params)
		i=0
		while i<c:
			out=["Param:"]
			out.append(str(self.params[i]))
			out.append("\tEst:")
			out.append(str(self.estimations[i]))
			out.append("\tAE:")
			out.append(str(abs(self.params[i]-self.estimations[i])))
			print " ".join(out)
			i+=1

class NoResult:
	def __init__(self,value):
		self.value=value
	def display(self):
		print self.value
		

"""
Basic class of every random experiment
"""
class RE:
	def __init__(self,r=r1(),name=""):
		self.r=r
		self.name=name
	def start(self,count,expType='frq'):
		expType=expType.strip()
		if expType == 'frq':
			return self.frequency(count)
		elif expType == 'MV':
			return self.expectation(count)
		elif hasattr(self,expType):
			return getattr(self,expType)(count)
		return NoResult("No such type:"+expType)
	
	def frequency(self,count):
		fired=0;
		c=count
		while c>0:
			c-=1
			if self.oneExp() :
				fired+=1
		return Result(fired,count,self.name,self.P())
	def expectation(self,count):
		num=0
		c=count
		while c>0:
			c-=1
			num+=self.oneValue()
		return MVResult((num+0.0)/count,self.EX())
	def EX(self):
		return None
	def P(self):
		return None
	def oneValue(self):
		raise NotImplimentedError("Abstract")
	def oneExp(self):
		raise NotImplimentedError("Abstract")
	
