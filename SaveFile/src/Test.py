# coding=utf-8
import re
filename = u"O’Reilly Safari | ? < > *	®"
ascii_file =  filename.encode(encoding='ascii', errors='ignore')
print re.sub("[^\w\s]","",ascii_file)