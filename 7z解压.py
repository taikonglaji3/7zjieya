from py7zr import SevenZipFile
from tkinter import Tk,Entry,Button,Label,LEFT,RIGHT,X,Y,BOTTOM,TOP

def jy7z():
    global shurubao
    global shurujie
    global shurumi
    jieya.destroy()
    j7z=Tk()
    j7z.geometry('300x180')
    j7z.title('7z解压')
    baolujing,jielujing,password=Label(j7z,text='压缩包路径文本txt：'),Label(j7z,text='解压至目录：'),Label(j7z,text='密码：')
    shurubao,shurujie,shurumi=Entry(j7z),Entry(j7z),Entry(j7z)
    queren=Button(j7z,text='开始解压',command=queren7z)

    sign1=[baolujing,shurubao,jielujing,shurujie,password,shurumi,queren]
    for i in sign1:
        i.pack()
    j7z.mainloop()

def queren7z():
    txt = open(shurubao.get().replace('"',''), 'r', encoding='utf-8')
    path_list = txt.read().replace('"', '').split('\n')
    number_list = [i for i in range(len(path_list))]
    path_dict = {k: v for k, v in zip(path_list, number_list)}
    mulu = shurujie.get().replace('"','')
    for k, v in path_dict.items():
        path = k.replace('"', '')
        extract = mulu + str(v)
        if path[-3,-1]=='.7z':
            with SevenZipFile(path,password=shurumi.get()) as archive:
                archive.extractall(path=extract)
        if path[-7,-1]=='.7z.001':
            with

jieya=Tk()
jieya.geometry('300x120')
jieya.title('解压方式')
label=Label(jieya,text='请选择解压方式')
label.pack()
jieya7z,jieyazip,jieyarar=Button(jieya,text='7z解压',command=jy7z),Button(jieya,text='zip解压'),Button(jieya,text='rar解压')

jieya7z.pack(fill=X,expand=True)
jieyazip.pack(fill=X,expand=True)
jieyarar.pack(fill=X,expand=True)
jieya.mainloop()
