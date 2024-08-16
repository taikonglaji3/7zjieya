from py7zr import SevenZipFile
import os
paths=input('路径：')
password='acgfun.net'
mulu=input('解压目录:')
path_list=paths.replace('""','","').replace('\\','/').split(',')
number_list=[i for i in range(len(path_list))]
path_dict={k:v for k,v in zip(path_list,number_list)}
for k,v in path_dict.items():
    path=k.replace('"','')
    extract=mulu+str(v)
    with SevenZipFile(path,password=password) as archive:
            archive.extractall(path=extract)



