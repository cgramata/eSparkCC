from resourceFile import ResourceFile
from studentResultObject import StudentResultObject
from curriculumAssignment import CurriculumAssignment
from importExportData import ImportExportData
from transformData import TransformData


def main():
    finalStudentCurriculum = []

    dataObject = ImportExportData()
    resourceAttribute = ResourceFile()
    finalCurriculumObject = CurriculumAssignment()
    rawDomainFileData = dataObject.importDomainFile()
    rawTestScoresData = dataObject.importStudentTestFile()
    transformedDataObject = TransformData(rawDomainFileData, rawTestScoresData)

    for name in transformedDataObject.listOfStudentNames:
        finalIndividualCurriculum = finalCurriculumObject.makeTheCurriculumPerStudent(name,
                                                                      transformedDataObject.studentScoreDictionary,
                                                                      transformedDataObject.gradeCourseDictionary,
                                                                      resourceAttribute.curriculumSize)
        finalStudentCurriculum.append(finalIndividualCurriculum)

    #creates file "resultingStudentCurriculum.csv" in directory
	  #dataObject.writeCurriculumResult(finalStudentCurriculum)

    for curriculum in finalStudentCurriculum: 
      print curriculum


if __name__ == "__main__": main()
