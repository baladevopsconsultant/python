#! /usr/bin/python2.7
def fileadd(*argv):
    url = open("urlfile","r")
    urllist=[]
    for line in url:
        striping = line.strip()
        print (striping)
        urllist.append(striping)
    url.close()
    try:
        for i in range(*argv):
            a=str(i)
            b=i-1
            print (b)
            link=urllist[b]
            Lines=["<record>\n","<refid>ref-" + a +"<</refid>\n","<url>" + link + "</url>\n","</record>\n"]
            file1 = open("urlfile.txt","a+")
            file1.writelines(Lines)
            file1.close()
    except IndexError as error:
        print ("URL not matching the Range of Refid")
if __name__ == "__main__":
    import sys
    value=sys.argv[1]
    value=int(value)
    value= value + 1
    fileadd(1,value)
