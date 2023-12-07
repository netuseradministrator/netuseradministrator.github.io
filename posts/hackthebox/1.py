import os
import re

def add_header(filename):
    with open(filename, 'r',encoding='utf-8') as f:
        content = f.read()

    # 获取文件名
    filename = os.path.basename(filename)

    # 创建头部
    header = """
+++
title = '{title}'
date = '2023-12-07T16:08:29+08:00'
draft = true
+++
""".format(title=filename[:-3])

    # 将头部添加到内容中
    content = header + content

    # 将内容写入文件
    with open(filename, 'w',encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    # 获取目录中的所有 MD 文件
    filenames = os.listdir('.')
    for filename in filenames:
        if filename.endswith('.md'):
            add_header(filename)
