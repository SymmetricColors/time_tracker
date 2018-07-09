import argparse
import tracker
class input_args():

    def __init__(self):
        parser=argparse.ArgumentParser(description="my working time tracker")
        parser.add_argument("-t", action='store')
        parser.add_argument("-s" , action='store' )
        args=parser.parse_args()

        if args.t:
            tracker.main()

        if args.s:
            print("hello world")

a=input_args()