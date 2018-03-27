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
##gsjjimg=["http://i1.tietuku.com/66b1b72038a34a17.jpg","http://i1.tietuku.com/522cdb6ad9e553eb.jpg","http://i1.tietuku.com/e9d6705bd58f0b11.jpg","http://i1.tietuku.com/cf11a0be955fc15f.jpg","http://i1.tietuku.com/f42b1071598f8e31.jpg","http://i1.tietuku.com/14a5dcfcd33d03a8.jpg","http://i1.tietuku.com/44400067c2d3d14e.jpg","http://i4.tietuku.com/ff524e39e34bd1fe.jpg","http://i4.tietuku.com/3a3fee9f076ed7b0.jpg","http://i1.tietuku.com/5a72a0dd8a09b593.jpg","http://i1.tietuku.com/1566f1ebac5f7cf5.jpg"]
gsjjimg="1.jpg|2.jpg|3.jpg|4.jpg|5.jpg|6.jpg|7.jpg|8.jpg|9.jpg|10.jpg|11.jpg|12.jpg|13.jpg|16.jpg|17.jpg|18.jpg|19.jpg|20.jpg|21.jpg|22.jpg|23.jpg|24.jpg|25.jpg|26.jpg|27.jpg|28.jpg|29.jpg|31.jpg|32.jpg|33.jpg|34.jpg|35.jpg|36.jpg|37.jpg|38.jpg|39.jpg|40.jpg|41.jpg|42.png|43.png|44.png|45.png|46.png|47.png|48.png|49.png|50.png|51.png|52.png|53.png|54.png|55.png|56.png".split("|")

##lxwmimg=["http://i4.tietuku.com/069338f324af4a7a.jpg","http://i2.tietuku.com/6690b880ffdb8e24.jpg","http://i2.tietuku.com/f2f87f97b5192519.jpg","http://i2.tietuku.com/31821d2c2b94d176.gif","http://i2.tietuku.com/4fe65c0513a1b532.jpg","http://i2.tietuku.com/606003007ccb5c0b.jpg","http://i2.tietuku.com/ed2e830792de4ec0.jpg","http://i2.tietuku.com/6c23cf43bc48d65e.jpg","http://i2.tietuku.com/bce226b1154f6e2e.jpg","http://i2.tietuku.com/8315d29e1af8ddad.jpg"]
lxwmimg="1.jpg|2.jpg|3.jpg|4.jpg|5.jpg|6.jpg|7.jpg|8.jpg|9.jpg|10.jpg|11.jpg|12.jpg|13.jpg|14.jpg|15.jpg|16.jpg|17.jpg|18.jpg|19.jpg|20.jpg|21.jpg|22.jpg|23.gif|24.gif|25.gif|26.gif|27.gif|28.png".split("|")
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

def addarticle(fenlei0):
  wzpath=os.getcwd()+u"\\文章".encode("gbk")
  while True:
    print u"选择文章..."
    print u"00.结束创建"
    print u"0.返回上一层"
    wzlist=os.listdir(wzpath)
    n=1
    for i in wzlist:
      print str(n)+"."+i.decode("gbk")
      n+=1
    while True:
      xuhao=raw_input(u"请输入文章序号：".encode("gbk"))
      if xuhao=="0" or xuhao=="00":
        wzpath=os.getcwd()+u"\\文章".encode("gbk")
        break
      if int(xuhao)>0 and int(xuhao)<len(wzlist)+1:
        if os.path.isdir(wzpath+"\\"+wzlist[int(xuhao)-1]):
          wzpath=wzpath+"\\"+wzlist[int(xuhao)-1]
          break
        else:
          
          f=open(wzpath+"\\"+wzlist[int(xuhao)-1],"r+")
          fdata=f.read()
          f.close()
          print u"创建"
          url="/index.php?g=User&m=Img&a=add"
          data=request(host1, url, headers1)   
          __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
          
          url="/index.php?g=User&m=Img&a=editClass"
          data=request(host1, url, headers1)   
          for i in re.findall("returnHomepage\((.*?)',",data):
            if i.find(fenlei0)!=-1:
              classid=i.replace("'","")

          
          url="/index.php?g=User&m=Img&a=insert"
          pd={}
          pd["precisions"]="0"
          pd["title"]=unicode(os.path.splitext(wzlist[int(xuhao)-1])[0],"gbk")
          pd["classid"]=classid
          pd["showpic"]="0"
          pd["info"]=fdata#en(u'<span style="font-size:16px;font-family:SimSun;">　　%s</span>'%gsjj.decode("gbk"))+u'<br/><span style="font-size:16px;font-family:SimSun;">　　我们尊崇“踏实、拼搏、责任”的企业精神，并以诚信、共赢、开创经营理念，创造良好的企业环境，以全新的管理模式，完善的技术，周到的服务，卓越的品质为生存根本，我们始终坚持用户至上 用心服务于客户，坚持用自己的服务去打动客户。</span>'
          pd["pc_cat_id"]="0"
          pd["pc_show"]="0"
          pd["texttype"]="1"
          pd["sbmt"]=en(u"保存")
          pd["__hash__"]=__hash__ 
          data=request(host1, url, headers1,urllib.urlencode(pd))
          break
    if xuhao=="00":break
  print u"文章创建完成！"
    
  
  
  
  
  
