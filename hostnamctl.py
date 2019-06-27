#! /usr/local/bin/python3.7
def hostname():
    from subprocess import Popen,PIPE
    with open('hostname.txt','w') as f:
        output=Popen(["hostnamectl"],stdout=PIPE)
        response=output.stdout.read().decode('utf-8')
        print(response, file=f)
hostname()
