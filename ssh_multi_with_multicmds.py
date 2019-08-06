import paramiko
username='<username>'
password='xxxx'
port=22
cmd="echo ==========networkconfiguration============ \n cat /etc/sysconfig/network-scripts/ifcfg-eth0 \n echo =====DNS===== \n cat /etc/resolv.conf"
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
        resp=''.join(outlines)
        print(resp)
if __name__ == '__main__':
    multissh()
