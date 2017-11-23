#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'wyl QQ635864540'


'''
注意:
1.填入你的cookie
2.填入你的tbs
'''


'''
Created on 20171122
@author:wyl QQ635864540
'''

import urllib2
import re
import urllib
import time
import getallbars
import json


class TieBaLoginCls:
	def __init__(self, bars = None):
		self.url='http://tieba.baidu.com/sign/add'
		self.debug_on = True
		self.bars = bars
	
	def __del__(self):
		self.url=''
	
	def Login(self):
		for bar in self.bars:
			print bar
			bar =bar.decode('gbk').encode('utf-8')
			headers = {
				'Accept':'application/json, text/javascript, */*; q=0.01',
				'Accept-Language':'zh-CN,zh;q=0.8',
				'Connection':'keep-alive',
				'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
				'Cookie':'',#填入你的cookie
				'Host':'tieba.baidu.com',
				'Origin':'http://tieba.baidu.com',
				'Referer':'http://tieba.baidu.com/f?kw=%s&fr=index&fp=0&ie=utf-8',
				'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36',
				'X-Requested-With':'XMLHttpRequest'
				}
			bardata={
				'ie':'utf-8',
				'kw':bar,
				'tbs':''#填入你的tbs
				}
			headers['Referer']=headers['Referer'] % bar
			if self.debug_on:
				print headers['Referer']
			try:
				request = urllib2.Request(url=self.url, data=urllib.urlencode(bardata).encode(), headers=headers)
				response=urllib2.urlopen(request)
				html = response.read()
				if html.find('errmsg') != -1:
					errindex = html.find('errmsg')
					msgindex = html.find('",', errindex)
					msgstr = html[errindex+9:msgindex]
					print 'errmsg:',msgstr
				else:
					errorindex = html.find('error')
					errorendindex = html.find('",', errorindex)
					errorstr = html[errorindex + 8:errorendindex]
					print 'error:',errorstr
					if errorstr == 'need vcode':
						time.sleep(60)
				response.close()
			except Exception as e:
				print 'exception in Login:',str(e)
			time.sleep(41)
		
	
if __name__=='__main__':
	gb = getallbars.GetAllBars()
	bars = gb.FindAllBars()
	lc = TieBaLoginCls(bars)
	lc.Login()