#! /bin/python
import os
output=[]
for line in open('list'):
    f=line.rstrip('\n').split(' ')
    print f
    jsonout={}
    jsonout[f[4]] = f[5]
    output.append(jsonout)
print output
for i in output:
    print i['user']
