from studentResultObject import StudentResultObject

class CurriculumAssignment:

	#takes in raw data as first two parameters, stores resulting information into tables and dictionaries
	def storeFileValues(self,
						domainList,
						scoreTestList,
						domainDictionary,
						scoreDictionary,
						listOfNames,
						testScoresLayout):

		for row in domainList:
			row = filter(None, row)
			if row[0] == "K":
				row[0] = "0"
			domainDictionary[int(row[0])] = row[1:]
			

		for row in scoreTestList[1:]:
			row = filter(None, row)
			scoreDictionary[row[0]] = row[1:]
			listOfNames.append(row[0])

		for name in listOfNames:
			self.replaceKValueInList(scoreDictionary[name])
			self.strValuesToInt(scoreDictionary[name])

		for row in scoreTestList[0:1]:
			for value in row[1:]:
				testScoresLayout.append(value)


	def strValuesToInt(self, listWithStr):
		for entry in range(len(listWithStr)):
			listWithStr[entry] = int(listWithStr[entry])



	#If it has the value "K" it is replaced with an int value of 0
	def replaceKValueInList(self, scoreList):
		for score in range(len(scoreList)):
			if scoreList[score] == "K":
				scoreList[score] = "0" 


	def makeTheCurriculumPerStudent(self,
									studentName,
									testScoreDictionary,
									domainDictionary,
									sizeOfNeededCurriculum):

		resultingCurriculum = []
		minResult = min(testScoreDictionary[studentName]) 

		studentObject = StudentResultObject(studentName, testScoreDictionary[studentName])

		resultingCurriculum.append(studentName)
		

		for key in range(minResult,sizeOfNeededCurriculum):

			curriculumOrder = domainDictionary[key]
			for curriculum in curriculumOrder:
				if getattr(studentObject,curriculum) <= key and len(resultingCurriculum) != sizeOfNeededCurriculum:
					if key == 0:
						resultingCurriculum.append("K"+"."+curriculum)
						studentCurriculumSize = len(resultingCurriculum)
						setattr(studentObject,curriculum,getattr(studentObject,curriculum)+1)
					else:
						resultingCurriculum.append(str(key)+"."+curriculum)
						studentCurriculumSize = len(resultingCurriculum)
						setattr(studentObject,curriculum,getattr(studentObject,curriculum)+1)

		return(resultingCurriculum)
