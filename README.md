# Radom experiment toolkit

## Usage
Step 1):
    You should implement abstruct class RE within package rexp.
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
 Method oneExp means once Bernoulli's experiment,the method  should return a bool value to indicate event occured or not.In this case ,oneExp return a random value 0 or 1(self.r is o random number generator) means the up side or down side of a Coin.

Step 2):
    Using run shell script the run some experiment:
```shell
$./run -m ThrowCoin
```



