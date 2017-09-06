import csv
from currSize import CurrSize
from studentResultObject import StudentResultObject
from curriculumAssignment import CurriculumAssignment


def importFiles():
	listOfDomainRows = []
	listOfTestScoreRows = []
	domainFile = open("domain_order.csv")
	scoresFile = open("student_tests.csv")

	domainFileReader = csv.reader(domainFile, delimiter=',')
	scoresFileReader = csv.reader(scoresFile, delimiter=',')
	
	for row in domainFileReader:
		listOfDomainRows.append(row)

	for row in scoresFileReader:
		listOfTestScoreRows.append(row)

	domainFile.close()
	scoresFile.close()

	return (listOfDomainRows, listOfTestScoreRows)


def main():
	domainDictionary = {}
	domainGradeRange = []
	testScoreDictionary = {}
	listOfStudentNames = []
	layoutOfScores = []
	gradeRange = []
	finalStudentCurriculum = []

	#creates objects to access methods or variables
	curriculumAttribute = CurrSize()
	curriculumObject = CurriculumAssignment()

	#first stores raw data from csv files
	#then stores broken down data into lists and dictionaries
	domainFileReaderMain, testScoresReaderMain = importFiles()
	curriculumObject.storeFileValues(domainFileReaderMain,testScoresReaderMain,domainDictionary,domainGradeRange,
		testScoreDictionary,listOfStudentNames,layoutOfScores)


	for entry in range(len(listOfStudentNames)):
		name = listOfStudentNames[entry]
		madeCurriculum = curriculumObject.makeTheCurriculumPerStudent(name, testScoreDictionary, domainDictionary, curriculumAttribute.curriculumSize)
		finalStudentCurriculum.append(madeCurriculum)

	for curriculum in finalStudentCurriculum:
		print curriculum


if __name__ == "__main__": main()

