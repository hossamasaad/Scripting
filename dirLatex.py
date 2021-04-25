# Imporing essintial libraries
import argparse
import os


# check if file or directory
def isDirectory(filePath):
    return os.path.isdir(filePath) == True


# Get directory name
def getDirName(dirPath):
    return dirPath.split('\\')[-1]


# Traverse the directory
def searchDir(filePath, depth):
    # indent shape
    indent = '  '

    # Get Current directory files
    fileList = os.listdir(filePath)
    
    # print the current directory name
    dirName = getDirName(filePath)
    print('{}.{} {}'.format(indent * depth, depth+1, '{' + dirName + '} .'))

    # Go throw The List
    for file in fileList:

        # Check if the file dirctory or not
        if isDirectory(file):

            # join current path with the new directory to get the new path of sub directory
            newPath = os.path.join(filePath, file)

            os.chdir(newPath)                                # Go To the sub Directory
            searchDir(newPath, depth+1)                      # Traverse the sub directory
            os.chdir(filePath)                               # Back to the main directory

        else:
            # Print File name
            print("{}.{} {}".format(indent*(depth+1), depth+2, '{' + file + '} .'))        
     

def main(): 

    # Adding parsers
    parser = argparse.ArgumentParser(description='Print the directory-tree code for the LaTeX dirtree package')
    parser.add_argument(dest='path', type=str, help="Root directory of the tree")

    # get the directory path
    dirPath = parser.parse_args().path

    # Traverse The directory 
    print('\\dirLatex {% ')
    searchDir(dirPath, 0)
    print('}')


if __name__ == '__main__':
    main()