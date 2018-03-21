import re,os
def keep(pat,text,type=False):
	if os.path.exists(pat)==0:
		f=open(pat, 'w+')
		f.write(text)
		f.close()
	else:
		if type:
			f=open(pat, 'w+')
			f.write(text)
			f.close()
		else:
			f=open(pat, 'a')
			f.write(text)
			f.close()
def cn(x):
	x=x.decode("utf8")
	return x
def en(x):
	x=x.encode("utf8")
	return x
d=open("e://a.txt","r")
dat=d.read()
d.close()
dat=dat.replace("\n","$")
keep("e://b.txt",dat,True)
dlist=re.findall("\((.*?)￥$",dat)
qq=""
s="￥syUUgWdHok￥"
#keep("e://b.txt",s+"\n",True)
for i in dlist:
	if(i.find("2分")!=-1):
		q=re.findall("(.*?)\)",i)[0]
		print q
		ss=re.findall("￥\w+￥",i)[0]
		if(s.find(ss)==-1):
			s=s+ss
			print ss
			keep("e://b.txt",ss+"\n")