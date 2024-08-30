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
    baolujing=Label(j7z,text='压缩包路径文本txt：')
    shurubao=Entry(j7z)
    queren=Button(j7z,text='开始解压',command=queren7z)
    jielujing=Label(j7z,text='解压至目录：')
    shurujie=Entry(j7z)
    password=Label(j7z,text='密码：')
    shurumi=Entry(j7z)
    baolujing.pack()
    shurubao.pack()
    jielujing.pack()
    shurujie.pack()
    password.pack()
    shurumi.pack()
    queren.pack()
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
        with SevenZipFile(path,password=shurumi.get()) as archive:
            archive.extractall(path=extract)


jieya=Tk()
jieya.geometry('300x120')
jieya.title('解压方式')
label=Label(jieya,text='请选择解压方式')
label.pack()
jieya7z=Button(jieya,text='7z解压',command=jy7z)
jieyazip=Button(jieya,text='zip解压')
jieyarar=Button(jieya,text='rar解压')
jieya7z.pack(fill=X,expand=True)
jieyazip.pack(fill=X,expand=True)
jieyarar.pack(fill=X,expand=True)
jieya.mainloop()
