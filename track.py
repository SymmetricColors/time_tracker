import datetime
import time
import sys
import jalali
import sqlite3
import dataSource
def main(project_name):
    # try:
    #     current_work = sys.argv[1]
    # except IndexError:
    #     print("please specify your project")
    #     exit(1)
    dt=datetime.datetime.now()
    try:
        time.sleep(100000000000000)
    except KeyboardInterrupt:
        dt2=datetime.datetime.now()
        current_georgian_date="{0}-{1}-{2}".format(dt2.year,dt2.month,dt2.day)
        current_persian_date=jalali.Gregorian(dt.year,dt.month,dt.day).persian_string()
        duration=(dt2-dt).total_seconds()
        date=(current_georgian_date,str(dt),str(dt2),duration,project_name,current_persian_date)
        datasource=dataSource.DataSource('working_dates.db')
        datasource.insert_data(date)

