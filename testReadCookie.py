#encoding=utf-8
#从文本中读取cookie来访问网页
import urllib2
import urllib
import cookielib
file="cookie.txt"
#第一步：创建一个cookie变量
cookie=cookielib.MozillaCookieJar()
#第二步：对文件读取cookie到变量中
cookie.load(file,ignore_discard=True,ignore_expires=True)
#第三步：利用urllib2的HTTPCookieProcessor来创建一个cookie处理器
hander=urllib2.HTTPCookieProcessor(cookie)
#第四步：创建一个opener
opener=urllib2.build_opener(hander)
#创建一个请求
request=urllib2.Request("http://www.baidu.com")
response=opener.open(request)
print response.read()
