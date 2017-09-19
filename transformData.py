class TransformData:
    def __init__(self, listOfGradeCourses, listOfStudentScores):
        self.gradeCourseDictionary = self.createGradeCourseDictionary(listOfGradeCourses)
        self.listOfStudentNames = self.createListOfStudentNames(listOfStudentScores)
        self.studentScoreDictionary = self.createStudentScoreDictionary(listOfStudentScores)

    def createListOfStudentNames(self, listOfStudentScores):
        nameOfStudents = []

        for row in listOfStudentScores[1:]:
            row = filter(None, row)
            # scoreDictionary[row[0]] = row[1:]
            nameOfStudents.append(row[0])

        return nameOfStudents

    def createGradeCourseDictionary(self, listOfGradeCourses):
        gradeCourseDictionary = {}

        for row in listOfGradeCourses:
            row = filter(None, row)
            if row[0] == "K":
                row[0] = "0"
            gradeCourseDictionary[int(row[0])] = row[1:]

        return gradeCourseDictionary

    def createStudentScoreDictionary(self, listOfStudentScores):
        studentScoreDictionary = {}

        for row in listOfStudentScores[1:]:
            row = filter(None, row)
            rowValue = self.changeKToZero(row[0:])
            studentScoreDictionary[row[0]] = list(map(int, rowValue[1:]))

        return (studentScoreDictionary)

    def changeKToZero(self, scoreList):
        newValueList = []

        for score in range(len(scoreList)):
            if scoreList[score] == "K":
                newValueList.append('0')
            else:
                newValueList.append(scoreList[score])

        return newValueList
