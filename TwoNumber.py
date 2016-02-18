import rexp
class TN(rexp.RE):
	def oneExp(self):
		d1= self.r.decimal()
		d2=self.r.decimal()
		return d1*d2>0.25 and d1+d2<1.25
	 
if __name__=="__main__" :
	TN().start(10000000).display()
