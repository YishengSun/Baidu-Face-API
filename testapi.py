# -*- coding: utf-8 -*- 
from aip import AipFace
import datetime
# encoding:utf-8
import base64
import urllib
import ssl
import os
import time



APP_ID = '10859201'
API_KEY = 'vC9RSPvbHwjfddlsOvSQfd1F'
SECRET_KEY = 'kOZ3hS9cqDa63GIG7kRKWZBxhvsnWnQd'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


##获取访问的token
def getAccessToken():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+API_KEY+'&client_secret='+SECRET_KEY
    request = urllib.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.urlopen(request)
    content = response.read()
    if (content):
        print(content)
    return content


# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

 # 调用人脸属性检测接口
def faceDetecting(picName,options=""):
    begin = datetime.datetime.now()
    result = ""
    # 调用人脸属性识别接口
    if options =="":
        result = client.detect(get_file_content(picName))
    else:
        result = client.detect(get_file_content(picName), options)
    print(result)
    end = datetime.datetime.now()
    print("processs is end with process duration time is: "+str(end-begin))

#注册人脸用于识别人的脸
def registerFaceForUser(uid,userInfo,groupId,picPath):
    info= client.addUser(
        uid,
        userInfo,
        groupId,
        get_file_content(picPath)
    )
    return(str(info))

registerFaceForUser("huge","huge is a supper star!","babu","huge/sss.jpg")
"""
registerFaceForUser("hege","hege is a supper star!","babu","huge/huge-2.jpg")
registerFaceForUser("hege","hege is a supper star!","babu","huge/huge-3.jpg")
registerFaceForUser("hege","hege is a supper star!","babu","huge/huge-4.jpg")
registerFaceForUser("hege","hege is a supper star!","babu","huge/huge-5.jpg")
registerFaceForUser("hege","hege is a supper star!","babu","huge/huge-6.jpg")
registerFaceForUser("hege","hege is a supper star!","babu","huge/huge-7.jpg")
registerFaceForUser("hege","hege is a supper star!","babu","huge/huge-8.jpg")
registerFaceForUser("hege","hege is a supper star!","babu","huge/huge-9.jpg")
registerFaceForUser("hege","hege is a supper star!","babu","huge/huge-10.jpg")

registerFaceForUser("yangyang","hege is a supper star!","babu","yangyang/yang-1.jpg")
registerFaceForUser("yangyang","hege is a supper star!","babu","yangyang/yang-2.jpg")
registerFaceForUser("yangyang","hege is a supper star!","babu","yangyang/yang-3.jpg")
registerFaceForUser("yangyang","hege is a supper star!","babu","yangyang/yang-4.jpg")
registerFaceForUser("yangyang","hege is a supper star!","babu","yangyang/yang-5.jpg")
registerFaceForUser("yangyang","hege is a supper star!","babu","yangyang/yang-6.jpg")
"""



##检测人脸是否是授权的人物
def recognizeFaceForOne(groupId,picPath):
    options = {
        'user_top_num': 1,
        'face_top_num': 1,
    }
    info = client.identifyUser(
        groupId,
        get_file_content(picPath),
        options
    )
    return info['result'][0]['scores'][0]

def GetFileList(dir, fileList):
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gb2312'))
    elif os.path.isdir(dir):  
        for s in os.listdir(dir):
            #如果需要忽略某些文件夹，使用以下代码
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)  
    return fileList

list = GetFileList('C:\\Users\\SYS\\Desktop\\baiduApi\\myface', [])
list1=[]
list2=[]
for x in list:
        list1.append(x.split('\\')[-1].split('.')[0])
        list2.append(x.split('\\')[-1])
        
"""
recognizeFaceForOne("babu","myface/sun.jpg")

print(str(datetime.datetime.now()))

print(str(datetime.datetime.now()))
"""

score=[]
for y in list2:
    score.append(recognizeFaceForOne("babu","myface/"+y))
num = score.index(max(score))

if max(score)>75:
    print u"欢迎你  "+list1[num]+"!"
else:
    file = open('C:\\wamp\\www\\kunfan\\w1.txt','w')
    file.write(u"您不是本公司员工!")
    file.close()   



