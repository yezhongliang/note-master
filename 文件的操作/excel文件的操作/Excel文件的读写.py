# -*- coding: utf-8 -*-
"""
@Time    :2022/8/12 15:04
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""
python对excel操作的库有xlrd(excel+read),xlwt(excel+write),openpyxl，pandas
1.xlrd: 读取excel 文件，支持xls和xlsx格式
2.xlwt：写入excel文件，只支持xls格式，不支持xlsx
3.openpyxl：既可以读取可以写入excel文件，但是只支持xlsx格式的文档

xls：旧版excel，2003年及以前的版本
xlsx：新版excel，2007年及以后的版本

安装xlrd第三方库：pip install xlrd
    指定版本下载：pip install xlrd==版本号
安装xlwt第三方库：pip install xlwt
    指定版本下载：pip install xlwt==版本号
安装openpyxl第三方库：pip install openpyxl
    指定版本下载：pip install openpyxl==版本号
    
查看有哪些库以及版本：pip3 list、pip list，不要升级pip 升级以后有可能导致用不了
如果不指定说明下载哪个版本号，那就默认下载最新版本
卸载第三方包的命令：pip uninstall 包名

第三方库下载的两个方式：
1：通过dos窗口输入pip install 包名 进行下载即可
2：在pycharm里面进行下载
查看已经下载的第三方库的命令：pip list
"""

