#encoding=utf-8
import urllib
import urllib2
#python中字典的另外一种写法
values={}
values["username"]="154943046@qq.com"
values["password"]="XXXX"
data=urllib.urlencode(values)
url="https://passport.csdn.net/account/login"
geturl=url+"?"+data#get方式传送数据
print geturl
request=urllib2.Request(geturl)

response=urllib2.urlopen(request)
print response.read()
