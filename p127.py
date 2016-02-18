from rexp import RE
import math
class YMV(RE):
	def oneValue(self):
		s=2*self.r.decimal()*math.pi  #2PiR R=1
		y=math.sin(s)
		return y
	def EX(self):
		return 0
