from currSize import CurrSize
from studentResultObject import StudentResultObject
from curriculumAssignment import CurriculumAssignment
from importRawData import ImportRawData
from translateRawData import TranslateRawData


def main():
	domainDictionary = {}
	testScoreDictionary = {}
	listOfStudentNames = []
	finalStudentCurriculum = []

	dataObject = ImportRawData()
	domainFileReaderMain = dataObject.importDomainFile()
	testScoresReaderMain = dataObject.importStudentTestFile()

	rawDataObject = TranslateRawData(domainFileReaderMain, testScoresReaderMain)

	#creates objects to access methods or variables
	curriculumAttribute = CurrSize()
	curriculumObject = CurriculumAssignment()

	print(rawDataObject.gradeCourseDictionary)

	curriculumObject.storeFileValues(domainFileReaderMain,
									 testScoresReaderMain,
									 domainDictionary,
									 testScoreDictionary,
									 listOfStudentNames)


	for name in listOfStudentNames:
		madeCurriculum = curriculumObject.makeTheCurriculumPerStudent(name, 
																	  testScoreDictionary,
																	  domainDictionary,
																	  curriculumAttribute.curriculumSize)
		finalStudentCurriculum.append(madeCurriculum)

	#todo change this to write to a csv file instead of printing
	for curriculum in finalStudentCurriculum:
		print curriculum


if __name__ == "__main__": main()

