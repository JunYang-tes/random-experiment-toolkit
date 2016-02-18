import rexp
class ThrowCoin(rexp.RE):
	def __init__(self):
		rexp.RE.__init__(self,r=rexp.r1())
	def oneExp(self):
		return self.r.next(1)
	def P(self):
		return 0.5

if __name__ == "__main__":
	ThrowCoin().start(1000000).display()
