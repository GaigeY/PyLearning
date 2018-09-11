# -*- coding: UTF-8 -*-

import subprocess

print u"【9-3】调用subprocess.Popen()函数运行dir命令，列出当前目录下的文件。"
p = subprocess.Popen("dir", shell=True)
p.wait()