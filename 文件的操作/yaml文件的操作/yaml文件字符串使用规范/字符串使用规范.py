# -*- coding: utf-8 -*-
"""
@Time    :2023/1/14 11:39
@version :Python3.7.4
@Software:pycharm2020.3.2
"""
"""
1) 字符串默认不使用引号表示。
示例： username: lisi
转为Python字典： {'username': 'lisi'}

2) 如果字符串之中包含空格或特殊字符，需要放在引号之中。
虽然不放在引号里面也不会报错，但是为了规范，最好是放在引号里面
示例： username: 'hello python'
转为Python字典： {'username': 'hello python'}

3) 单引号和双引号都可以使用，但是单引号会对特殊字符转义，而双引号不会对特殊字符转义。
示例： username: 'Hello\nPython'
      nickname: "Hello\nPython"
转为Python字典： {'username': 'Hello\\nPython', 'nickname': "Hello\nPython"}

4) 单引号之中如果还有单引号，必须连续使用两个单引号转义。
示例： username： 'I''m jacky'
转为Python字典： {'username': 'I\'m jacky'}

5) 字符串可以写成多行，但从第二行开始，必须有一个单空格缩进。换行符会被自动转为空格。
示例：
    title: 人生苦短
      我用python
转为Python字典： {'title': '人生苦短 我用python'}
             
6）多行字符串可以使用|保留换行符，也可以使用>折叠换行。

示例：
    books: |
      天龙八部
      神雕侠侣
      笑傲江湖
    ---
    date: >
      yesterday
      today
      tomorrow
转为Python字典后：
{'books': '天龙八部\n神雕侠侣\n笑傲江湖\n'}
{'date': 'yesterday today tomorrow\n'}

7) +表示保留文字块末尾的换行，-表示删除字符串末尾的换行。
示例：
    username: |+
      abidal
      
    
    ---  
    username: |-
      karma
      
转为python字典后：
{'username': 'abidal\n\n'}
{'username': 'karma'}

8) 字符串之中也可以插入HTML标签
示例：
    content： 
      <p style="font: 14px;color: red">
       这是文章正文
      </p>
"""

import yaml
with open('yaml_string',mode='r') as file1:
    data = yaml.safe_load(file1)
    print(data)



