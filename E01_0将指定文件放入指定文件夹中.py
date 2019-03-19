""" 
    作者：李海兵
    作用：
        将符合条件的文件放入指定文件夹中
    版本：E01_0
    修订日期
        2019-03-19
    使用模块：
        1.OS
        2.
"""
import os
import shutil
import re
import datetime

def get_filename(file_type,old_path):
    # file_name =[]
    final_name_list = []
    source_dir = old_path #读取当前路径,改为old_path
    for root,dirs,files in os.walk(source_dir):  
        for f in files :  
            if  file_type in f:  
                final_name_list.append(f)
    return final_name_list #返回由文件名组成的列表

#在桌面写入文件
def write_file(file_list,filename,new_path):
	filename_time = datetime.datetime.today()
    filePath = os.path.join(new_path,fileName)
    for file_name in file_list:
        with open(filePath,"w") as f:
            f.write(file_name + "\n")
        f.close()

def main_function(file_type,filename,new_path,old_path):
    file_list = get_filename(file_type,old_path)
    write_file(file_list,filename,new_path)
    

old_path=r'E:\Mr.Li\Downloads\未整理'  #需要分析的文件夹
new_path=r'E:\Mr.Li\Desktop'    #列表存放位置
fileName='测试_.txt'
file_type='.pdf'
main_function(file_type,fileName,new_path,old_path)
