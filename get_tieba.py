#encoding=utf-8
#功能：爬取贴吧上面的图片
import urllib2
import urllib
#raw_input是python的一个内置函数，通过读取控制台的输入与用户实现交互。
#input也可以读取控制台的输入与用户实现交互，但是input和raw_input由一定的差异，
#例如：raw_input将控制台上所有的输入均作为字符串（即使全是数字组合）来进行处理，而input对输入有一定的要求，如果输入的是字符串，则一定要用引号
#从控制台输入一个url
url=raw_input("raw_input":)
try:
	request=urllib2.Request(url)
	response=urllib2.urlopen(request)
	content=response.read().decode("utf-8")
except urllib2.URLError,e:
	if hasattr(e,"reason"):
		print e.reason
#定义一个函数，得到内容
def getContent(content):
	#利用正则来进行匹配
	pattern=re.compile(r'src="(.*?)" pic_ext=')
	items=re.findall(pattern,content)
	count=0
	for item in items:
		count++
		urllib2.urlretrieve(item,"%s.jpg"  % count)

getContent(content)