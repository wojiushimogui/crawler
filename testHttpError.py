#encoding=utf-8
#HTTPError的讲解：HTTPError是URLError的子类，在你利用urlopen方法发出一个请求时，
#服务器上都会对应一个应答对象response，其中它包含一个数字”状态码”。
import urllib2
url="http://www.xingjiakmite.com"
request=urllib2.Request(url)
try:
	response=urllib2.urlopen(request)
except urllib2.HTTPError,e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason
except urllib2.URLError,e:
	if hasattr(e,"reson"):
		print e.reason
else:
	print "OK"