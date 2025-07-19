# -*- coding: utf-8 -*-
"""
@Time    :2022/8/12 19:09
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""
"""
yaml文件介绍：
    yaml [ˈjæməl]: Yet Another Markup Language ：另一种标记语言。
    yaml 是专门用来写配置文件的语言，非常简洁和强大,之前用ini也能写配置文件，
    看了yaml后，发现这个更直观，更方便，有点类似于json格式。也是Python自动化中常见的一种数据驱动的方式。
yaml文件规则：
    1.区别大小写  --跟python一样
    2.使用缩进表示层级关系    --跟python一样
    3.缩进时不允许使用Tab键，只允许使用空格。
    4.缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
    5.#表示注释，从这个字符一直到行尾，都会被解析器忽略，这个和python的注释一样

Yaml文件数据结构
对象：键值对的集合，又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary），
    标识符为冒号“:” 
数组：一组按次序排列的值，又称为序列（sequence） / 列表（list） --》类似于python列表,
    标识符为 -
纯量（scalars）：单个的、不可再分的值。字符串、布尔值、整数、浮点数、Null、日期、时间
    纯量没有标识符
    字符串：在yaml文件里面编写的时候可以加引号，也可以不加引号
    布尔值：TURE/True/true   FALSE/False/false 都可以表示布尔值
    整数：1，2，3，4，5，6
    浮点数：1.11，2.22，3.33
    Null: ~
    日期：2023-08-08 格式yyy-MM-dd
    时间：2023-08-08 10:10:10 格式：yyy-MM-ddTHH:mm:ss，日期与时间用T连接
    
注意：yaml文件的键和值之间一定要多加一个空格，不然语法错误！
编辑YAML文件推荐插件：YAML
校验YAML文件是否有语法的网站：https://www.bejson.com/validators/yaml_editor/


学习的目标：
1.学会看懂YAML文件
2.学会编写YAML文件

面试题：什么是序列化和反序列化
序列化：把数据变成可存储的字节，输出到文件，就叫序列化（通俗：数据保存到文件）
反序列化：把yaml/json这些文件的字节转换成为数据，就叫反序列化（通俗：从文件读取数据）

"""

