import csv
from currSize import CurrSize
from studentResultObject import StudentResultObject
from curriculumAssignment import CurriculumAssignment
from currSize import CurrSize


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

	return (listOfDomainRows, listOfTestScoreRows)


def main():
	domainDictionary = {}
	domainGradeRange = []
	testScoreDictionary = {}
	listOfStudentNames = []
	layoutOfScores = []
	gradeRange = []
	resultingCurriculum = []

	#creates objects to access methods or variables
	curriculumAttribute = CurrSize()
	curriculumObject = CurriculumAssignment()

	#first stores raw data from csv files
	#then stores broken down data into lists and dictionaries
	domainFileReaderMain, testScoresReaderMain = importFiles()
	curriculumObject.storeFileValues(domainFileReaderMain,testScoresReaderMain,domainDictionary,domainGradeRange,
		testScoreDictionary,listOfStudentNames,layoutOfScores)


	#for name in range(len(listOfStudentNames)-1):

	

	#studentObjectTest = StudentResultObject("Amy","K",3,2,1)
	#studentObjectTest = StudentResultObject("Carl","K",1,4,7)
	

	#print(studentObjectTest.studentName)
	
	

if __name__ == "__main__": main()

