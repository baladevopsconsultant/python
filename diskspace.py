#! /bin/python
import subprocess
threshold=0
child=subprocess.Popen(['df','-h'],stdout=subprocess.PIPE)
output = child.communicate()[0].strip().split("\n")
for x in output[1:]:
    if int(x.split()[-2][:-1]) == 0:
       print x
