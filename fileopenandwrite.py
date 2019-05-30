#! /bin/python
def filewrite():
    f=open("test.txt","w+")
    

    for i in range(10):
        f.write("This is line %d \r\n" % (i+1))
    f.close()

#filewrite()
if __name__ == "__main__":
   filewrite()

