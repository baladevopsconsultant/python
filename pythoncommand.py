#! /bin/python
import os
import subprocess
command='cat list | cut -d" " -f5,6 > output.txt'
os.system(command)
for i in open('output.txt'):
#    print type(i)
    f=i.rstrip('\n').split(' ')
#    print f
    dict1 = {}
    dict1[f[0]]=f[1]
    print dict1['user']
    
#result=run(command,shell=True,stdout=PIPE,universal_newlines=True)
#print(result.stdout)
