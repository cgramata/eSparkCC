from studentResultObject import StudentResultObject

class CurriculumAssignment:

	def makeTheCurriculumPerStudent(self, studentName, testScoreDictionary, domainDictionary, sizeOfNeededCurriculum):

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
						setattr(studentObject,curriculum,getattr(studentObject,curriculum)+1)
					else:
						resultingCurriculum.append(str(key)+"."+curriculum)
						setattr(studentObject,curriculum,getattr(studentObject,curriculum)+1)

		return(resultingCurriculum)
