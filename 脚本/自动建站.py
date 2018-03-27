# -*- coding: utf8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import cStringIO
import os
import re
import httplib
import gzip
import time
import urllib

'''
import io
# allows for image formats other than gif
from PIL import Image, ImageTk
try:
  # Python2
  import Tkinter as tk
  from urllib2 import urlopen
except ImportError:
  # Python3
  import tkinter as tk
  from urllib.request import urlopen
def getimage(url):
  root = tk.Tk()
  #url = "http://37t.cn/index.php?m=Index&a=verifyLogin"

  image_bytes = urlopen(url).read()
  data_stream = io.BytesIO(image_bytes)
  pil_image = Image.open(data_stream)
  w, h = pil_image.size
  fname = url.split('/')[-1]
  sf = "{} ({}x{})".format(fname, w, h)
  root.title(sf)
  tk_image = ImageTk.PhotoImage(pil_image)
  label = tk.Label(root, image=tk_image, bg='brown')
  label.pack(padx=5, pady=5)
  root.mainloop()
'''

def cn(x):
  x=x.decode("utf8")
  return x
def en(x):
  x=x.encode("utf8")
  return x

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
    f=open(pat, 'a')
    f.write(text)
    f.close()


def request(host, url, headers, body = None, sendCookie = True, setCookie = True, referer = None):
  global headmsg
  headers = headers.copy()
  conn = httplib.HTTPConnection(host)
  method = "GET"
  if body:
    method = "POST"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
  if sendCookie and Cookies.has_key(host):
    headers["Cookie"] = Cookies[host]
  if referer:
    headers["Referer"] = referer
  conn.request(method, url, body, headers)
  res = conn.getresponse()
  cookie = res.getheader("set-cookie")
  headmsg=res.getheaders()
  if cookie and setCookie:
    i = cookie.find(";")
    if i != -1:
      cookie = cookie[:i]
    Cookies[host] = cookie
  data = res.read()
  if res.getheader("Content-Encoding") == "gzip":
    io = cStringIO.StringIO()
    io.write(data)
    io.seek(0)
    gz = gzip.GzipFile(fileobj = io)
    data = gz.read()
    gz.close()
    io.close()

  conn.close()
  return data


Cookies = {'37t.cn':'','oa.qz160168.cn':''}
host1="37t.cn"
headers1 = {'User-Agent':'Opera/9.80 (Windows NT 5.1; U; Edition Next; zh-cn) Presto/2.10.289 Version/12.00','Accept':'text/html, application/xhtml+xml, */*','Accept-Language':'zh-CN','Accept-Encoding':'gzip, deflate','Cache-Control':'no-cache','Connection':'Keep-Alive'}

def logout():
  url="/index.php?g=System&m=Admin&a=logout"
  data=request(host1, url, headers1)


