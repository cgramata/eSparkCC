from resourceFile import ResourceFile
from studentResultObject import StudentResultObject
from curriculumAssignment import CurriculumAssignment
from importExportData import ImportExportData
from transformData import TransformData


def main():
    listOfFinalStudentCurriculums = []

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
        listOfFinalStudentCurriculums.append(finalIndividualCurriculum)

    #creates file "resultingStudentCurriculum.csv" in directory
	  #dataObject.writeCurriculumForStudent(listOfFinalStudentCurriculums)

    for curriculum in listOfFinalStudentCurriculums: 
      print curriculum


if __name__ == "__main__": main()
