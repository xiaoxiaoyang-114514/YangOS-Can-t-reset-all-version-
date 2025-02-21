import sys
import os
import datetime
import time
from start import start
from gwt import find, write, get_text
from get_os import get_os
from delf import delete_single_file, delete_directory, delete_files_in_directory
from logwrite import write_new_log

directory = os.path.dirname(os.path.abspath(__file__))
logpath = directory + '/etc/lastlog.txt'
write(logpath,'')
write_new_log('power on.','OS')

file = open('usrpwd.txt','r')
pwd = file.read()
file.close()

def login():
    ent = input('user:')
    if ent == 'root':
        ent = input('password: ')
        if not ent == pwd:
            print('passwrod is wrong')
            sys.exit(2)
    else:
        print('name defound')
        sys.exit(0)

def main():
    nowpath = 'OS/'
    while True:
        path = str(nowpath) + ' > '
        userenter = str(input('root@localhost:~#  '))
        log = 'user input \'' + userenter + '\''
        write_new_log(log,'User')
        codes(userenter)

def codes(ent):
    command = ent.split(' ')
    first_com = command[0]
    if ent == 'help':
        print('clear :清空控制台')
        print('find :查找当前目录下的所有文件')
        print('write <path> :将一个字符串写入文件(\\n 换行)(若不存在将创建,若存在会清空内容!!!)')
        print('get <name> :获取文件内容')
        print('create-folder <path> :创建文件夹')
        print('delete-file <path> :删除文件')
        print('delete-folder <path> :删除文件夹')
        print('exit :关机')
        print('info :系统信息')
        print('repwd :重新设置密码')
        print('now :当前时间')
        print('reset-all :恢复出厂设置')
        print('echo <text> :输出文本')
        print('tips :输出系统使用小提示')
    elif ent == 'tips':
        write_new_log('echo tips','info')
        print('')
        print('tip : 请不要将系统文件放置在带有空格的目录下，否则无法解析位置，切记！')
        print('tip : 但凡是带有参数的指令，不要在一个参数内带有空格，切记！')
        print('tip : 此系统与Linux文件管理相同, 要提前加斜杠。如Linux为/etc/xxx.txt , 本系统也为/etc/xxx.txt 。')
        print('')
    elif first_com == 'echo':
        print(str(command[1]))
    elif ent == 'clear':
        os.system('cls')
        write_new_log('clear done','info')
    elif ent == 'exit':
        write_new_log('system exit.','OS')
        write_new_log('power off','OS')
        sys.exit(1)
    elif ent == 'find':
        print('')
        find()
        write_new_log('all path found','info')
        print('')
    elif ent == 'info':
        print('')
        get_os()
        write_new_log('get os info','info')
        print('')
    elif ent == 'repwd':
        write_new_log('user want to reset password','info')
        pwd = input('new password: ')
        logecho = 'user reset password.it is ' + pwd
        file = open('usrpwd.txt', 'w')
        file.write(pwd)
        write_new_log(logecho,'OS')
        write_new_log('password reset.exit reset.','info')
    elif ent == 'now':
        now = datetime.datetime.now()
        print(now)
        write_new_log('now time get.','info')
    elif ent == 'reset-all':
        write_new_log('user want to reset os','WARN')
        write_new_log('user writng password','info')
        ifpwd = input('input your password: ')
        if ifpwd == pwd:
            write_new_log('os reset','WARN')
            set = 'notset'
            print('消除密码...')
            file = open('usrpwd.txt', 'w')
            file.write(set)
            print('清除系统...')
            file = open('OSname.txt', 'w')
            file.write(set)
            path = str(directory) + '/usr/'
            delete_files_in_directory(path)
            print('done')
            time.sleep(1)
            sys.exit(-5)
        else:
            print('password wrong')
            write_new_log('password is wrong.stop reset','info')
    elif command[0] == 'write':
        write_new_log('user writing on file','info')
        if not len(command) >= 2:
            print('index erorr.')
            write_new_log('input error','ERROR')
        else:
            text = input('What will you write in your file?  :')
            path = str(directory) + command[1]
            write(path,text)
    elif command[0] == 'get':
        write_new_log('user geting text on file','info')
        if not len(command) >= 2:
            print('index erorr.')
            write_new_log('input error','ERROR')
        else:
            path = str(directory) + command[1]
            text = get_text(path)
            print(text)
    elif command[0] == 'create-folder':
        write_new_log('user creating folder','info')
        if not len(command) >= 2:
            print('index erorr.')
            write_new_log('input error','ERROR')
        else:
            path = str(directory) + command[1]
            try:
                os.makedirs(path)
                print('path added')
            except FileExistsError:
                print('erorr.path is had on the computer in the past.')
    elif command[0] == 'delete-file':
        write_new_log('user want to delete file','info')
        if str('py') in str(directory) + command[1]:
            write_new_log('OS file cannot delete','WARN')
            print('cannot delete.it is the OS file.')
        else:
            if not len(command) >= 2:
                print('index erorr.')
                write_new_log('input error','ERROR')
            else:
                path = str(directory) + command[1]
                delete_single_file(path)
                write_new_log('delete done','info')
    elif command[0] == 'delete-folder':
        write_new_log('user want to delete folder','info')
        if str('etc') in str(directory) + command[1] or '/' == command[1]:
            write_new_log('cannot delete,it is OS folder')
            print('cannot delete.it is the OS folder.')
        else:
            if not len(command) >= 2:
                print('index erorr.')
                write_new_log('input error','ERROR')
            else:
                write_new_log('delete done','info')
                path = str(directory) + command[1]
                delete_directory(path)

    else:
        write_new_log('commands defound.','info')
        print('Not find "' + ent + '" of commands.Please retry or input "help".')


if __name__ == '__main__':
    os.system('cls')
    start()
    if pwd == 'notset':
        print('user name is "root"')
        pwd = input(' OS: set your password: ')
        file = open('usrpwd.txt', 'w')
        file.write(pwd)
        file.close()
      
    write_new_log('booting','OS')
    login()
    os.system('cls')
    main()
