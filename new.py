#coding=utf-8
import os
import string
import jieba
import sys
reload(sys)
sys.setdefaultencoding('utf-8')                                                  #将自身重载为utf-8编码

def tokenize (filename):                                                         #定义分词用函数
    fn = open(r'G:\pangu\english_stopword.dat')
    stopwords = {}.fromkeys([line.rstrip() for line in fn])                      #载入停止词
    print filename
    openfile=open(filename)
    of=openfile.read()
    segs = jieba.cut(of)                                                         #开始分词<
    final = ''
    for seg in segs:
        if seg not in stopwords:
            final += seg                                                         #>分词结束
    final=final.replace('\n',' ')                                                #将词语规则化
    final=' '.join(final.split())
    print("".join(final))
    newfile=open(r'G:\temp\NEWtext.dat','a')
    newfile.write(final)
    newfile.write("\n")
    newfile.close()
    fn.close()

info=os.getcwd()                                                                 #获得当前路径并处理
listfile=os.listdir(os.getcwd())
listfile=os.listdir(info)
for line in listfile:
    if line[-3:]==".py":                                                         #跳过自身
        continue  
    tokenize(line)
    print ("\n")                                                                 #规则化输出文件