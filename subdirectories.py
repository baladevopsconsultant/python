#! /bin/python
import os
from functools import partial
def makefolders(dest,subfolders):
    concat_path=partial(os.path.join,dest)
    makedirs=partial(os.makedirs)
    for path in map(concat_path,subfolders):
        makedirs(path)
        filecreationpath=os.path.join(path,'testfile')
        with open(filecreationpath,'w') as data:
            data.write("New file added under subfolder \n")

if __name__ == "__main__":
    dest='/home/kbalasubramani/python'
    subfolders=('Numbers/Folder_1/', 'Letters/Folder_2/', 'Letters/Folder_3/')
    makefolders(dest,subfolders)
    
