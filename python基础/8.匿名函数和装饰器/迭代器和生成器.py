
"""
迭代器：
    有__iter__和__next__,用的是return。
    特点：
        1、迭代器是访问集合元素的一种方式，迭代器对象从集合的第一个元素开始访问，直到所有的元素，被访问完结束。
        2、迭代器 只能往前 不会往后退
        3、取迭代器中的数据只能一个一个地取，而且取出来的数据在迭代器中就不存在了。
    常用方法：
        iter方法：它可以将字符串、列表、元组等容器变成迭代器
        next方法：用于对迭代器进行遍历
            说明：在对迭代器进行遍历时候，如果没有后续元素了，next()会抛出一个 StopIteration 异常。


生成器：本质上是一个迭代器
    有__next__，用的是yield
    使用了yield的含住被称为生成器，生成器是一个返回迭代器的函数，只能用于迭代操作。在调用生成器运行的过程中，
    每次遇到yield时函数会暂停并保存当球按所有的运行信息，返回yield的值，并在下一次执行next()方法时从当前位置继续运行。



python基本的数据类型有那些？
    1、number类型
        int、float、bool、复数
    2、字符串类型
    3、列表类型
    4、字典类型
    5、元组类型
    6、集合类型

序列（sequence）包含：list、str、tuple,所有序列都可以转换成迭代器





面试题：
1.迭代器和生成器的区别是什么？
2.如何编写迭代器 如何编写生成器

"""

# 迭代器总demo
# list_demo = [1,2,3,4,5,6,7]
# it = iter(list_demo)
# print(next(it))  #1
# print(next(it))  #2
# print(next(it))  #3
# print(next(it))  #4
# print(next(it))  #5
# print(next(it))  #6
# print(next(it))  #7
# print(it.__next__())  #也可以用于输出，内存的话呢是用完就会释放掉
# print(next(it))  #报错了 StopIteration  已经停止迭代了


#声明一些变量，用于测试
list1 = [1,2,3,4,5,6,7]
str1 = "abcde"
tuple1 = (1,2,3,4,5,6,7,8,9,10)


#列表转换成为迭代器
# it1 = iter(list1)
# for index,data in enumerate(it1):
#     print(f"当索引为{index}时",f"data为:{data}")

#字符串转换成迭代器
# it2 = iter(str1)
# print(it2)  #输出迭代器it2的内存地址  <str_iterator object at 0x000002645513EF40> 物理地址
# for i in enumerate(it2):
#     print(i)

#元组转换成迭代器
# it3 = iter(tuple1)
# print(it3)  #输出迭代器it3的内存地址   <tuple_iterator object at 0x000002A25378EF10> 物理地址
# for i in enumerate(it3):
#     print(i)



#生成器
arr2 = [11,22,33,44,2131,1236,654,99,888]
#推导式，只能用元组 不能用列表。用了列表会变成列表
arr3 = (i * 10 for i in arr2)
print(arr3)   #迭代器对象 <generator object <genexpr> at 0x00000224A31594A0>，所以说生成器本质上述是迭代器
print(arr3.__next__())  #110
print(arr3.__next__())  #220

def gengerator_even():
    for i in arr3:
        if i % 2 == 0:
            yield i  #相当于return的作用，但是return下面不执行，yield下面会执行
            print("*" * 10)

a = gengerator_even()
print(a)  #<generator object gengerator_even at 0x0000029353DFCD60>
print(a.__next__())
print(a.__next__())

a.close()  #关闭之后就不能用next了，再用的话就会报错了
print(a.__next__())




"""
描述
1、enumerate是Python的一个内置函数。
2、enumerate意为：枚举，列举
3、enumerate()
函数用于将一个(可迭代的对象)
可遍历的数据对象(
    如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标。也就是说，对于一个可迭代的（iterable） / 可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值。

使用场景
1、一般用在
for 循环当中，遍历或查找对象及其索引值（下标）。
2、Python
2.3.以上版本可用，2.6
添加
start
参数。

语法
enumerate()
方法的语法:
enumerate(sequence, [startindex = 0])

参数
sequence – 一个序列、迭代器或其他支持迭代对象。
start – 下标起始位置。索引值默认从0计算，可变。

返回值
返回
enumerate(枚举)
对象。
"""














