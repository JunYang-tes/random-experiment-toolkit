#Radom experiment toolkit
This is a toolkit for radom experiment,using this toolkit you can simulate random event and verify probability and expectation.According to the Bernoulli's theorem of large numbers ,this toolkit can using frequency to verify probability of rando event.
##usage
Step 1):You should implement abstruct class RE within package rexp,the subclass should has the same name of .py file.
		Take ThrowCoin as example:
		```python
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

		```
