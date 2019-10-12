# -*- coding: UTF8 -*-

'''
递归解除重命名当前文件夹下的所有文件，删除后缀，后缀为suffix变量
'''

import os;

path = "." #文件夹目录
suffix = '_'
def eachFile(filepath):
    fileNames = os.listdir(filepath)  # 获取当前路径下的文件名，返回List
    for file in fileNames:
        oldDir = filepath + '/' + file # 将文件名加入到当前文件路径后面
        # print(oldDir)
        # if os.path.isdir(oldDir): # 如果是文件夹
        if os.path.isfile(oldDir):  # 如果是文件
            if oldDir[-1] == suffix:   # 是否有后缀
                os.rename(oldDir,oldDir[:-1])#重命名
                print('Derenaming' + oldDir + '->' + oldDir[:-1])
        else:
            eachFile(oldDir)                #如果不是文件，递归这个文件夹的路径

if __name__ == "__main__":
    eachFile(path)



