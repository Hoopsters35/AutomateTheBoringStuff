#!usr/bin/env python
import re, os, shutil

#create regex to find american name
amerNameRegex = re.compile(('''
    (\w)*                  #name of file before date
    ([01][0-9])            #month
    ([-/])?                #separator (optional)
    ([0-3][0-9])           #day
    ([-/])?                #separator (optional)
    ([12][90][0-9][0-9])   #year
    (\w)*                  #name of file after date (with ext)
    '''), re.VERBOSE)

#cd to the correct directory
print(os.getcwd())
#find all instances of files with american names in the directory

#flip the date and month spot on each found file with shutil.mv

#print message of completion
