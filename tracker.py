import argparse
import track
import dataSource
class time_tracker():

    def __init__(self):
        parser=argparse.ArgumentParser(description="my working time tracker")
        parser.add_argument("-t", action='store',help="track the specified project time")
        parser.add_argument("-s" , action='store',help="show worked hours for specified project" )
        parser.add_argument("-a", action="store",help="show all the times for specified project")
        args=parser.parse_args()

        if args.t:
            track.main(args.t)

        if args.s:
            datasource=dataSource.DataSource('working_dates.db')
            times=datasource.get_data(args.s)
            sum_of_seconds=0
            for time in times:
                sum_of_seconds+=time[3]
            print(sum_of_seconds/3600)

        if args.a:
            datasource=dataSource.DataSource('working_dates.db')
            times=datasource.get_data(args.a)
            for time in times:
                temp=str(time)
                temp=temp.replace('u','')
                temp=temp.replace('\'','')
                temp=temp.replace('(','')
                temp=temp.replace(')','')
                print(temp)
a=time_tracker()