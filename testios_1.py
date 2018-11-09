#! /usr/bin/python
# -*- coding:utf-8 -*-  
# filename : testios.py
# author: hyper
# createdate: 2017/02/22

import sys
import wda
import random
import math
import time


def gesture_1(code):
    try:
        global session
        print(code)
        #脚本所使用的坐标值并非基于屏幕像素，而是基于点，单位是pt；换算关系：一英寸=72pt(点)=96px(像素)
        #session.tap(353,height*random.random()) #注释掉其他事件代码，单独执行右边菜单键点击事件以验证坐标的准确性
        #简单写法：swipe_left()  swipe_right()   swipe_up()  swipe_down()    tap_hold(x,y,1.0)   double_tap(x,y)
        ##上滑动
        
        if code == 1:
            session.swipe(200, 700, 200, 500, 0.5)
        ##下滑动
        elif code == 3:
            session.swipe(100, 400, 100, 300, 0.5)
        ##右滑动
        #session.swipe_right()    
        elif code == 5:
            swipe_width = width*random.random()
            if swipe_width < 200:
                swipe_width = 200
            swipe_height = height*random.random()
            if swipe_height < 100:
                swipe_height = 100
            session.swipe(swipe_width-200, swipe_height, swipe_width, swipe_height, 0.5)
        ##左滑动
        elif code == 7:
            swipe_width = width*random.random()
            if swipe_width < 200:
                swipe_width = 200
            swipe_height = height*random.random()
            if swipe_height < 100:
                swipe_height = 100
            session.swipe(swipe_width, swipe_height, swipe_width-200, swipe_height, 0.5)

        #右上滑动
        elif code == 9:
            session.swipe(200, 650, 300, 550, 0.5)
        #增加右边菜单键点击率
        elif code == 11:
            session.tap(353,height*random.random())
        #捏
        elif code == 13:
            session(className="",name="").pinch(4,1)
        ##随机点击事件
        else:
            session.tap(width*random.random(),height*random.random())
    except Exception,e:
        print("\033[5;31m 报错信息：\033[0m"+str(e))
        print("\033[1;35m 重启应用... \033[0m")
        session = driver.session(bundleid)
        time.sleep(10)


if __name__ == '__main__':
    bundleid = sys.argv[1]
    gesture_num = sys.argv[2]
    #与手机上的WebDriveAgent客户端链接
    driver = wda.Client('http://localhost:8100')
    # 启动应用，建立会话
    session = driver.session(bundleid)
	# 取得屏幕大小
    height = session.window_size().height
    width = session.window_size().width
    print('宽和高：%s %s' %(width,height))
    #根据元素属性定位元素
    print(session(className="Image",name="browse_topsongs_normal").exists) #判断元素是否存在
    #session(className="Image",name="browse_topsongs_normal").swipe("left") #对元素滑动操作该方法已不可用
    #session(className="Image",name="browse_topsongs_normal").pinch(2,1) #捏
    #session(className="StaticText",name="Music Genres").scroll() #滚动使元素可见
    #session(text="browse_topsongs_normal").click()
    
    #session.tap(20,30)
	#session.swipe(300, 400, 300, 100, 1.0)
	#等待60s，用户进行初始化操作
    time.sleep(10)
    #driver.status()
    #driver.home()
    #driver.source()
    #driver.screenshot('screen.png')
    num = int(gesture_num)
    while num>0 :
        num = num -1
        code = math.floor(random.random()*14)
        gesture_1(code)
