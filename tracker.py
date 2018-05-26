import datetime
import time
import sys


try:
    current_work = sys.argv[1]
except IndexError:
    print("please specify your project")
    exit(1)
dt=datetime.datetime.now()
times=open('times','a')
times.write("[start] session started at {0}\n".format(dt))
try:
    time.sleep(100000000000000)
except KeyboardInterrupt:
    dt2=datetime.datetime.now()
    times.write('[stopped] session stopped at {0}\n'.format(dt2))
    times.write('[duration] @{1} session duration {0}\n'.format(dt2-dt,current_work))