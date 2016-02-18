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
&nbsp;&nbsp;Method oneExp means once Bernoulli's experiment,the method  should return a bool value to indicate event occured or not.In this case ,oneExp return a random value 0 or 1(self.r is o random number generator) means the up side or down side of a Coin.

Step 2):
    Using run shell script the run some experiment:
```
$./run -m ThrowCoin
```
The output of program looks like:
>Exp count:5000
    Event  fired:2551 times
    Frequence of event is:0.5102
    P:0.5
    Absolute error is:0.0102
    Time consumption :0:00:00.015120M
    
using `./run --help` for more detail.
>usage: observer.py [-h] -m MODULE [-c CLASS] [-t TIMES] [--type TYPE] [--arg ARG]
optional arguments:
  -h, --help            show this help message and exit
  -m MODULE, --module MODULE
                        module's name (file name without .py)
  -c CLASS, --class CLASS
                        class in module
  -t TIMES, --times TIMES
                        experiment count,default value is 1000
  --type TYPE           experiment type,it can be frq or MV or method anme
  --arg ARG             arguments will be passed to constructor,wraped by 
  
  *Note*
  You can using `-c CLASS` to specify a class which should be subclass of RE to run


