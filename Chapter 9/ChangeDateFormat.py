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
os.chdir('/home/justin/Python-Workspace/AutomateTheBoringStuff/Chapter\ 9')
#find all instances of files with american names in the directory
for folder, subfolder, file in os.walk():
    if amerNameRegex.match(file):
        print(file)

#flip the date and month spot on each found file with shutil.mv

#print message of completion
print('end of program')
