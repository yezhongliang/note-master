# -*- coding: utf-8 -*-
"""
@Time    :2022/8/10 16:57
@version :Python3.7.4
@Software:pycharm2020.3.2.
"""

"""sort排序
sort是内置的方法，可以直接对列表进行排序,sort默认是升序排序，从小到大
当参数reverse=True的时候，是降序排序
用法：
    变量名.sort(func=None,key=None,reverse=False)
"""
list1 = [1,8,7,10,90,76]
list1.sort(reverse=True)
print(list1)

tuple2 = (1,3,4,56,7,100)
list3 = list(tuple2)
list3.sort()
print(list3)

"""sorted
用法：sorted(func=None,key=None,reverse=False)   #默认是升序，
当reverse=True时，是降序排序
用法：变量=sorted(变量名)

sort和sorted的区别：
    1.sorted不会改变原来的列表，而是返回一个新的已经排序好的列表，需要用变量来接收
    2.sorted可以用于任何一个可迭代的对象
"""
# list2 = [1,3,4,5,6,90,66,77]
# res = sorted(list2,reverse=True)
# print(res)

# tuple1 = (1,3,5,7,10,2,4,6,8)
# res1 = sorted(tuple1)
# print(res1)
