import os
import datetime
import argparse

argparser = argparse.ArgumentParser(description='Writes date in front of the filename')
argparser.add_argument("-t", "--today",  help="set the current date", action="store_true")
argparser.add_argument("-c", "--custom", help="specify the date in the filename, YYYY-MM-DD")
args = argparser.parse_args()

# Get the name of the current script
current_script = os.path.basename(__file__)[:-3]

# Get all files in the current directory except this script
files = [file for file in os.listdir('.') 
         if os.path.isfile(file) 
         and file != current_script + '.py'
         and file != current_script + '.exe']

for file in files:
    try:
        # filename already has a date
        datetime.datetime.strptime(file[:10], '%Y-%m-%d')
    except:
        if args.today:
            # get the current date
            date = str(datetime.datetime.now())[:10]
        elif args.custom:
            # date specified by the user
            date = args.custom
        else:
            # get the creation date of the file
            creation_time = os.path.getctime(file)
            date = str(datetime.datetime.fromtimestamp(creation_time))[:10]
            
        # rename the file
        os.rename(file, date + '_' + file)