#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import subprocess
import datetime

##wol.pyのPATH
_WOL_PY_PATH = '/home/xxxx/script/wol/wol.py'

argvs = sys.argv 
if (len(argvs)  != 2):   # 引数が足りない場合は、その旨を表示
	print 'Usage: # python %s machinename' % argvs[0]
	quit()

#マシン名とMACのペアを羅列
macdic = {
		'MACHINENAME1':'XX-XX-XX-XX-XX-XX',
		'MACHINENAME2':'XX-XX-XX-XX-XX-XX',
		}

macaddr= macdic[argvs[1]]

cmd = 'python ' + _WOL_PY_PATH + ' ' + macaddr
print '[' + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + '] ' +  cmd
subprocess.call(cmd, shell=True)

