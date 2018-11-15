#! /usr/bin/python
# -*- coding:utf-8 -*-
#执行脚本的格式为：python test.py -p packagename -v 执行次数
#执行次数后面接需要执行的事件和百分比，如30%上滑事件：python test.py -p packagename -v 执行次数 --up 30
#具体操作事件可选项，可使用-help或--help获取，python test.py -h/--help
#没有设置百分比的事件会平均剩下的百分比去随机执行，不需要某个事件被执行则把百分比设置为0，百分比之和为100
import sys
import math
import time
import random
import getopt
import wda

def usage():
    print(
          """
              Usage:sys.args[0] [option]
              -h or --help：显示帮助信息
              --up ：上滑动操作，选项后接0-100之间的数，为该事件执行的百分比，百分比之和不超过100   例如：--up 20
              --dn ：下滑动操作
              --lt ：左滑动操作
              --rt ：右滑动操作
              --rp ：右上滑动操作
              --ph ：捏操作
              --st ：随机点击操作
              """
          )
    sys.exit()

try:
    options, args = getopt.getopt(sys.argv[1:], "hp:v:", ["help","up=","dn=","lt=","rt=","rp=","ph=","st="])
except getopt.GetoptError:
    print 'Oops we have some error!Please input -h or --help to get help.'
    sys.exit()
print(options)
temp = {}
pg = ""
vl = ""
for name, value in options:
    if name in ("-h", "--help"):
        usage()
    elif name in "-p":
        pg = value
    elif name in "-v":
        vl = value
    else:
        temp[name] = value
print(temp)
bundleid = pg
gesture_num = int(vl)
#与手机上的WebDriveAgent客户端链接
driver = wda.Client('http://localhost:8100')
# 启动应用，建立会话
session = driver.session(bundleid)
# 取得屏幕大小
height = session.window_size().height
width = session.window_size().width
print('宽和高：%s %s' %(width,height))

def up():
    session.swipe(200, 600, 200, 300, 0.5)
def down():
    session.swipe(100, 300, 100, 600, 0.5)
def left():
    swipe_width = width*random.random()
    if swipe_width < 200:
        swipe_width = 200
    swipe_height = height*random.random()
    if swipe_height < 100:
        swipe_height = 100
    session.swipe(swipe_width, swipe_height, swipe_width-200, swipe_height, 0.5)
def right():
    swipe_width = width*random.random()
    if swipe_width < 200:
        swipe_width = 200
    swipe_height = height*random.random()
    if swipe_height < 100:
        swipe_height = 100
    session.swipe(swipe_width, swipe_height, swipe_width-200, swipe_height, 0.5)
def right_up():
    session.swipe(200, 650, 300, 550, 0.5)
def pinch():
    session(className="",name="").pinch(4,1)
def shufft():
    session.tap(width*random.random(),height*random.random())

def getfun(fun):
    if fun == "--up":
        return up()
    elif fun == "--dn":
        return down()
    elif fun == "--lt":
        return left()
    elif fun == "--rt":
        return right()
    elif fun == "--rp":
        return right_up()
    elif fun == "--ph":
        return pinch()
    elif fun == "--st":
        return shufft()


total = 0
for i in temp.values():
    total= total + int(i)

default = (100-total)/(7-len(temp))
fun_list=["--up","--dn","--lt","--rt","--rp","--ph","--st"]
for i in fun_list:
    if i not in temp.keys():
        temp[i] = default
print(temp.items())

while gesture_num>0:
    gesture_num = gesture_num - 1
    num = math.floor(random.random()*101)
    print("num:",num)
    curr_sum = 0
    #result = 0
    for k in temp.keys():
        try:
            curr_sum = curr_sum + int(temp.get(k))
            #print("curr_sum:",curr_sum)
            if num<=curr_sum and num != 0:
                getfun(k)
                print(k)
                #reult = curr_sum
                break
        except Exception,e:
            print("\033[5;31m 报错信息：\033[0m"+str(e))
            if "status=889" in str(e):
                session = driver.session(bundleid)
                time.sleep(10)
            else:
                break


#-u 50 -d 20 -c 10
#"-u","-d","-l","-r","-g","-p","-s"
