from rexp import RE
class E6_9(RE):
	def oneExp(self):
		self.generate()
		return self.box2[self.r.next(5)]==0
	def oneValue(self):
		self.generate()
		cnt=0
		for v in self.box2:
			if v==0:
				cnt+=1
		return cnt
	def EX(self):
		return 1.5
	def generate(self):
		self.box1=[1,1,1,0,0,0]
		self.box2=[1,1,1]
		self.box2.append(self.getOne())
		self.box2.append(self.getOne())
		self.box2.append(self.getOne())
	def getOne(self):
		index=self.r.next(len(self.box1)-1)
		value=self.box1[index]
		self.box1=self.box1[:index]+self.box1[index+1:]
		return value
	def P(self):
		return float(1)/4
