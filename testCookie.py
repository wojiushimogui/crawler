#encoding=utf-8
#保存cookie到变量
import urllib2
import cookielib
#第一步：得到一个cookie实例对象
cookie=cookielib.CookieJar()
#第二步：利用urllib2库的HTTPCookieProcessor对象
hander=urllib2.HTTPCookieProcessor(cookie)
#第三步：得到一个opener
opener=urllib2.build_opener(hander)
response=opener.open("http://www.baidu.com")
for item in cookie:
	print "Name="+item.name
	print "Value="+item.value
