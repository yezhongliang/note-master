# -*- coding: utf-8 -*-
"""
@Time    :2022/8/18 23:35
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
from time import sleep

"""
为什么要学习元素定位方式
1.让程序操作指定元素，就必须要先找到此元素
2.找到元素后才能进行操作（填写，清除，选择等等等等）

webDriver提供了8种定位元素的方式：
属性定位：
    id  id是唯一的。
    name   
    class name 不唯一，也有可能重复
    tag name  标签名，重复的几率超级大

超链接定位： 标签名需要是a标签
    link text 
    partial link text
    
路径定位：
    xpath
    css seletor

分为四类：
id、name、class_name、tag name：根据元素的标签或元素的属性进行定位
link_text、partial_link_text:根据超链接的文本来进行定位
    link_text:全匹配
    partial_link_text：模糊匹配
    
xpath：根据路径定位--万能定位方式
css：根据css选择器定位（样式定位）--万能定位方式

有id用id，没id用clas或者name，都没有的话就用xpath和css
速度：最快的是id，然后就是css，xpath最慢

在公司里面，能把这个元素定位到就可以了，不管你用什么方法
"""

"""id定位方式，用的方法是find_element('定位方式','定位方式对应的值')
"""

#
# #任务：打开百度，窗口最大化，输入“疯狂星期四”，点击搜索

