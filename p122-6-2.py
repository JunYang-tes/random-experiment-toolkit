from rexp import RE
class BusStopCountMV(RE):
	def __init__(self,passengers=25,stations=9):
		RE.__init__(self)
		self.passengerCnt=passengers
		self.stations=stations
	def oneValue(self):
		self.initThisTime()
		value=0
		for i in range(0,self.stations):	#there are nine bus stations
			if self.needStop(i):
				value+=1
		return value
	def EX(self):
		return self.stations*(1-(float(self.stations-1)/self.stations)**self.passengerCnt)
	def initThisTime(self):
		self.passenger=[]
		for i in range(0,self.passengerCnt):	#there are 25 passengers in the bus
			self.passenger.append(self.r.next(self.stations-1))	#0-8 ,9 stations
	def needStop(self,stationIndex):
		for v in self.passenger:
			if v==stationIndex:
				return True
		return False

if __name__=="__main__":
	BusStopCountMV().start(1000,'MV').display()
