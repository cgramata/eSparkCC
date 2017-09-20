class TransformData:
    def __init__(self, listOfGradeCourses, listOfStudentScores):
        self.gradeCourseDictionary = self.createGradeCourseDictionary(listOfGradeCourses)
        self.listOfStudentNames = self.createListOfStudentNames(listOfStudentScores)
        self.studentScoreDictionary = self.createStudentScoreDictionary(listOfStudentScores)

    #creates a list of student names from the student test score file
    def createListOfStudentNames(self, listOfStudentScores):
        nameOfStudents = []

        for row in listOfStudentScores[1:]:
            row = filter(None, row)
            nameOfStudents.append(row[0])

        return nameOfStudents

    #the key is actual grade level, the value are the courses offered at each grade level in a list
    def createGradeCourseDictionary(self, listOfGradeCourses):
        gradeCourseDictionary = {}

        for row in listOfGradeCourses:
            row = filter(None, row)
            if row[0] == "K":
                row[0] = "0"
            gradeCourseDictionary[int(row[0])] = row[1:]

        return gradeCourseDictionary

    #the key is the student name, the value are the students' test scores in a list
    def createStudentScoreDictionary(self, listOfStudentScores):
        studentScoreDictionary = {}

        for row in listOfStudentScores[1:]:
            row = filter(None, row)
            studentScores = self.changeKToZero(row[0:])
            studentScoreDictionary[row[0]] = list(map(int, studentScores[1:]))

        return (studentScoreDictionary)

    def changeKToZero(self, scoreList):
        convertedValueList = []

        for score in range(len(scoreList)):
            if scoreList[score] == "K":
                convertedValueList.append('0')
            else:
                convertedValueList.append(scoreList[score])

        return convertedValueList
