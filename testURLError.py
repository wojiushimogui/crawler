#encoding=utf-8
#访问错误的URL的抛异常的处理
#首先解释下URLError可能产生的原因：
#	网络无连接，即本机无法上网
#	连接不到特定的服务器
#	服务器不存在

import urllib2
url="http://wuranghao.com"
request=urllib2.Request(url)
try:
	response=urllib2.urlopen(request)
except urllib2.URLError,e:
	print e.reason  #输出  [Errno 11004] getaddrinfo failed