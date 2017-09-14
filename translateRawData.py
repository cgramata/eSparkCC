class TranslateRawData:

	def __init__(self, listOfGradeCourses, listOfStudentScores):
		self.gradeCourseDictionary = self.createGradeCourseDictionary(listOfGradeCourses)
		self.listOfStudentNames = self.createListOfStudentNames(listOfStudentScores)
		self.testVariable2 = "test2"
		self.testVariable3 = "test3"


	def createListOfStudentNames(self, listOfStudentScores):
		nameOfStudents = []

		for row in listOfStudentScores[1:]:
			row = filter(None, row)
			#scoreDictionary[row[0]] = row[1:]
			nameOfStudents.append(row[0])

		return (nameOfStudents)


	def createGradeCourseDictionary(self, listOfGradeCourses):
		gradeCourseDictionary = {}

		for row in listOfGradeCourses:
			row = filter(None, row)
			if row[0] == "K":
				row[0] = "0"
			gradeCourseDictionary[int(row[0])] = row[1:]

		return (gradeCourseDictionary)