def login(username,password,gsjj,gsjc,kddh,gsdz):
  if len(username)==8:
    username="0595"+username
  print username
  if len(kddh)==8:
    kddh="0595-"+kddh
  url="/index.php?m=Index&a=login"
  data=request(host1, url, headers1)
  __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
  verifycode2="1234"#raw_input("code:")
  url="/index.php?m=Users&a=checklogin"
  data=request(host1, url, headers1,"username=%s&password=%s&verifycode=%s&__hash__=%s"%(username,password,verifycode2,__hash__))
  token=re.findall('token=(.*?)"',data)[0]
  print cn(re.findall('<span>(.*?)</span>',data)[0])
  print u"删除自带分类文章中...."
  url="/index.php?g=User&m=Classify&a=index&token="+token
  data=request(host1, url, headers1)
  try:
    for i in re.findall('href="(.*?)">删',data):
      request(host1, i, headers1)
  except Exception,ex:pass
  url="/index.php?g=User&m=Img&a=index&token="+token
  data=request(host1, url, headers1)
  try:
    for i in re.findall('href="(.*?)">删',data):
      request(host1, i, headers1)
  except Exception,ex:pass
  url="/index.php?g=User&m=Photo&a=index&token="+token
  data=request(host1, url, headers1)
  try:
    for i in re.findall(", '(.*?)'",data):
      request(host1, i, headers1)
  except Exception,ex:pass 
  print u"开始创建分类..."
  yanse=10
  # print u"1.红色"
  # print u"2.橙色"
  # print u"3.黄色"
  # print u"4.绿色"
  # print u"5.蓝色"
  # print u"6.灰色"
  # print u"7.紫色"
  # print u"8.棕色"
  # print u"9.白色"
  # print u"10.卡通"
  # while True:
    # yanse=raw_input(u"请输入图标颜色(直接回车默认6)：".encode("gbk"))
    # if len(yanse)==0:
      # yanse=6
      # break
    # else:
      # if yanse=="1" or yanse=="2" or yanse=="3" or yanse=="4" or yanse=="5" or yanse=="6" or yanse=="7" or yanse=="8" or yanse=="9" or yanse=="10":
        # yanse=int(yanse)
        # break
    
    
    
  #1.标准6类  

  fenlei1=u"公司简介"
  fenlei2=u"相关展示"
  fenlei3=u"相关资讯"
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
  imagelist=["http://37t.cn/tpl/static/attachment/icon/fangdichan/fangdichan_red/3.png","http://37t.cn/tpl/static/attachment/icon/fangdichan/fangdichan_orange/3.png","http://37t.cn/tpl/static/attachment/icon/fangdichan/fangdichan_yellow/3.png","http://37t.cn/tpl/static/attachment/icon/fangdichan/fangdichan_green/3.png","http://37t.cn/tpl/static/attachment/icon/fangdichan/fangdichan_blue/3.png","http://37t.cn/tpl/static/attachment/icon/fangdichan/fangdichan_gray/24.png","http://37t.cn/tpl/static/attachment/icon/fangdichan/fangdichan_purple/3.png","http://37t.cn/tpl/static/attachment/icon/fangdichan/fangdichan_brown/3.png","http://37t.cn/tpl/static/attachment/icon/fangdichan/fangdichan_white/21.png","http://37t.cn/tpl/static/attachment/icon/lovely/bill.png"]
  imgurl=imagelist[yanse-1]
  pd={}
  pd["name"]=en(fenlei1)
  pd["img"]=imgurl
  pd["sorts"]="6"
  pd["tpid"]="258"
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
  imagelist=["http://37t.cn/tpl/static/attachment/icon/edu/edu_red/11.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_orange/11.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_yellow/11.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_green/11.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_blue/11.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_gray/21.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_purple/11.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_brown/11.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_white/25.png","http://37t.cn/tpl/static/attachment/icon/lovely/eye.png"]
  imgurl=imagelist[yanse-1]
  pd["name"]=en(fenlei2)
  pd["img"]=imgurl
  pd["sorts"]="5"
  pd["url"]=gnurl
  pd["__hash__"]=__hash__ 
  data=request(host1, url, headers1,urllib.urlencode(pd))
  print u"%s创建完成"%fenlei2
  #相关资讯
  url="/index.php?g=User&m=Classify&a=add"
  data=request(host1, url, headers1)   
  __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
  print u"创建%s中"%fenlei3
  url="/index.php?g=User&m=Classify&a=insert"
  imagelist=["http://37t.cn/tpl/static/attachment/icon/edu/edu_red/15.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_orange/15.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_yellow/15.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_green/15.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_blue/15.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_gray/3.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_purple/15.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_brown/15.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_white/21.png","http://37t.cn/tpl/static/attachment/icon/lovely/1.png"]
  imgurl=imagelist[yanse-1]
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
  imagelist=["http://37t.cn/tpl/static/attachment/icon/edu/edu_red/19.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_orange/19.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_yellow/19.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_green/19.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_blue/19.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_gray/1.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_purple/19.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_brown/19.png","http://37t.cn/tpl/static/attachment/icon/edu/edu_white/27.png","http://37t.cn/tpl/static/attachment/icon/lovely/open-letter.png"]
  imgurl=imagelist[yanse-1]
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
  dturl=re.findall("returnHomepage\('(.*?)'\)",data)[0]
  
  url="/index.php?g=User&m=Classify&a=add"
  data=request(host1, url, headers1)   
  __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
  print u"创建%s中"%fenlei5
  url="/index.php?g=User&m=Classify&a=insert"
  imagelist=["http://37t.cn/tpl/static/attachment/icon/canyin/canyin_red/18.png","http://37t.cn/tpl/static/attachment/icon/canyin/canyin_orange/18.png","http://37t.cn/tpl/static/attachment/icon/canyin/canyin_yellow/18.png","http://37t.cn/tpl/static/attachment/icon/canyin/canyin_green/18.png","http://37t.cn/tpl/static/attachment/icon/canyin/canyin_blue/18.png","http://37t.cn/tpl/static/attachment/icon/canyin/canyin_gray/9.png","http://37t.cn/tpl/static/attachment/icon/canyin/canyin_purple/18.png","http://37t.cn/tpl/static/attachment/icon/canyin/canyin_brown/18.png","http://37t.cn/tpl/static/attachment/icon/canyin/canyin_white/11.png","http://37t.cn/tpl/static/attachment/icon/lovely/map.png"]
  imgurl=imagelist[yanse-1]
  pd["name"]=en(fenlei5)
  pd["img"]=imgurl
  pd["sorts"]="2"
  pd["url"]=dturl
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
  imagelist=["http://37t.cn/tpl/static/attachment/icon/canyin/canyin_red/15.png","http://37t.cn/tpl/static/attachment/icon/canyin/canyin_orange/15.png","http://37t.cn/tpl/static/attachment/icon/canyin/canyin_yellow/15.png","http://37t.cn/tpl/static/attachment/icon/canyin/canyin_green/15.png","http://37t.cn/tpl/static/attachment/icon/canyin/canyin_blue/15.png","http://37t.cn/tpl/static/attachment/icon/canyin/canyin_gray/2.png","http://37t.cn/tpl/static/attachment/icon/canyin/canyin_purple/15.png","http://37t.cn/tpl/static/attachment/icon/canyin/canyin_brown/15.png","http://37t.cn/tpl/static/attachment/icon/canyin/canyin_white/21.png","http://i1.tietuku.com/5be9442216db9f5a.png"]
  imgurl=imagelist[yanse-1]
  pd["name"]=en(fenlei6)
  pd["img"]=imgurl
  pd["sorts"]="1"
  pd["url"]=gnurl
  pd["__hash__"]=__hash__ 
  data=request(host1, url, headers1,urllib.urlencode(pd))
  print u"%s创建完成"%fenlei6
  addarticle(fenlei3)
