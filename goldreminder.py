#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, urllib2, threading, os

resp = urllib2.urlopen('https://goldetfprod.alipay.com/gold/queryChart.htm?productCode=000930')

respread = resp.read();

pattern = re.compile(r'\[{"fundGoldPrice":\d+\.\d+');
match = pattern.search(respread);

if match:
	s = match.group()
	p = re.compile(r'\d+\.\d+');
	res = p.search(s);

	if res:
		gold = float(res.group())
		
		if gold > 249.1 or gold < 223.2:
			file = open('gold.txt', 'w')
			file.write(str(gold)+'\n黄金价格提醒注意')

			os.system('open -a Sublime\ Text\ 2 gold.txt')

			pass