#! /bin/python
def multidirectories():
    from os import makedirs
    dirstruct='files/backup/'
    makedirs(dirstruct)
    
    with open(dirstruct + 'new_file', 'w') as data:
        data.write('The file is created under the directory')

if __name__ == "__main__":
    multidirectories()
