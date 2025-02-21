import os

def find():
    global directory
    # 遍历目录树
    for root, dirs, files in os.walk(directory):
        # 遍历当前目录下的所有文件
        for file in files:
            # 构建文件的完整路径
            file_path = os.path.join(root, file)
            fliepath = file_path.replace(directory,'')
            print(f'File: {fliepath}')
        # 遍历当前目录下的所有子目录
        for dir in dirs:
            # 构建子目录的完整路径
            dir_path = os.path.join(root, dir)
            folpath = dir_path.replace(directory,'')
            print(f'Directory: {folpath}')

def write(path,text):
    file = open(path,'w')
    file.write(str(text))
    file.close()

def get_text(path):
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "文件不存在"
    except IOError:
        return "读取文件时出错"
    

# 指定目录
directory = os.path.dirname(os.path.abspath(__file__))

