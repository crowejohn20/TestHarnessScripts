'''
Created on Jul 20, 2015

@author: john.crowe
'''

import os

testLog = ("/Users/john.crowe/Desktop/test.txt")

def generateFileList():
    
    fileList = os.listdir("/Users/john.crowe/Desktop/Qa Model Objs")
    testFiles = open(testLog,"w")
    
    for x in fileList:
        if x.endswith(".obj"):
            print ("Adding File " + x)
            testFiles.write(x +"\n")
    testFiles.close()

def checkTestFiles():
    if os.stat(testLog).st_size == 0:
        print ("File empty. Regenerating file list from directory.")
        generateFileList()
    return
    
def getFile():
    
    readFile = open(testLog, "r").read()
    fileList = readFile.split("\n")[:-1]
    selectedFile =  fileList.pop(0)
    writeFile = open(testLog, "w")
    
    for x in fileList:
        writeFile.write(x + "\n")
    writeFile.close()
    return selectedFile
    
checkTestFiles()
myFile= getFile()
print ("File Selected for testing: " + myFile)