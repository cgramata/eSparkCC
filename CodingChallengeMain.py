from currSize import CurrSize
from studentResultObject import StudentResultObject
from curriculumAssignment import CurriculumAssignment
from importTranslateRawData import ImportTranslateRawData


def main():
	domainDictionary = {}
	testScoreDictionary = {}
	listOfStudentNames = []
	layoutOfScores = []
	finalStudentCurriculum = []

	dataObject = ImportTranslateRawData()
	domainFileReaderMain = dataObject.importDomainFile()
	testScoresReaderMain = dataObject.importStudentTestFile()

	#creates objects to access methods or variables
	curriculumAttribute = CurrSize()
	curriculumObject = CurriculumAssignment()


	curriculumObject.storeFileValues(domainFileReaderMain,
									 testScoresReaderMain,
									 domainDictionary,
									 testScoreDictionary,
									 listOfStudentNames,
									 layoutOfScores)


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

