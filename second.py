#encoding=utf-8
import urllib2
request=urllib2.Request("http://www.baidu.com")#构造一个request对象实例
response=urllib2.urlopen(request)
print response.read()