def login(username,password,gsjj,gsjc,kddh,gsdz):
  if len(username)==8:
    username="0595"+username
  print username
  url="/index.php?m=Index&a=login"
  data=request(host1, url, headers1)
  __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
  verifycode2="1234"#raw_input("code:")
  url="/index.php?m=Users&a=checklogin"
  data=request(host1, url, headers1,"username=%s&password=%s&verifycode=%s&__hash__=%s"%(username,password,verifycode2,__hash__))
  token=re.findall('token=(.*?)"',data)[0]
  print cn(re.findall('<span>(.*?)</span>',data)[0])
  fenlei1=u"公司简介"
  print u"开始创建文章..."
  print u"创建%s"%fenlei1
  url="/index.php?g=User&m=Img&a=add"
  data=request(host1, url, headers1)   
  __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
  url="/index.php?g=User&m=Img&a=insert"
  pd={}
  pd["precisions"]="0"
  pd["title"]=en(fenlei1)
  pd["classid"]=en(u"5039,的撒发生")
  pd["pic"]="http://37t.cn/uploads/w/wsweyi1428396337/d/0/6/b/thumb_5545d69fa7928.jpg"
  pd["showpic"]="1"
  pd["info"]=en(u'<span style="font-size:16px;font-family:SimSun;">　　%s</span>'%gsjj.decode("gbk"))
  pd["pc_cat_id"]="0"
  pd["pc_show"]="0"
  pd["texttype"]="1"
  pd["sbmt"]=en(u"保存")
  pd["__hash__"]=__hash__ 
  data=request(host1, url, headers1,urllib.urlencode(pd))  
  # print (u"创建相册中...")
  # url="/index.php?g=User&m=Photo&a=add&token="
  # data=request(host1, url, headers1,"button=&title=产品展示&picurl=产品展示&info=产品展示&isshowinfo=0&status=1&__hash__=%s"%__hash__)
  # print u"相册创建成功！"

  print u"开始创建分类..."
  print u"1.标准6类"
  print u"2.6类双相册"
  print u"3.6类双动态"
  print u"4.5类+相册"
  print u"5.5类+动态"
  while True:
    fenlei=raw_input(u"请输入分类类型(直接回车默认1)：".encode("gbk"))
    if len(fenlei)==0:
      fenlei="1"
      break
    else:
      if fenlei=="1" or fenlei=="2" or fenlei=="3" or fenlei=="4" or fenlei=="5":
        break
  print u"1.红色"
  print u"2.橙色"
  print u"3.黄色"
  print u"4.绿色"
  print u"5.蓝色"
  print u"6.灰色"
  print u"7.紫色"
  print u"8.棕色"
  print u"9.白色"
  while True:
    yanse=raw_input(u"请输入图标颜色(直接回车默认6)：".encode("gbk"))
    if len(yanse)==0:
      yanse=6
      break
    else:
      if yanse=="1" or yanse=="2" or yanse=="3" or yanse=="4" or yanse=="5" or yanse=="6" or yanse=="7" or yanse=="8" or yanse=="9":
        yanse=int(yanse)
        break
    
    
    
  #1.标准6类  
  if fenlei=="1":
    fenlei1=u"公司简介"
    fenlei2=u"产品展示"
    fenlei3=u"相关知识"
    fenlei4=u"联系我们"
    fenlei5=u"地图导航"
    fenlei6=u"在线留言"
    while True:
      print u"1.%s"%fenlei1
      print u"2.%s"%fenlei2
      print u"3.%s"%fenlei3
      print u"4.%s"%fenlei4
      print u"5.%s"%fenlei5
      print u"6.%s"%fenlei6
      xiugai=raw_input(u"输入修改项目序号，输入其他进入下一步：".encode("gbk"))
      if xiugai=="1":
        fenlei1=unicode(raw_input((u"%s改为："%fenlei1).encode("gbk")),"gbk")
      elif xiugai=="2":
        fenlei2=unicode(raw_input((u"%s改为："%fenlei2).encode("gbk")),"gbk")
      elif xiugai=="3":
        fenlei3=unicode(raw_input((u"%s改为："%fenlei3).encode("gbk")),"gbk")
      elif xiugai=="4":
        fenlei4=unicode(raw_input((u"%s改为："%fenlei3).encode("gbk")),"gbk")
      elif xiugai=="5":
        fenlei5=unicode(raw_input((u"%s改为："%fenlei5).encode("gbk")),"gbk")
      elif xiugai=="6":
        fenlei6=unicode(raw_input((u"%s改为："%fenlei6).encode("gbk")),"gbk")
      else:
        break


        
      
    #公司简介
    print u"创建%s中"%fenlei1
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/3.png","orange/3.png","yellow/3.png","green/3.png","blue/3.png","gray/24.png","purple/3.png","brown/3.png","white/21.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/fangdichan/fangdichan_"+imagelist[yanse-1]
    pd={}
    pd["name"]=en(fenlei1)
    pd["img"]=imgurl
    pd["sorts"]="6"
    pd["tpid"]="1"
    pd["conttpid"]="1"
    pd["status"]="1"
    pd["url"]=""
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei1
    



    #产品展示
    url="/index.php?g=User&m=Photo&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print (u"创建相册中...")
    url="/index.php?g=User&m=Photo&a=add&token="
    data=request(host1, url, headers1,"button=&title=%s&picurl=http://37t.cn/tpl/static/attachment/focus/default/2.jpg&info=%s&isshowinfo=0&status=1&__hash__=%s"%(en(fenlei2),en(fenlei2),__hash__))
    print u"相册创建成功！"
    print u"获取相册信息"
    url="/index.php?g=User&m=Link&a=Photo&iskeyword=0"
    data=request(host1, url, headers1)
    gnurl=re.findall("returnHomepage\('(.*?)'\)",data)[0]
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei2
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/11.png","orange/11.png","yellow/11.png","green/11.png","blue/11.png","gray/21.png","purple/11.png","brown/11.png","white/25.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/edu/edu_"+imagelist[yanse-1]
    pd["name"]=en(fenlei2)
    pd["img"]=imgurl
    pd["sorts"]="5"
    pd["url"]=gnurl
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei2
    #相关知识
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei3
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/15.png","orange/15.png","yellow/15.png","green/15.png","blue/15.png","gray/3.png","purple/15.png","brown/15.png","white/21.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/edu/edu_"+imagelist[yanse-1]
    pd["name"]=en(fenlei3)
    pd["img"]=imgurl
    pd["sorts"]="4"
    pd["url"]=""
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei3
    #联系我们
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei4
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/19.png","orange/19.png","yellow/19.png","green/19.png","blue/19.png","gray/1.png","purple/19.png","brown/19.png","white/27.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/edu/edu_"+imagelist[yanse-1]
    pd["name"]=en(fenlei4)
    pd["img"]=imgurl
    pd["sorts"]="3"
    pd["url"]=""
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei4
    #地图导航
    print u"获取地图信息"
    url="/index.php?g=User&m=Link&a=Company&iskeyword=0"
    data=request(host1, url, headers1)
    gnurl=re.findall("returnHomepage\('(.*?)'\)",data)[0]
    
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei5
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/18.png","orange/18.png","yellow/18.png","green/18.png","blue/18.png","gray/9.png","purple/18.png","brown/18.png","white/11.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/canyin/canyin_"+imagelist[yanse-1]
    pd["name"]=en(fenlei5)
    pd["img"]=imgurl
    pd["sorts"]="2"
    pd["url"]=gnurl
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei5   
    #在线留言
    gnurl="{siteUrl}/index.php?g=Wap&m=Reply&a=index&token=%s&wecha_id={wechat_id}"%token
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei6
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/15.png","orange/15.png","yellow/15.png","green/15.png","blue/15.png","gray/2.png","purple/15.png","brown/15.png","white/21.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/canyin/canyin_"+imagelist[yanse-1]
    pd["name"]=en(fenlei6)
    pd["img"]=imgurl
    pd["sorts"]="1"
    pd["url"]=gnurl
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei6
##################################################################################################################
  #2.6类双相册  
  elif fenlei=="2":
    fenlei1=u"公司简介"
    fenlei2=u"产品展示"
    fenlei3=u"企业荣誉"
    fenlei4=u"联系我们"
    fenlei5=u"地图导航"
    fenlei6=u"在线留言"
    while True:
      print u"1.%s"%fenlei1
      print u"2.%s"%fenlei2
      print u"3.%s"%fenlei3
      print u"4.%s"%fenlei4
      print u"5.%s"%fenlei5
      print u"6.%s"%fenlei6
      xiugai=raw_input(u"输入修改项目序号，输入其他进入下一步：".encode("gbk"))
      if xiugai=="1":
        fenlei1=unicode(raw_input((u"%s改为："%fenlei1).encode("gbk")),"gbk")
      elif xiugai=="2":
        fenlei2=unicode(raw_input((u"%s改为："%fenlei2).encode("gbk")),"gbk")
      elif xiugai=="3":
        fenlei3=unicode(raw_input((u"%s改为："%fenlei3).encode("gbk")),"gbk")
      elif xiugai=="4":
        fenlei4=unicode(raw_input((u"%s改为："%fenlei3).encode("gbk")),"gbk")
      elif xiugai=="5":
        fenlei5=unicode(raw_input((u"%s改为："%fenlei5).encode("gbk")),"gbk")
      elif xiugai=="6":
        fenlei6=unicode(raw_input((u"%s改为："%fenlei6).encode("gbk")),"gbk")
      else:
        break


        
      
    #公司简介
    print u"创建%s中"%fenlei1
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/3.png","orange/3.png","yellow/3.png","green/3.png","blue/3.png","gray/24.png","purple/3.png","brown/3.png","white/21.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/fangdichan/fangdichan_"+imagelist[yanse-1]
    pd={}
    pd["name"]=en(fenlei1)
    pd["img"]=imgurl
    pd["sorts"]="6"
    pd["tpid"]="1"
    pd["conttpid"]="1"
    pd["status"]="1"
    pd["url"]=""
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei1
    



    #产品展示
    url="/index.php?g=User&m=Photo&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print (u"创建相册中...")
    url="/index.php?g=User&m=Photo&a=add&token="
    data=request(host1, url, headers1,"button=&title=%s&picurl=http://37t.cn/tpl/static/attachment/focus/default/2.jpg&info=%s&isshowinfo=0&status=1&__hash__=%s"%(en(fenlei2),en(fenlei2),__hash__))
    print u"相册创建成功！"
    print u"获取相册信息"
    url="/index.php?g=User&m=Link&a=Photo&iskeyword=0"
    data=request(host1, url, headers1)
    gnurl=re.findall("returnHomepage\('(.*?)'\)",data)[0]
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei2
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/11.png","orange/11.png","yellow/11.png","green/11.png","blue/11.png","gray/21.png","purple/11.png","brown/11.png","white/25.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/edu/edu_"+imagelist[yanse-1]
    pd["name"]=en(fenlei2)
    pd["img"]=imgurl
    pd["sorts"]="5"
    pd["url"]=gnurl
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei2
    #企业荣誉
    url="/index.php?g=User&m=Photo&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print (u"创建相册中...")
    url="/index.php?g=User&m=Photo&a=add&token="
    data=request(host1, url, headers1,"button=&title=%s&picurl=http://37t.cn/tpl/static/attachment/focus/default/2.jpg&info=%s&isshowinfo=0&status=1&__hash__=%s"%(en(fenlei3),en(fenlei3),__hash__))
    print u"相册创建成功！"
    print u"获取相册信息"
    url="/index.php?g=User&m=Link&a=Photo&iskeyword=0"
    data=request(host1, url, headers1)
    gnurl=re.findall("returnHomepage\('(.*?)'\)",data)[0]
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei3
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/15.png","orange/15.png","yellow/15.png","green/15.png","blue/15.png","gray/3.png","purple/15.png","brown/15.png","white/21.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/edu/edu_"+imagelist[yanse-1]
    pd["name"]=en(fenlei3)
    pd["img"]=imgurl
    pd["sorts"]="4"
    pd["url"]=gnurl
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    #联系我们
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei4
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/19.png","orange/19.png","yellow/19.png","green/19.png","blue/19.png","gray/1.png","purple/19.png","brown/19.png","white/27.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/edu/edu_"+imagelist[yanse-1]
    pd["name"]=en(fenlei4)
    pd["img"]=imgurl
    pd["sorts"]="3"
    pd["url"]=""
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei4
    #地图导航
    print u"获取地图信息"
    url="/index.php?g=User&m=Link&a=Company&iskeyword=0"
    data=request(host1, url, headers1)
    gnurl=re.findall("returnHomepage\('(.*?)'\)",data)[0]
    
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei5
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/18.png","orange/18.png","yellow/18.png","green/18.png","blue/18.png","gray/9.png","purple/18.png","brown/18.png","white/11.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/canyin/canyin_"+imagelist[yanse-1]
    pd["name"]=en(fenlei5)
    pd["img"]=imgurl
    pd["sorts"]="2"
    pd["url"]=gnurl
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei5   
    #在线留言
    gnurl="{siteUrl}/index.php?g=Wap&m=Reply&a=index&token=%s&wecha_id={wechat_id}"%token
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei6
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/15.png","orange/15.png","yellow/15.png","green/15.png","blue/15.png","gray/2.png","purple/15.png","brown/15.png","white/21.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/canyin/canyin_"+imagelist[yanse-1]
    pd["name"]=en(fenlei6)
    pd["img"]=imgurl
    pd["sorts"]="1"
    pd["url"]=gnurl
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei6
#############################################################################
  #3.6类双动态
  elif fenlei=="3": 
    fenlei1=u"公司简介"
    fenlei2=u"企业文化"
    fenlei3=u"相关知识"
    fenlei4=u"联系我们"
    fenlei5=u"地图导航"
    fenlei6=u"在线留言"
    while True:
      print u"1.%s"%fenlei1
      print u"2.%s"%fenlei2
      print u"3.%s"%fenlei3
      print u"4.%s"%fenlei4
      print u"5.%s"%fenlei5
      print u"6.%s"%fenlei6
      xiugai=raw_input(u"输入修改项目序号，输入其他进入下一步：".encode("gbk"))
      if xiugai=="1":
        fenlei1=unicode(raw_input((u"%s改为："%fenlei1).encode("gbk")),"gbk")
      elif xiugai=="2":
        fenlei2=unicode(raw_input((u"%s改为："%fenlei2).encode("gbk")),"gbk")
      elif xiugai=="3":
        fenlei3=unicode(raw_input((u"%s改为："%fenlei3).encode("gbk")),"gbk")
      elif xiugai=="4":
        fenlei4=unicode(raw_input((u"%s改为："%fenlei3).encode("gbk")),"gbk")
      elif xiugai=="5":
        fenlei5=unicode(raw_input((u"%s改为："%fenlei5).encode("gbk")),"gbk")
      elif xiugai=="6":
        fenlei6=unicode(raw_input((u"%s改为："%fenlei6).encode("gbk")),"gbk")
      else:
        break


        
      
    #公司简介
    print u"创建%s中"%fenlei1
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/3.png","orange/3.png","yellow/3.png","green/3.png","blue/3.png","gray/24.png","purple/3.png","brown/3.png","white/21.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/fangdichan/fangdichan_"+imagelist[yanse-1]
    pd={}
    pd["name"]=en(fenlei1)
    pd["img"]=imgurl
    pd["sorts"]="6"
    pd["tpid"]="1"
    pd["conttpid"]="1"
    pd["status"]="1"
    pd["url"]=""
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei1


    #企业文化
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei2
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/14.png","orange/14.png","yellow/14.png","green/14.png","blue/14.png","gray/10.png","purple/14.png","brown/14.png","white/13.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/edu/edu_"+imagelist[yanse-1]
    pd["name"]=en(fenlei2)
    pd["img"]=imgurl
    pd["sorts"]="5"
    pd["url"]=""
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei2
    #相关知识
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei3
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/15.png","orange/15.png","yellow/15.png","green/15.png","blue/15.png","gray/3.png","purple/15.png","brown/15.png","white/21.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/edu/edu_"+imagelist[yanse-1]
    pd["name"]=en(fenlei3)
    pd["img"]=imgurl
    pd["sorts"]="4"
    pd["url"]=""
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei3
    #联系我们
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei4
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/19.png","orange/19.png","yellow/19.png","green/19.png","blue/19.png","gray/1.png","purple/19.png","brown/19.png","white/27.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/edu/edu_"+imagelist[yanse-1]
    pd["name"]=en(fenlei4)
    pd["img"]=imgurl
    pd["sorts"]="3"
    pd["url"]=""
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei4
    #地图导航
    print u"获取地图信息"
    url="/index.php?g=User&m=Link&a=Company&iskeyword=0"
    data=request(host1, url, headers1)
    gnurl=re.findall("returnHomepage\('(.*?)'\)",data)[0]
    
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei5
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/18.png","orange/18.png","yellow/18.png","green/18.png","blue/18.png","gray/9.png","purple/18.png","brown/18.png","white/11.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/canyin/canyin_"+imagelist[yanse-1]
    pd["name"]=en(fenlei5)
    pd["img"]=imgurl
    pd["sorts"]="2"
    pd["url"]=gnurl
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei5   
    #在线留言
    gnurl="{siteUrl}/index.php?g=Wap&m=Reply&a=index&token=%s&wecha_id={wechat_id}"%token
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei6
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/15.png","orange/15.png","yellow/15.png","green/15.png","blue/15.png","gray/2.png","purple/15.png","brown/15.png","white/21.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/canyin/canyin_"+imagelist[yanse-1]
    pd["name"]=en(fenlei6)
    pd["img"]=imgurl
    pd["sorts"]="1"
    pd["url"]=gnurl
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei6
###################################################################################################################
  #4.5类+相册
  elif fenlei=="4":
    fenlei1=u"公司简介"
    fenlei2=u"产品展示"
    fenlei3=u"联系我们"
    fenlei4=u"地图导航"
    fenlei5=u"在线留言"
    while True:
      print u"1.%s"%fenlei1
      print u"2.%s"%fenlei2
      print u"3.%s"%fenlei3
      print u"4.%s"%fenlei4
      print u"5.%s"%fenlei5
      xiugai=raw_input(u"输入修改项目序号，输入其他进入下一步：".encode("gbk"))
      if xiugai=="1":
        fenlei1=unicode(raw_input((u"%s改为："%fenlei1).encode("gbk")),"gbk")
      elif xiugai=="2":
        fenlei2=unicode(raw_input((u"%s改为："%fenlei2).encode("gbk")),"gbk")
      elif xiugai=="3":
        fenlei3=unicode(raw_input((u"%s改为："%fenlei3).encode("gbk")),"gbk")
      elif xiugai=="4":
        fenlei4=unicode(raw_input((u"%s改为："%fenlei3).encode("gbk")),"gbk")
      elif xiugai=="5":
        fenlei5=unicode(raw_input((u"%s改为："%fenlei5).encode("gbk")),"gbk")
      else:
        break


        
      
    #公司简介
    print u"创建%s中"%fenlei1
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/3.png","orange/3.png","yellow/3.png","green/3.png","blue/3.png","gray/24.png","purple/3.png","brown/3.png","white/21.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/fangdichan/fangdichan_"+imagelist[yanse-1]
    pd={}
    pd["name"]=en(fenlei1)
    pd["img"]=imgurl
    pd["sorts"]="6"
    pd["tpid"]="1"
    pd["conttpid"]="1"
    pd["status"]="1"
    pd["url"]=""
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei1
    



    #产品展示
    url="/index.php?g=User&m=Photo&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print (u"创建相册中...")
    url="/index.php?g=User&m=Photo&a=add&token="
    data=request(host1, url, headers1,"button=&title=%s&picurl=http://37t.cn/tpl/static/attachment/focus/default/2.jpg&info=%s&isshowinfo=0&status=1&__hash__=%s"%(en(fenlei2),en(fenlei2),__hash__))
    print u"相册创建成功！"
    print u"获取相册信息"
    url="/index.php?g=User&m=Link&a=Photo&iskeyword=0"
    data=request(host1, url, headers1)
    gnurl=re.findall("returnHomepage\('(.*?)'\)",data)[0]
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei2
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/11.png","orange/11.png","yellow/11.png","green/11.png","blue/11.png","gray/21.png","purple/11.png","brown/11.png","white/25.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/edu/edu_"+imagelist[yanse-1]
    pd["name"]=en(fenlei2)
    pd["img"]=imgurl
    pd["sorts"]="5"
    pd["url"]=gnurl
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei2
    #联系我们
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei3
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/19.png","orange/19.png","yellow/19.png","green/19.png","blue/19.png","gray/1.png","purple/19.png","brown/19.png","white/27.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/edu/edu_"+imagelist[yanse-1]
    pd["name"]=en(fenlei3)
    pd["img"]=imgurl
    pd["sorts"]="3"
    pd["url"]=""
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei3
    #地图导航
    print u"获取地图信息"
    url="/index.php?g=User&m=Link&a=Company&iskeyword=0"
    data=request(host1, url, headers1)
    gnurl=re.findall("returnHomepage\('(.*?)'\)",data)[0]
    
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei4
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/18.png","orange/18.png","yellow/18.png","green/18.png","blue/18.png","gray/9.png","purple/18.png","brown/18.png","white/11.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/canyin/canyin_"+imagelist[yanse-1]
    pd["name"]=en(fenlei4)
    pd["img"]=imgurl
    pd["sorts"]="2"
    pd["url"]=gnurl
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei4  
    #在线留言
    gnurl="{siteUrl}/index.php?g=Wap&m=Reply&a=index&token=%s&wecha_id={wechat_id}"%token
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei5
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/15.png","orange/15.png","yellow/15.png","green/15.png","blue/15.png","gray/2.png","purple/15.png","brown/15.png","white/21.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/canyin/canyin_"+imagelist[yanse-1]
    pd["name"]=en(fenlei5)
    pd["img"]=imgurl
    pd["sorts"]="1"
    pd["url"]=gnurl
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei5
################################################################################################################
  #5.5类+动态
  elif fenlei=="5":
    fenlei1=u"公司简介"
    fenlei2=u"相关知识"
    fenlei3=u"联系我们"
    fenlei4=u"地图导航"
    fenlei5=u"在线留言"
    while True:
      print u"1.%s"%fenlei1
      print u"2.%s"%fenlei2
      print u"3.%s"%fenlei3
      print u"4.%s"%fenlei4
      print u"5.%s"%fenlei5
      xiugai=raw_input(u"输入修改项目序号，输入其他进入下一步：".encode("gbk"))
      if xiugai=="1":
        fenlei1=unicode(raw_input((u"%s改为："%fenlei1).encode("gbk")),"gbk")
      elif xiugai=="2":
        fenlei2=unicode(raw_input((u"%s改为："%fenlei2).encode("gbk")),"gbk")
      elif xiugai=="3":
        fenlei3=unicode(raw_input((u"%s改为："%fenlei3).encode("gbk")),"gbk")
      elif xiugai=="4":
        fenlei4=unicode(raw_input((u"%s改为："%fenlei3).encode("gbk")),"gbk")
      elif xiugai=="5":
        fenlei5=unicode(raw_input((u"%s改为："%fenlei5).encode("gbk")),"gbk")
      else:
        break


        
      
    #公司简介
    print u"创建%s中"%fenlei1
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/3.png","orange/3.png","yellow/3.png","green/3.png","blue/3.png","gray/24.png","purple/3.png","brown/3.png","white/21.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/fangdichan/fangdichan_"+imagelist[yanse-1]
    pd={}
    pd["name"]=en(fenlei1)
    pd["img"]=imgurl
    pd["sorts"]="6"
    pd["tpid"]="1"
    pd["conttpid"]="1"
    pd["status"]="1"
    pd["url"]=""
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei1




    #相关知识
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei2
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/15.png","orange/15.png","yellow/15.png","green/15.png","blue/15.png","gray/3.png","purple/15.png","brown/15.png","white/21.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/edu/edu_"+imagelist[yanse-1]
    pd["name"]=en(fenlei2)
    pd["img"]=imgurl
    pd["sorts"]="4"
    pd["url"]=""
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei2
    #联系我们
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei3
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/19.png","orange/19.png","yellow/19.png","green/19.png","blue/19.png","gray/1.png","purple/19.png","brown/19.png","white/27.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/edu/edu_"+imagelist[yanse-1]
    pd["name"]=en(fenlei3)
    pd["img"]=imgurl
    pd["sorts"]="3"
    pd["url"]=""
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei3
    #地图导航
    print u"获取地图信息"
    url="/index.php?g=User&m=Link&a=Company&iskeyword=0"
    data=request(host1, url, headers1)
    gnurl=re.findall("returnHomepage\('(.*?)'\)",data)[0]
    
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei4
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/18.png","orange/18.png","yellow/18.png","green/18.png","blue/18.png","gray/9.png","purple/18.png","brown/18.png","white/11.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/canyin/canyin_"+imagelist[yanse-1]
    pd["name"]=en(fenlei4)
    pd["img"]=imgurl
    pd["sorts"]="2"
    pd["url"]=gnurl
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei4
    #在线留言
    gnurl="{siteUrl}/index.php?g=Wap&m=Reply&a=index&token=%s&wecha_id={wechat_id}"%token
    url="/index.php?g=User&m=Classify&a=add"
    data=request(host1, url, headers1)   
    __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
    print u"创建%s中"%fenlei5
    url="/index.php?g=User&m=Classify&a=insert"
    imagelist=["red/15.png","orange/15.png","yellow/15.png","green/15.png","blue/15.png","gray/2.png","purple/15.png","brown/15.png","white/21.png"]
    imgurl="http://37t.cn/tpl/static/attachment/icon/canyin/canyin_"+imagelist[yanse-1]
    pd["name"]=en(fenlei5)
    pd["img"]=imgurl
    pd["sorts"]="1"
    pd["url"]=gnurl
    pd["__hash__"]=__hash__ 
    data=request(host1, url, headers1,urllib.urlencode(pd))
    print u"%s创建完成"%fenlei5
  else:pass
  print u"开始创建文章..."
  print u"创建%s"%fenlei1
  url="/index.php?g=User&m=Img&a=add"
  data=request(host1, url, headers1)   
  __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
  url="/index.php?g=User&m=Img&a=insert"
  pd={}
  pd["precisions"]="0"
  pd["title"]=en(fenlei1)
  pd["classid"]=en(u"5039,的撒发生")
  pd["pic"]="http://37t.cn/uploads/w/wsweyi1428396337/d/0/6/b/thumb_5545d69fa7928.jpg"
  pd["showpic"]="1"
  pd["info"]=en(u'<span style="font-size:16px;font-family:SimSun;">　　%s</span>'%gsjj)
  pd["pc_cat_id"]="0"
  pd["pc_show"]="0"
  pd["texttype"]="1"
  pd["sbmt"]=en(u"保存")
  pd["__hash__"]=__hash__ 
  data=request(host1, url, headers1,urllib.urlencode(pd))

  
  