##################################################################################################################

  
#################################################################################################################
  rand=random.randint(0,len(gsjjimg)-1)
  randimg="http://37t.cn/tpl/static/attachment/introduction/"+gsjjimg[rand]
  print u"开始创建文章..."
  print u"创建%s"%fenlei1
  url="/index.php?g=User&m=Img&a=add"
  data=request(host1, url, headers1)   
  __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
  
  url="/index.php?g=User&m=Img&a=editClass"
  data=request(host1, url, headers1)   
  for i in re.findall("returnHomepage\((.*?)',",data):
    if i.find(fenlei1)!=-1:
      classid=i.replace("'","")

  
  url="/index.php?g=User&m=Img&a=insert"
  pd={}
  pd["precisions"]="0"
  pd["title"]=en(fenlei1)
  pd["classid"]=classid
  pd["pic"]=randimg
  pd["showpic"]="1"
  pd["info"]=en(u'<span style="font-size:16px;font-family:SimSun;">　　%s</span>'%gsjj.decode("gbk"))+u'<br/><span style="font-size:16px;font-family:SimSun;">　　我们尊崇“踏实、拼搏、责任”的行业精神，并以诚信、共赢、开创经营理念，创造良好的行业环境，以全新的管理模式，完善的技术，周到的服务，卓越的品质为生存根本，我们始终坚持用户至上 用心服务于客户，坚持用自己的服务去打动客户。</span>'
  pd["pc_cat_id"]="0"
  pd["pc_show"]="0"
  pd["texttype"]="1"
  pd["sbmt"]=en(u"保存")
  pd["__hash__"]=__hash__ 
  data=request(host1, url, headers1,urllib.urlencode(pd))

