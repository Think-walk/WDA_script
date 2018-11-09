#! /usr/bin/python
# -*- coding:utf-8 -*-  

import sys
import atx
import time
from atx.ext.report import Report

def monkey_atx():
    try:
        #截图
        image = driver.screenshot()
        image.save('screen.png')
        
        #滑动首页banner图
        driver.swipe(200,500,800,500,0.1)   #iphone x的尺寸
        driver.swipe(200,500,800,500,0.1)
        #滚动界面使元素可见,并点击
        #driver(className="StaticText",name="Music Genres").scroll()
        #driver(className="StaticText",name="Music Genres").tap()
        time.sleep(2)
        
        #根据元素属性定位
        #elem=driver(className="Image",name="browse_topsongs_normal") #根据元素属性定位,网络教程"Class_name"的写法是错误的
        #elem.swipe("right")    #元素对象操作的方法swipe()貌似不能用了，抛异常'Element' object has no attribute 'swipe'
        #elem.tap()  #元素对象的点击
        #elem2=driver(className="CollectionView")
        #elem2.scroll()  #滚动使元素可见
        #elem2.click()
        
        print('寻找ui元素“更多”...')
        driver(text=u'更多').click()
        time.sleep(2)
        #print(driver(text=u'取消').exists)   #判断元素是否存在
        driver(text=u'想聽的').click()
        time.sleep(3)
        ##click_exists()该方法表示元素存在就点击不存在就立即返回防止抛异常而被中断，还可以在括号内设置等待时间(timeout=5.0)
        driver(text=u'browse collect normal').click_exists()
        driver(text=u'ic list more@3x').click()
        driver(text=u'music_menu_addplaylist').click()
        driver(text=u'Collect').click()
        time.sleep(2)
        driver(text=u'back').click()
        driver(text=u'back').click()
    except Exception,e:
        print("\033[5;35m 错误信息：%s \033[0m" %str(e))


bundleid = sys.argv[1]
gesture_num = sys.argv[2]
#与手机进行连接
driver = atx.connect('http://localhost:8100')
#获取屏幕大小
dis = driver.display
print('宽是：%s 高是：%s' %(dis.width, dis.height))
#打印设备信息
print(driver.status())

# 启动应用
launcher = driver.start_app(bundleid)
print("launcher ok!")
time.sleep(10)
monkey_atx()
print('关闭app...')
driver.stop_app()
#生成测试报告
print('正在生成测试报告...')
rp = Report(driver)
rp.patch_wda()
