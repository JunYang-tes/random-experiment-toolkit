import argparse
import numpy as np
import datetime as dt
def estimate_time(sample,expType,count,obj):
	x=np.array(sample)
	y=[]
	for xv in sample:
		dt1=dt.datetime.now()
		obj.start(xv,expType)
		dt2=dt.datetime.now()
		y.append((dt2-dt1).total_seconds())
	y=np.array(y)
	print "Polyfitting"
	f=np.poly1d(np.polyfit(x,y,1))
	return dt.timedelta(seconds=f(count))
def constructor(module,className,arg):
	module=vars(__import__(module))
	clazz=module.get(className,None)
	if clazz is None:
		return None
	if arg==None or hasattr(clazz,"init_types") is False:
		return clazz()
	argDict=clazz.init_types()
	ap=argparse.ArgumentParser()
	for k in argDict:
		ap.add_argument("--prefix"+k,type=argDict[k])
	argParser=ap.parse_args(str_convert(arg).split())
	argWillBePassed={}
	for k in argDict:
		if hasattr(argParser,"prefix"+k):
			argWillBePassed[k]=getattr(argParser,"prefix"+k)
		else:
			print "no "+k
	return clazz(**argWillBePassed)
def str_convert(str):
	ret=[]
	ret.append("--prefix")
	key=1
	value=2
	state=key
	for c in str:
		if state==key:
			if c=='=':
				state=value
				ret.append(' ')
			else:
				ret.append(c)
		else:
			if c==',':
				state=key
				ret.append(' --prefix')
			else:
				ret.append(c)
	return ''.join(ret)

ap=argparse.ArgumentParser()
ap.add_argument("-m","--module",help="module's name (file name without .py)",required=True)
ap.add_argument("-c","--class",help="class in module")
ap.add_argument("-t","--times",help="experiment count,default value is 1000",type=int,default=5000)
ap.add_argument("--type",help="experiment type,it can be frq or MV or method anme",default="frq")
ap.add_argument("--arg",help="arguments will be passed to constructor,wraped by ``")



args=vars(ap.parse_args())



className=args.get("class")	#module name as default class name
if className is None:
	className=args["module"]
obj=constructor(args["module"],className,args.get("arg",None))

if obj is not None:
	cnt=args["times"]
	if cnt>10000:
		print "Estimating time consumption"
		time=estimate_time([10,20,40,80,160,320,640],args["type"],cnt,obj)
		print "Estimated time consumption is "+str(time)
		print str(dt.datetime.now()+time)
	dt1=dt.datetime.now()
	obj.start(args["times"],args["type"]).display()
	dt2=dt.datetime.now()
	ts=dt2-dt1
	print "Time consumption :"+str(ts)+"M"
else:
	print "class "+str(className)+" not in module "+str(args["module"])


