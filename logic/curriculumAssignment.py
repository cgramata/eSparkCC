from studentResultObject import StudentResultObject


class CurriculumAssignment:
    def makeTheCurriculumPerStudent(self, studentName, testScoreDictionary, gradeCourseDictionary, sizeOfNeededCurriculum):

        resultingCurriculum = []

        minResult = min(testScoreDictionary[studentName])
        studentObject = StudentResultObject(studentName, testScoreDictionary[studentName])

        resultingCurriculum.append(studentName)

        for gradeLevel in range(minResult, sizeOfNeededCurriculum):
            curriculumOrder = gradeCourseDictionary[gradeLevel]
            for curriculum in curriculumOrder:
                if getattr(studentObject, curriculum) <= gradeLevel and len(resultingCurriculum) != sizeOfNeededCurriculum:
                    if gradeLevel == 0:
                        resultingCurriculum.append("K" + "." + curriculum)
                        setattr(studentObject, curriculum, getattr(studentObject, curriculum) + 1)
                    else:
                        resultingCurriculum.append(str(gradeLevel) + "." + curriculum)
                        setattr(studentObject, curriculum, getattr(studentObject, curriculum) + 1)

        return resultingCurriculum
