
import time
import sys

def get_osname():
     try:
       file = open('OSname.txt', 'r')
       osname = file.read()
       file.close()
       if osname == 'notset':
           osname = input('set your os name: ')
           file = open('OSname.txt', 'w')
           file.write(osname)
     except FileNotFoundError:
       print('文件未找到,引导失败,Error -1')
       time.sleep(1)
       sys.exit(-1)
     return str(osname)
     

def loading():
    for i in range(11):
        progress = "#" * i + "-" * (10 - i)
        print(f"\r{progress}",end="")
        time.sleep(0.2)
    print('')

def start():
        file = open('OSname.txt', 'r')
        name = file.read()
        if name == 'notset':
          print('Prepared YangOS...')
          loading()
          print('done,now set os name and pwd')
          get_osname()
        else:
          print('starting YangOS...')
          loading()
          print('done,now login')
          get_osname()


