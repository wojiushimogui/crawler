#encoding=utf-8
#post 方式传送数据
import urllib
import urllib2
values={'username':'154943046@qq.com','password':'wuranghao'}
data=urllib.urlencode(values)#将提交的字典编码
url="https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request=urllib2.Request(url,data)
response=urllib2.urlopen(request)
print response.read()
