#encoding=utf-8
#功能：抓取糗事百科段子的第一个版本
import urllib
import urllib2
url="http://www.qiushibaike.com/hot/page/1"
#添加一个请求头
user_agent="Mozilla/5.0 (Windows NT 6.1)"
headers={"User-Agent":user_agent}
try:
	request=urllib2.Request(url,headers=headers)
	response=urllib2.urlopen(request)
	print response.read()
except urllib2.URLError,e:
	if hasattr(e,"code"):
		print e.cond
	if hasattr(e,"reason"):
		print e.reason