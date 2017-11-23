#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
注意:
1.填入你的cookie
'''

__author__ = 'wyl QQ635864540'

'''
Created on 20171122
@author:wyl QQ635864540
'''

import urllib2
import urllib2
import re
import time

class GetAllBars:
	def __init__(self, url=None):
		self.compiler=re.compile(r'title="([^\s]*?)">', re.IGNORECASE)
			
	def FindAllBars(self):
		result = []
		page = 1
		while True:
			url = 'http://tieba.baidu.com/f/like/mylike?&pn={}'
			url = url.format(page)
			#'Accept-Encoding':'gzip, deflate', #这一段加上之后导致获取到的html为乱码，所以去掉
			headers = {
				'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
				'Accept-Language':'zh-CN,zh;q=0.8',
				'Cache-Control':'max-age=0',
				'Connection':'keep-alive',
				'Cookie':'',#填入你的cookie
				'Host':'tieba.baidu.com',
				'Upgrade-Insecure-Requests':'1',
				'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
				}
			try:
				request = urllib2.Request(url=url, headers=headers)
				response = urllib2.urlopen(request)
				html = response.read()
				response.close()
				#print html
				findres = self.compiler.findall(html)
				if len(findres) is 0:
					response.close()
					break
				result = result + findres
			except Exception as e:
				print 'exception in FindAllBars:', str(e)
				if hasattr(e, 'code'):
					code = e.code
				else:
					code = None
			page = page + 1			
		return result
		
if __name__=='__main__':
	gb = GetAllBars()
	result = gb.FindAllBars()
	for res in result:
		print res
	print len(result)