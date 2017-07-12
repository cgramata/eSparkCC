class CurriculumAssignment:

	#takes in raw data as first two parameters, stores resulting information into tables and dictionaries
	def storeFileValues(self, domainList, scoreTestList, domainDictionary, domainGradeRange, scoreDictionary, listOfNames, testScoresLayout):
		for row in domainList:
			row = filter(None, row)
			domainDictionary[row[0]] = row[1:]
			domainGradeRange.append(row[0])

		self.replaceKValue(domainGradeRange)
		self.strValuesToInt(domainGradeRange)
		self.increaseMaxGrade(domainGradeRange)
		
		#adds another grade to the max grade range
		for row in scoreTestList[1:]:
			row = filter(None, row)
			scoreDictionary[row[0]] = row[1:]
			listOfNames.append(row[0])

		for row in scoreTestList[0:1]:
			for value in row[1:]:
				testScoresLayout.append(value)


	def strValuesToInt(self, listWithStr):
		for entry in range(len(listWithStr)):
			listWithStr[entry] = int(listWithStr[entry])


	def increaseMaxGrade(self, listOfGrades):
		newMaxGrade = max(listOfGrades) + 1
		listOfGrades.append(newMaxGrade)


	#If it has the value "K" it is replaced with an int value of 0
	def replaceKValue(self, scoreList):

		for score in range(len(scoreList)):
			if scoreList[score] == "K":
				scoreList[score] = 0 


	#def storeStudentAttributes(self, name):


	#def makeTheCurriculum(self, finalCurriculumList, numberOfCurriculum):

		#while len(finalCurriculumList) != numberOfCurriculum:
			#for 
	




