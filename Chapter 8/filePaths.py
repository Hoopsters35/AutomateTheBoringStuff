import os #useful module to work with file paths
os.sep #gets the separator for the current operating system - \ (\\) on windos, / on mac/linux
os.path.join("c:\\", 'users', 'justi', 'Python-Workspace', 'doodle.png') #combines strings with os.sep

CurrentWorkingDirectory = os.getcwd()

#os.chdir('C:\\') #changes cwd

#absolute file paths contain entire file path
#relative file path contains file path based on cwd
#
#. in file path stands for this folder
#.. in file path stands for parent folder
#
absPath = os.path.abspath("spam.png") # returns the absolute path from a relative
os.path.isabs("spam.png") #returns false because this is a relative path

os.path.relpath(path, filename)
#os.path.isrel
#
os.path.dirname(fullpath) #returns path
os.path.basename(fullpath) #returns filename

os.path.exists(path) #returns boolean if it exists
os.path.isdir(path) #returns true if the path is a folder
os.path.isfile(path) #returns true if path is a file


os.path.getsize(filename) #returns size in bytes
os.listdir(directory name) #lists everything in given directory

os.makedirs(filepath) #makes directory for given path