host2="oa.qz160168.cn"
headers2 = {'User-Agent':'Opera/9.80 (Windows NT 5.1; U; Edition Next; zh-cn) Presto/2.10.289 Version/12.00','Accept':'text/html, application/xhtml+xml, */*','Accept-Language':'zh-CN','Accept-Encoding':'gzip, deflate','Cache-Control':'no-cache','Connection':'Keep-Alive'}

  
def loginoa():
  print u"登陆OA系统中！"
  url="/login.asp?Menu=Submit"
  data=request(host2, url, headers2,"username=linh&userpass=330362495")
  print (re.findall("'(.*?)'",data)[0]).decode("gbk")
  page=1
  while True:
    url="/wljcburl.asp?ToPage=%s"%str(page)
    data=request(host2, url, headers2)
    print re.findall('<td colspan="10"  align="center">(.*?)</td>',data)[0].decode("gbk")
    danlist=re.findall("<tr onMouseOver=(.*?)</tr>",data.replace("\n","").replace("　".encode("gbk"),""))
    n=0
    idlist=[]
    for i in danlist:
      infolist=re.findall('<td>(.*?)</td>',i)
      idlist.append(infolist[0])
      n+=1
      print u"%s.%s(建站人:%s)"%(str(n), infolist[1].decode("gbk"),infolist[13].decode("gbk"))
    while True:
      xuhao=raw_input(u"请输入建站序号(0刷新，00下一页，000上一页)：".encode("gbk"))
      if xuhao=="0":
        break
      elif xuhao=="00":
        page+=1
        break
      elif xuhao=="000":
        page-=1
        break
      else:
        try:
          id=idlist[int(xuhao)-1]
          while True:
            queren=raw_input(u"输入1开始建站，任意返回：".encode("gbk"))
            if queren!="1":break
            #获取单子信息
            else:
              url="/wljcburl.asp?Menu=Edit&ID=%s"%id
              data=request(host2, url, headers2)
              #keep("D://q.txt",data)
              jfhm=re.findall('id="jfhm" size="15" style="width:90%" value="(.*?)"',data)[0]
              gsjc=re.findall('name="gsjc" size="20" value="(.*?)"',data)[0]
              gsdz=re.findall('id="gsdz" value="(.*?)"',data)[0]
              kddh=re.findall('name="kddh" size="20" value="(.*?)"',data)[0]
              gsjj=re.findall('>(.*?)</tex',re.findall('name="gsjs"(.*?)area>',data)[0])[0]
              gsjj=gsjj.replace("\n","").replace("　".encode("gbk"),"").replace(" ","").replace(".",u"。".encode("gbk"))
              # print jfhm
              # print gsjc
              # print gsdz
              # print kddh
              # print gsjj
              #计费账号，密码，公司简介，公司简称，刊登电话，公司地址
              login("qq330362495","330362495",gsjj,gsjc,kddh,gsdz)
              
              
              
              
              
              
              
              
              break
          break  
        except Exception,ex:
          print ex
          pass

	
try:
  loginoa()
  #login("83181","123456")
  os.system("pause")
except Exception,ex:
  print Exception,":",ex
  os.system("pause") 
