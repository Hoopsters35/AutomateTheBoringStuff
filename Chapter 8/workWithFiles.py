#use shelf to save variables and methods etc (binary shelves) 
#for txt files, work with open(path, r/w/a) and use read methods or write methods
#
#to save data structures, use shelve
import shelve

shelfFile = shelve.open('mydata') #opens like a file
shelfFile['animals'] = ['Zoey', 'Jake', 'Snickles'] #stores information in a dictionary format
keys = list(shelfFile.keys())
contents = list(shelfFile.values())
shelfFile.close() #can be reopened at any time to get data

#mess with location of files/directories
import shutil
shutil.copy(filePath, newFilePath) #copies a single file and places it with given dir and name
shutil.copytree(dirPath, newDirPath)  #copies an entire directory and places it in given dir and name

shutil.move(filePath, newFilePath) #directly moves file to new loc- 
#move is also used to rename files by giving same location, and giving new name


#how to delete files/directories
import os
os.unlink(path) #deletes file at given path
os.rmdir(path) #deletes EMPTY directory at given path

#to delete a dir with contents --
#import shutil
shutil.rmtree(path) #removes given directory --use with caution

#use send2trash module to send it to recycling bin instead of perm deleting -- must use pip to install (section 11 lesson 33)
send2trash.send2trash(path) #sends the item at the path to recycling bin

#walking a directory tree --
#import os
for foldername, subfolders, filenames in os.walk(path): #each iterations returns all 3
	print('foldername is: ', foldername)
	print('subfolders are: ', str(subfolders))
	print('files inside the folders are: ', str(filenames))
#this loop walks through eveything in a given dir. it starts with the parent dir and then goes deeper inside folders
#very efficient for using conditional statements to find particular names of files or directories inside any folder or filename


