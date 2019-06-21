#! /bin/python
def multifiles():
    items=["one","two","three"]
    content="This is my file %s\n"
    for item in items:
        with open("%s_file" % item,"w") as f:
             f.write(content % item)
if __name__ == "__main__":
    multifiles()


