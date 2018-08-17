#coding=utf-8

import sys
if len(sys.argv) < 2:
    print u'请使用命令行参数'
    sys.exit(1)
for i in range(0, len(sys.argv)):
    print ""+ str(i+1)+": "+ sys.argv[i]