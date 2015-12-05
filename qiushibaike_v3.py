#encoding=utf-8
#功能：抓取糗事百科的第二个版本
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
url="http://www.qiushibaike.com/hot/page/1"
user_agent="Mozilla/5.0 (Windows NT 6.1)"
headers={"User-Agent":user_agent}#请求头
try:
	request=urllib2.Request(url,headers=headers)
	response=urllib2.urlopen(request)
	content = response.read().decode('utf-8')
	# print content
	# #利用正则进行匹配
	# pattern = re.compile('<div.*?author clearfix">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         # 'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
	# items = re.findall(pattern,content)
	# for item in items:
		# haveImg=re.search("img",item[3])#判断是否有图片
		# if not haveImg:
			# print item[0],item[1],item[2],item[4]
	soup=BeautifulSoup(content,"html.parser")
	print soup.prettify()
	soup.find_all(div)
except urllib2.URLError,e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason
