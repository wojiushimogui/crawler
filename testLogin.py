#encoding=utf-8
#功能：模拟网站登陆
import urllib2
import urllib
import cookielib
#第一步：创建一个cookie变量
file="cookie_1.txt"
cookie=cookielib.MozillaCookieJar(file)
#第二步：利用urllib2的HTTPCookieProcessor来创建一个cookie处理器
hander=urllib2.HTTPCookieProcessor(cookie)
#第三步：创建一个opener
opener=urllib2.build_opener(hander)
#要传送的data
values={"stuid":"xxxxx","pwd":"xxxxxx"}
data=urllib.urlencode(values)
url="http://idas.uestc.edu.cn/authserver/login"
request=urllib2.Request(url,data)
#模拟登陆
response=opener.open(request)
#第四步：保存cookie
cookie.save(ignore_discard=True,ignore_expires=True)
#利用此时的cookie变量来访问另外一个网站
gradeurl="http://bbs.uestc.edu.cn/"
response=opener.open(gradeurl)
print response.read()
