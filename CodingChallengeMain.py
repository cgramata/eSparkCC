from currSize import CurrSize
from studentResultObject import StudentResultObject
from curriculumAssignment import CurriculumAssignment
from importRawData import ImportRawData
from translateRawData import TranslateRawData


def main():
	finalStudentCurriculum = []

	dataObject = ImportRawData()
	domainFileReaderMain = dataObject.importDomainFile()
	testScoresReaderMain = dataObject.importStudentTestFile()
	curriculumAttribute = CurrSize()
	curriculumObject = CurriculumAssignment()
	rawDataObject = TranslateRawData(domainFileReaderMain, testScoresReaderMain)


	for name in rawDataObject.listOfStudentNames:
		madeCurriculum = curriculumObject.makeTheCurriculumPerStudent(name,
																	  rawDataObject.studentScoreDictionary, 
																	  rawDataObject.gradeCourseDictionary, 
																	  curriculumAttribute.curriculumSize)
		finalStudentCurriculum.append(madeCurriculum)

	#todo change this to write to a csv file instead of printing
	for curriculum in finalStudentCurriculum:
		print curriculum


if __name__ == "__main__": main()

