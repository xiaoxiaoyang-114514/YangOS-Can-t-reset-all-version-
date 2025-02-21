import os
import shutil
def delete_single_file(file_path):
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"文件 {file_path} 不存在。")
        return
    
    # 检查是否为文件
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"已删除文件: {file_path}")
    else:
        print(f"警告: {file_path} 不是一个文件。")



def delete_directory(directory_path):
    # 检查目录是否存在
    if not os.path.exists(directory_path):
        print(f"目录 {directory_path} 不存在。")
        return
    
    # 删除目录及其内容
    shutil.rmtree(directory_path)
    print(f"已删除目录: {directory_path}")

def delete_files_in_directory(directory_path):
    # 检查目录是否存在
    if not os.path.exists(directory_path):
        print(f"目录 {directory_path} 不存在。")
        return
    
    try:
        # 删除目录中的所有文件
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"删除文件 {file_path} 时出错: {e}")
        print(f"已删除目录 {directory_path} 中的所有文件。")
    except Exception as e:
        print(f"删除目录中的文件时出错: {e}")