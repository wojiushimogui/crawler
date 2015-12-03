#encoding=utf-8
#设置请求头
import urllib
import urllib2
user_agent="Mozilla/5.0 (Windows NT 6.1)"
referer="http://www.zhihu.com/"
header={"User-Agent":user_agent,"Referer":referer}
url="http://www.zhihu.com/"
values={"username":"wuranghao","password":"xxxx"}
data=urllib.urlencode(values)
request=urllib2.Request(url ,data ,header)
response=urllib2.urlopen(request)
print response.read()