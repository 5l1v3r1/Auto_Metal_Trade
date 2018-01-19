#!/usr/bin/env.python
# _*_ coding:utf-8 _*_

import os
import time

###买入a手白银
def buy_silver(a):
    # 创建交易
    os.system("adb shell input tap 1000 142")
    time.sleep(0.1)

    # 选择交易品种
    os.system("adb shell input tap 1000 142")
    time.sleep(0.1)

    #选择白银
    os.system("adb shell input tap 959 440")
    time.sleep(0.1)

    #输入手数
    os.system("adb shell input tap 591 447")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input text {}".format(a)) #手数
    #买入
    time.sleep(0.1)
    os.system("adb shell input tap 803 1214")  #买入
    #退出到最初界面
    time.sleep(0.1)
    os.system("adb shell input tap 530 1890")

###卖出a手白银
def sell_silver(a):
    # 创建交易
    os.system("adb shell input tap 1000 142")
    time.sleep(0.1)

    # 选择交易品种
    os.system("adb shell input tap 1000 142")
    time.sleep(0.1)

    #选择白银
    os.system("adb shell input tap 959 440")
    time.sleep(0.1)

    #输入手数
    os.system("adb shell input tap 591 447")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input text {}".format(a)) #手数
    #买入
    time.sleep(0.1)
    os.system("adb shell input tap 261 1214")  #卖出
    #退出到最初界面
    time.sleep(0.1)
    os.system("adb shell input tap 530 1890")

###买入a手黄金
def buy_gold(a):
    # 创建交易
    os.system("adb shell input tap 1000 142")
    time.sleep(0.1)

    # 选择交易品种
    os.system("adb shell input tap 1000 142")
    time.sleep(0.1)

    #选择黄金
    os.system("adb shell input tap 966 293")
    time.sleep(0.1)

    #输入手数
    os.system("adb shell input tap 591 447")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input text {}".format(a)) #手数
    #买入
    time.sleep(0.1)
    os.system("adb shell input tap 803 1214")  #买入
    #退出到最初界面
    time.sleep(0.1)
    os.system("adb shell input tap 530 1890")

###卖出a手黄金
def sell_gold(a):
    # 创建交易
    os.system("adb shell input tap 1000 142")
    time.sleep(0.1)

    # 选择交易品种
    os.system("adb shell input tap 1000 142")
    time.sleep(0.1)

    #选择黄金
    os.system("adb shell input tap 966 293")
    time.sleep(0.1)

    #输入手数
    os.system("adb shell input tap 591 447")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input tap 947 1687")
    time.sleep(0.1)
    os.system("adb shell input text {}".format(a)) #手数
    #买入
    time.sleep(0.1)
    os.system("adb shell input tap 261 1214")  #卖出
    #退出到最初界面
    time.sleep(0.1)
    os.system("adb shell input tap 530 1890")
















