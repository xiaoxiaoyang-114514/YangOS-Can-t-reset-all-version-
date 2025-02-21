from gwt import write,get_text
import datetime
import os
directory = os.path.dirname(os.path.abspath(__file__))

def write_new_log(log,log_type):
    logtime = '[' + str(datetime.datetime.now()) + ']'
    logpath = directory + '/etc/lastlog.txt'
    logs = get_text(logpath)
    writelog = logtime + ':' + '[' + log_type + ']' + '  ' +  log + '\n'
    willwrite = logs + writelog
    write(logpath,willwrite)