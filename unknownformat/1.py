import os


def safe_link(file):
    # 使用 urllib.parse.quote 将文件名转换为URL编码，处理特殊字符
    from urllib.parse import quote
    return quote(file)


def generate_index_md(directory):
    # 定义文件名
    index_file = os.path.join(directory, 'index.md')

    # 初始化Markdown字符串
    md_content = "# Index of Files\n\n"

    # 遍历目录下的所有文件
    for file in os.listdir(directory):
        # 忽略index.md本身和隐藏文件
        if file == 'index.md' or file.startswith('.'):
            continue

        # 为每个文件创建Markdown链接，使用safe_link处理文件名
        md_content += f"- [{file}]({safe_link(file)})\n"

    # 使用utf-8编码写入文件
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(md_content)


# 替换成你的目录路径
directory_path = '.'
generate_index_md(directory_path)
