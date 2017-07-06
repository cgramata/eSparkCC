class CurriculumAssignment:


	def storeFileValues(self, domainList, scoreTestList, domainDictionary, domainGradeRange, scoreDictionary, listOfNames, testScoresLayout):

		for row in domainList:
			row = filter(None, row)
			domainDictionary[row[0]] = row[1:]
			domainGradeRange.append(row[0])

		for row in scoreTestList[1:]:
			row = filter(None, row)
			scoreDictionary[row[0]] = row[1:]
			listOfNames.append(row[0])

		for row in scoreTestList[0:1]:
			for value in row[1:]:
				testScoresLayout.append(value)