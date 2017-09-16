from currSize import CurrSize
from studentResultObject import StudentResultObject
from curriculumAssignment import CurriculumAssignment
from importExportData import ImportExportData
from translateData import TranslateData


def main():
    finalStudentCurriculum = []

    dataObject = ImportExportData()
    domainFileReaderMain = dataObject.importDomainFile()
    testScoresReaderMain = dataObject.importStudentTestFile()
    curriculumAttribute = CurrSize()
    curriculumObject = CurriculumAssignment()
    rawDataObject = TranslateData(domainFileReaderMain, testScoresReaderMain)

    for name in rawDataObject.listOfStudentNames:
        madeCurriculum = curriculumObject.makeTheCurriculumPerStudent(name,
                                                                      rawDataObject.studentScoreDictionary,
                                                                      rawDataObject.gradeCourseDictionary,
                                                                      curriculumAttribute.curriculumSize)
        finalStudentCurriculum.append(madeCurriculum)

    #creates file "resultingStudentCurriculum.csv" in directory
	dataObject.writeCurriculumResult(finalStudentCurriculum)


if __name__ == "__main__": main()
