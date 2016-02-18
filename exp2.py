# coding=UTF-8
"""
设有两箱同种零件，第一箱中有50件，其中10件一等品；第二箱中30件，其中18件一等品。
先两箱中随机挑出一箱，然后从该箱中抽取两个（不放回），求：
（1）先取出的零件是一等品的概率
（2）在先取出是一定品的条件下，后取出的仍然是一等品的概率
"""
import rexp
from rexp import r1
class Exp1(rexp.RE):
	def __init__(self,r=r1()):
		rexp.RE.__init__(self,r)
		self.generate() 				#产生两箱产品
		
	def oneExp(self):
		return self.getTwo()[0]==1			#返回bool值，表示第个随机取得的零件是否是1等品
	
	def getTwo(self):
		box=self.boxes[self.r.next(1)] 		#随机挑选一箱. self.r.next(1)随机返回0或1
		index=self.r.next(len(box)-1)		#随机产生一个索引.
		spare1=box[index]					#取出随机位置的零件
		box=box[0:index]+box[index+1:]		#箱子中的零件减少一个
		spare2=box[self.r.next(len(box)-1)]	#随机取出第二个零件
		spares=[]
		spares.append(spare1)
		spares.append(spare2)
		return spares						#返回随机取出的两个零件
		
	def generate(self):
		#由于抽取是随机的，这两箱不需要随机打乱
		self.boxes=[]
		box=[]
		for i in range(0,10):
			box.append(1)					#10个一等品
		for i in range(0,40):
			box.append(2)					#40个非一等品
		self.boxes.append(box)
		box=[]	
		for i in range(0,18):
			box.append(1)					#18个一等品
		for i in range(0,12):
			box.append(2)					#12个非一等品
		self.boxes.append(box)
class Exp2(Exp1):
	def oneExp(self):
		spares=self.getTwo()
		while spares[0] is not 1:			#直到第一个产品是一等品
			spares=self.getTwo()
		return spares[1]==1					#返回bool，表示第二个产品仍然是一等品
		
if __name__ =="__main__":
	Exp1().start(20000).display()
	Exp2().start(20000).display()		
