from rexp import RE
from rexp import r1
class BallsInBoxes(RE):
	def __init__(self,r=r1(),ballCnt=5,boxCnt=10):
		RE.__init__(self,r)
		self.ballCnt=ballCnt
		self.boxCnt=boxCnt
	def oneExp(self):
		tmp=[]
		for i in range (0,self.ballCnt):
			boxNum=self.r.next(self.boxCnt)
			if boxNum in tmp:
				return 0
			tmp.append(boxNum)
		return 1
if __name__ == "__main__":
	BallsInBoxes().start(10000).display()
		
