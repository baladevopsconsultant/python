#! /usr/bin/python2.7
def fileadd(*argv):
    for i in range(*argv):
        a=str(i)
        Lines=["<record>\n","<refid>ref-" + a +"<</refid>\n","<url>http://0.0.0.11/test-conv/res.1</url>\n","</record>\n"]
        file1 = open("urlfile.txt","a+")
        file1.writelines(Lines)
        file1.close()
if __name__ == "__main__":
    import sys
    value=sys.argv[1]
    value=int(value)
    value= value + 1
    fileadd(1,value)
