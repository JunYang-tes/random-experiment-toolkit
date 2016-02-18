# coding=UTF-8
'''
一个生产流水线，次品率为0.02，先抽取30个产品问：
（1） 至少有两个次品的概率  Exp2
（2） 已知一个次品的情况下至少两个次品的概率 Exp1
'''
import rexp
class Exp1(rexp.RE):
	def oneExp(self):
		has=False
		cnt=0;
		while not has:
			self.generate()
			for i in range (0,30):
				if self.p[i]==0:
					has=True
					cnt=cnt+1
		return cnt>=2

	def generate(self):
		self.p=[]
		for i in range(0,30):
			if self.r.next(50)==0:#1/50 的次品率
				self.p.append(0)  #0表示次品
			else:
				self.p.append(1)
class Exp2(Exp1):
	def oneExp(self):
		cnt=0
		self.generate()
		for i in range (0,30):
			if self.p[i]==0:
				cnt+=1
		return cnt>=2
if __name__ =="__main__":
	Exp2().start(10000).display()
