import os

class GetFile(object):
    ''' Methods to gather and return information on models stored in the test harness ''' 
    
    def __init__(self, modelList, path, extension):
        self.list    = modelList 
        self.path    = path
        self.ext     = extension
        self.listDir = os.listdir(self.path)
    
    def writeFile(self):
        self.write = open(self.list, "w")
        return self.write
    
    def readFile(self):
        self.read = open(self.list, "r")
        return self.read
        
    def populateFileList(self):
        
        toFile = self.writeFile()
    
        for model in self.listDir:
            if model.endswith(self.ext):
                print ("Adding File " + model)
                toFile.write(model +"\n")
        toFile.close()

    def checkTestFiles(self):
        
        if os.stat(self.list).st_size == 0:
            print ("File empty. Regenerating file list from directory.")
            self.populateFileList()
        return
    
    def printFileContent(self):
        ''' Print content of file before regeneration.'''
        print self.readFile().read()
        
    def manageFiles(self):
        
        self.checkTestFiles()
        
        objFileList = (self.readFile().read()).split("\n")[:-1]
        selectedFile = objFileList.pop(0)
        
        objWriteList = self.writeFile()
        
        for obj in objFileList:
            objWriteList.write(obj + "\n")
        objWriteList.close()
        
        return selectedFile

MODELTYPE = ".obj"
MODELPATH = "/Users/john.crowe/Desktop/Qa Model Objs"
myFile = GetFile("/Users/john.crowe/Desktop/test.txt", MODELPATH, MODELTYPE )
myFile.printFileContent()