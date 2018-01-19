#!/usr/bin/env.python
#_*_ coding: utf-8 _*_

from selenium import webdriver
import os
import time
import Trade


#获取当前时间
def gettime():
    a = time.localtime()
    year = int(a[0])
    month = int(a[1])
    day = int(a[2])
    hour = int(a[3])
    minute = int(a[4])
    sec = int(a[5])
    now = "%04d-%02d-%02d %02d:%02d:%02d"%(year,month,day,hour,minute,sec)
    return(now)

#主函数
def main():
    time.sleep(5)  #防止异常快速迭代达到最大迭代深度
    browser = webdriver.Chrome()    #选择浏览器
    try:
        #配置相应的数据源
        browser.get("http://www.igoldhk.com")    #加载页面
        #获取初始6个数值，每隔十秒获取一个
        goldPrice_solve = []
        silverPrice_solve = []
        for i in range(6):
            time.sleep(10)  # 每5s获取一个数据
            # 通过网页开发者模式可以找到对应标签的id，class等信息
            result = browser.find_element_by_id("new_price")
            # 将结果转化为浮点数
            price = result.text
            goldPrice = price[7] + price[8] + price[9] + price[10] + price[11] + price[12] + price[13]
            goldPrice = float(goldPrice)
            goldPrice_solve.append(goldPrice)
            silverPrice = price[44] + price[45] + price[46] + price[47] + price[48]
            silverPrice = float(silverPrice)
            silverPrice_solve.append(silverPrice)
            print(gettime(),silverPrice,goldPrice)
            #将历史价格写入文件
            t = gettime()
            fgold = open('F:/gold_history_data.txt', 'a')
            fsilver = open('F:/silver_history_data.txt', 'a')
            fgold.write('%s  %4.2f\n'%(t,goldPrice))
            fsilver.write('%s  %2.2f\n'%(t,silverPrice))
            fgold.close()
            fsilver.close()
        if (goldPrice_solve[0] == goldPrice_solve[1] == goldPrice_solve[2] == goldPrice_solve[3] == goldPrice_solve[4]):
            with open('F:/gold_history_data.txt', 'a') as fgold:
                fgold.write("网页出错，以上六组数据错误。")
            with open('F:/silver_history_data.txt', 'a') as fsilver:
                fsilver.write("网页出错，以上六组数据错误。")

            main()
        while True:
            #判断条件，当满足时执行相应操作
            if (0.15 < silverPrice_solve[4] - silverPrice_solve[5] < 1
                 or 0.15 < silverPrice_solve[3] - silverPrice_solve[5] < 1
                 or 0.15 < silverPrice_solve[2] - silverPrice_solve[5] < 1
                 or 0.15 < silverPrice_solve[1] - silverPrice_solve[5] < 1
                 or 0.15 < silverPrice_solve[0] - silverPrice_solve[5] < 1):
                #空一段位置执行操作
                a = 0.10
                Trade.buy_silver(a)
                Trade.sell_gold(a)
                with open ('F:/TraderRecord','a') as bs:
                    bs.write("%s 买入白银：%f手  卖出黄金：%f手"%(gettime(),a,a))
                main()                     #返回到主函数重新执行，防止短时间内再次交易
                #空一段位置执行操作
            elif (10 < goldPrice_solve[4] - goldPrice_solve[5] < 100
                 or 10 < goldPrice_solve[3] - goldPrice_solve[5] < 100
                 or 10 < goldPrice_solve[2] - goldPrice_solve[5] < 100
                 or 10 < goldPrice_solve[1] - goldPrice_solve[5] < 100
                 or 10 < goldPrice_solve[0] - goldPrice_solve[5] < 100):
                #空一段位置执行操作
                a = 0.10
                Trade.buy_gold(a)
                Trade.sell_silver(a)
                with open ('F:/TraderRecord','a') as bs:
                    bs.write("%s 卖出白银：%f手  买入黄金：%f手"%(gettime(),a,a))
                main()                     #返回主函数重新执行，防止短时间内再次交易
                #空一段位置执行操作

            time.sleep(10)  # 每5s获取一个数据
            # 通过网页开发者模式可以找到对应标签的id，class等信息
            result = browser.find_element_by_id("new_price")
            # 将结果转化为浮点数
            price = result.text
            goldPrice = price[7] + price[8] + price[9] + price[10] + price[11] + price[12] + price[13]
            goldPrice = float(goldPrice)
            silverPrice = price[44] + price[45] + price[46] + price[47] + price[48]
            silverPrice = float(silverPrice)
            print(gettime(),silverPrice,goldPrice)
            #将历史价格写入文件
            t = gettime()
            fgold = open('F:/gold_history_data.txt', 'a')
            fsilver = open('F:/silver_history_data.txt', 'a')
            fgold.write('%s  %4.2f\n'%(t,goldPrice))
            fsilver.write('%s  %2.2f\n'%(t,silverPrice))
            fgold.close()
            fsilver.close()
            # 对数据列表更新
            goldPrice_solve.pop(0)
            goldPrice_solve.append(goldPrice)
            silverPrice_solve.pop(0)
            silverPrice_solve.append(silverPrice)
    except Exception as e:
        with open('D:/logfile.txt','a') as logfile:
            logfile.write("{},{}".format(gettime(),e))
        browser.quit()
        main()

#执行程序
main()
