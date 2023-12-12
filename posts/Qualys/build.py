import os
import re
import sys


def add_header(filename):
    with open(os.path.join(root, os.path.basename(filename)), 'r', encoding='utf-8') as f:
        content = f.read()

    # 获取文件名
    filename = os.path.basename(filename)

    # 创建头部
    header = """
+++
title = '{title}'
date = '2023-12-12T16:08:29+08:00'
categories= ["Qualys"]
tags = ["Qualys"]
+++
""".format(title=filename[:-3])

    # 将头部添加到内容中
    content = header + content

    # 将内容写入文件
    with open(os.path.join(root, os.path.basename(filename)), 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    # 获取目录中的所有 MD 文件，包括子目录
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.md'):
                add_header(os.path.join(root, file))
