# --------------------------------------------------------------------------
# Purpose: To help test new geometry in Mari
# Discription:
# This code is used on the test harness to pick a new geometry everytime the test harness is run, it will keep a basic track of whats being tested and what it has left to test.
# It is used in CreateProject, Alembic, FBX 
# --------------------------------------------------------------------------

import os

class GetFile(object):
	''' Methods to gather and return information on models stored in a text file on netqa''' 
	
	def __init__(self, modelList, path, extension):
		self.geoList    = modelList 
		self.path    = path
		self.ext     = extension
		self.geoListDir = os.listdir(self.path)
		self.pickedForTesting = self.manageFiles()
	
	def writeFile(self):
		""" Funtion to open up a file for writing"""

		self.write = open(self.geoList, "w")
		return self.write
	
	def readFile(self):
		""" Funtion to open up a file for reading"""

		self.read = open(self.geoList, "r")
		return self.read
		
	def populateFileList(self):
		""" Creates a text file list of file names within a directory, that match the supplied extention """
		
		toFile = self.writeFile()
	
		for model in self.geoListDir:
			if model.endswith(self.ext):
				modelInfo = os.stat(os.path.join(self.path, model))
				print ("**** Adding File %s" % model + " Size: %s" % str(modelInfo.st_size) + " bytes")
				toFile.write(model +"\n")
		toFile.close()

	# We check if the file is empty or if it contains only a new line character
	def checkTestFiles(self):
		""" Checks if the list of test objects from a file is empty or not """
		if os.stat(self.geoList).st_size == 0 or self.readFile().readline() =="\n":
			print ("\n****" + str(self.ext) + " files empty, regenerating list from directory " + str(self.geoList))
			self.populateFileList()
		return
	
	def printFileContent(self):
		''' Prints the content of text file '''
		print self.readFile().read()

	def manageFiles(self):
		""" Picks the next geometry for testing them update the list """
		self.checkTestFiles()
		
		objFileList = (self.readFile().read()).split("\n")[:-1]
		selectedFile = str(objFileList.pop(0)).rstrip() 
		objWriteList = self.writeFile()
		
		for obj in objFileList:
			objWriteList.write(obj + "\n")
		objWriteList.close()
		return selectedFile
