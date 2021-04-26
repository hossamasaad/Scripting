# Imporing essintial libraries
import os
import shutil
import argparse
import datetime


# check if file or directory
def isDirectory(filePath):
    return os.path.isdir(filePath) == True

# Get directory name
def getDirName(dirPath):
    return dirPath.split('\\')[-1]

# Get extentions of the file
def getExt(name):
    return name.split('.')[-1]


# Move files from source to desintation
def moveFilesByType(source, destination):
    
    # Get Source directory files
    files = os.listdir(source)
    
    # Go throw files in the source directory
    for file in files:
        
        # get file ectintion to order files
        EXT = getExt(file)

        # get file source and destination
        frm = os.path.join(source, file)
        to = os.path.join(destination, EXT.upper())
        
        # check if there is a directory for this extintion or not
        if not os.path.exists(to) and not isDirectory(frm):
            os.mkdir(to)
        
        # finaly move the file

        shutil.move(frm, to)

def moveFilesByDate(source, destination):
    
    # Get Source directory files
    files = os.listdir(source)
    
    # Go throw files in the source directory
    for file in files:
        
        # get file source
        frm = os.path.join(source, file)

        # get file ectintion to order files
        timestamp = os.path.getmtime(frm)
        date = datetime.datetime.fromtimestamp(timestamp)
        date_str = str(date.year) + '-' + str(date.month) + '-' + str(date.day)

        # get file destination by date
        to = os.path.join(destination, date_str)

        # check if there is a directory for this extintion or not
        if not os.path.exists(to) and not isDirectory(frm):
            os.mkdir(to)
        
        # finaly move the file
        shutil.move(frm, to)

# main
def main():
     
    # Adding parsers
    parser = argparse.ArgumentParser(description='Moving files from source file to destination')
    parser.add_argument(dest='source', type=str, help="source directory")
    parser.add_argument(dest='destination', type=str, help="destination directory")
    parser.add_argument(dest='moving_type', type=str, help="Moving Type(date or type)")


    # source file
    source = parser.parse_args().source
    destination = parser.parse_args().destination
    moving_type = parser.parse_args().moving_type

    # Check is these directories or not
    if not (isDirectory(source) and isDirectory(destination)):
        print('There is an error in directories Pathes !!!!')
        return
    
    if moving_type == 'date':
        moveFilesByDate(source, destination)
    else:
        moveFilesByType(source, destination)


if __name__ == '__main__':
    main()
