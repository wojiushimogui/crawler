#encoding=utf-8
#完成的功能为：将cookie写入文件中
import urllib2
import cookielib
file="cookie.txt"
#第一步：利用FileCookieJar的子类MozillaCookieJar
cookie=cookielib.MozillaCookieJar(file)
#第二步：用HTTPCookieProcessor来创建一个Cookie的处理器
hander=urllib2.HTTPCookieProcessor(cookie)
#第三步：创建一个opener
opener=urllib2.build_opener(hander)
#创建一个请求
response=opener.open("http://www.baidu.com")
#第四步：将cookie保存到文本中
cookie.save(ignore_discard=True,ignore_expires=True)
