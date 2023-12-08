import os

def delete_lines_in_md_files(directory='.'):
    # 遍历指定目录及其子目录中的所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)

                # 逐行读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()

                # 删除第1至第14行
                modified_lines = lines[7:]

                # 将修改后的内容写回文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(modified_lines)

if __name__ == "__main__":
    # 删除当前目录及其子目录中所有MD文件的第1至第14行
    delete_lines_in_md_files()
