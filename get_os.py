import platform
import os
from start import get_osname
def get_os():
    print("操作系统名称:", platform.system())
    print("操作系统版本:", platform.release())
    print("操作系统详细版本:", platform.version())
    print("处理器名称:", platform.machine())
    print("处理器信息:", platform.processor())
    print("系统架构:", platform.architecture())
    print('内部操作系统：YangOS')
    name = get_osname()
    print('内部操作系统自定义名称：' + name)