###########
  rand=random.randint(0,len(lxwmimg)-1)
  randimg="http://37t.cn/tpl/static/attachment/contact/"+lxwmimg[rand]
  dturl=dturl.replace("{siteUrl}","").replace("{wechat_id}","")
  print u"创建联系我们"
  url="/index.php?g=User&m=Img&a=add"
  data=request(host1, url, headers1)   
  __hash__=re.findall('__hash__" value="(.*?)"',data)[0]
  
  url="/index.php?g=User&m=Img&a=editClass"
  data=request(host1, url, headers1)   
  for i in re.findall("returnHomepage\((.*?)',",data):
    if i.find("联系我们")!=-1:
      classid=i.replace("'","")
  
  url="/index.php?g=User&m=Img&a=insert"
  pd={}
  pd["precisions"]="0"
  pd["title"]=en(u"联系我们")
  pd["classid"]=classid
  pd["pic"]=randimg
  pd["showpic"]="1"
  pd["info"]=en(u'<p><span style="font-size:16px;font-family:SimSun;">%s</span></p><p><span style="font-size:16px;font-family:SimSun;">电话：<a target="_blank" href="tel:%s">%s</a></span></p><p><span style="font-size:16px;font-family:SimSun;">地址：<a href="http://37t.cn%s">%s</a></span></p>'%(gsjc.decode("gbk"),kddh,kddh,dturl,gsdz.decode("gbk")))
  pd["pc_cat_id"]="0"
  pd["pc_show"]="0"
  pd["texttype"]="1"
  pd["sbmt"]=en(u"保存")
  pd["__hash__"]=__hash__ 
  data=request(host1, url, headers1,urllib.urlencode(pd))  
  raw_input(u"创建完毕，回车继续建站！".encode("gbk"))
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
    danlist=re.findall("<tr onMouseOver=(.*?)</tr>",data.replace("\n","").replace("　".encode("gbk"),""))
    n=0
    idlist=[]
    namelist=[]
    userlist=[]
    for i in danlist:
      infolist=re.findall('<td>(.*?)</td>',i)
      idlist.append(infolist[0])
      namelist.append(infolist[1])
      userlist.append(infolist[13])
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
          name=namelist[int(xuhao)-1]
          user=userlist[int(xuhao)-1]
          while True:
            queren=raw_input(u"输入1开始建%s，任意返回：".encode("gbk")%(name+":"+user))
            if queren!="1":break
            #获取单子信息
            else:
              url="/wljcburl.asp?Menu=Edit&ID=%s"%id
              data=request(host2, url, headers2)
              
              keep("D://q.txt",data)
              jfhm=re.findall('<td colspan="5">(.*?)</td>',data)[0]
              password=re.findall('<td colspan="5">(.*?)</td>',data)[1]
              gsjc=re.findall('name="gsjc" size="20" value="(.*?)"',data)[0]
              gsdz=re.findall('id="gsdz" value="(.*?)"',data)[0]
              kddh=re.findall('name="kddh" size="20" value="(.*?)"',data)[0]
              gsjj=re.findall('>(.*?)</tex',re.findall('name="gsjs"(.*?)area>',data.replace("\r\n","</br>").replace("\n\r","</br>").replace("\n","</br>").replace("\r","</br>").replace("　".encode("gbk"),"").replace(" ","").replace(".",u"。".encode("gbk")))[0])[0]
              print 1
              #gsjj=gsjj.replace("\n","").replace("　".encode("gbk"),"").replace(" ","").replace(".",u"。".encode("gbk"))
              # print jfhm
              # print gsjc
              # print gsdz
              # print kddh
              # print gsjj
              #计费账号，密码，公司简介，公司简称，刊登电话，公司地址
              login(jfhm,password,gsjj,gsjc,kddh,gsdz)
              
              
              
              
              
              
              
              
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
