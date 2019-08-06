import paramiko
import csv
from getpass import getpass
username='<username>'
password=getpass()
port=22
cmd="cat /etc/sysconfig/network-scripts/ifcfg-eth0|grep IPADDR \n cat /etc/resolv.conf | grep <ipaddr>"
#cmd="cat /etc/sysconfig/network-scripts/ifcfg-eth0 \n cat /etc/resolv.conf | grep 10.16.126.1"
#cmd="cat /etc/sysconfig/network-scripts/ifcfg-eth0 \n cat /etc/resolv.conf"
with open('config_ouput.csv','w+') as config:
    fieldnames = ['networkconfiguration', 'DNS']
    wr = csv.writer(config,quoting=csv.QUOTE_ALL)
    wr.writerow(fieldnames)


def multissh():
    with open("hostslist","r") as host:
        line=host.read().splitlines()
        print(line)
    for host in line:
        print(host)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host,port,username,password)
        stdin,stdout,stderr=ssh.exec_command(cmd)
        outlines=stdout.readlines()
#        outlines=stdout.read()
#        print(outlines)
        stripped_line = [s.rstrip() for s in outlines]
        print(stripped_line)
#        output = [elem.strip('\n').split(',') for elem in outlines]
#        print(output)
#        clean_output=[i.strip("\n").split(",") for i in outlines[1:]]
#        clean_output=outlines.strip("\n").split(",")
#        outlines=stdout.read()
#        print(clean_output)
#        resp=''.join(outlines)
#        print(stripped_line)
#        print(resp)
#        with open('config_ouput.csv','a+') as config:
#            fieldnames = ['networkconfiguration', 'DNS']
#            wr = csv.writer(config,quoting=csv.QUOTE_ALL)
#           wr = csv.DictWriter(config,quoting=csv.QUOTE_ALL)
#            wr.writeheader()
#            wr.writerow(fieldnames)
#            wr.writerow(clean_output)
#            cmd_result=[]
#            for element in outlines:
#                cmd_result(element.strip('\n').split(','))
#            cmd_result.append(resp)
#            cmd_result.append(clean_output)
#            print(cmd_result)
#            wr.writerow(stripped_line)
        with open('config_ouput.csv','a+') as config:
            wr = csv.writer(config,quoting=csv.QUOTE_ALL)
            wr.writerow(stripped_line)
#            wr.writerow(cmd_result)
if __name__ == '__main__':
    multissh()
