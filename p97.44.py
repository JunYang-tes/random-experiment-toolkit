from rexp import RE
class Coin(RE):
	def __init__(self):
		RE.__init__(self)
	def oneExp(self):
		c1=0
		c2=0
		for i in range (0,5):
			if self.r.next(1)==1:
				c1+=1
			else:
				c2+=1
		return c1>=2 and c2>=2
class Product(RE):
	def __init__(self):
		RE.__init__(self)
	def oneExp(self):
		p=[False]*10
		#generate two 
		p[self.r.next(9)]=True
		r=self.r.next(9)
		while p[r]:
			r=self.r.next(9)
		p[r]=True
		#
		i=self.r.next(9)
		p=p[:i]+p[i+1:]
		return p[self.r.next(8)]==True
if __name__=="__main__":
	Product().start(1000).display()

		
