from rexp import RE
class Result:
	def __init__(self,value):
		self.value=value
	def display(self):
		print self.value

class E6_16(RE):
	def oneExp(self):
		v=self.r.normal_distribution(40,14.8)
		return v>=30 and v<=40
	def P(self):
		return 0.5
	def max(self,count):
		c=count
		sum=0
		while c>0:
			c-=1
			sum+=self.oneMimic()
		return Result(sum/float(count))
	def oneValue(self):
		return self.oneMimic()
	def Ex(self):
		return 37
	def oneMimic(self):
		max=0
		ret=0
		for i in range(1,50):
			tmp=int(self.r.normal_distribution(40,14.8))
			if i>=tmp :
				value=70*tmp
				if value > max:
					max=value
					ret=i
					print (i,max)
			else:
				value=70*i-100*(tmp-i)
				if value > max:
					max=value
					ret=i
					print (i,max)
		return ret
