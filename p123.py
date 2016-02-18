from rexp import RE
class E6_5(RE):
	def EX(self):
		return 16;
	def oneValue(self):
		value=0
		while True:
			value+=1
			if self.X():
				break
		while True:
			value+=1
			if self.X():
				break
		return value
	def X(self):
		return self.r.next(7)==0 #1/8
	def oneExp(self):
		return 1

