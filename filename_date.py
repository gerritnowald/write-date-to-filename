import os
import datetime
import argparse

argparser = argparse.ArgumentParser(description='Writes creation date into the filename')
argparser.add_argument("-d", "--date", help="Specify the date in the filename, YYYY-MM-DD")
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
        if args.date:
            # date specified by the user
            os.rename(file, args.date + '_' + file)
        else:
            # get the creation date of the file
            creation_time = os.path.getctime(file)
            creation_date = datetime.datetime.fromtimestamp(creation_time)

            # rename the file
            os.rename(file, str(creation_date)[:10] + '_' + file)