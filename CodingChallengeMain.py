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

	return (listOfDomainRows, listOfTestScoreRows)


def main():
	domainDictionary = {}
	domainGradeRange = []
	testScoreDictionary = {}
	listOfStudentNames = []
	layoutOfScores = []
	gradeRange = []

	testAssignment = CurriculumAssignment()
	domainFileReaderMain, testScoresReaderMain = importFiles()
	testAssignment.storeFileValues(domainFileReaderMain,testScoresReaderMain,domainDictionary,domainGradeRange,testScoreDictionary,listOfStudentNames,layoutOfScores)

	testingClass = CurrSize()
	studentObjectTest = StudentResultObject("Amy","K",3,2,1)
	studentObjectTest = StudentResultObject("Carl","K",1,4,7)
	

	print(studentObjectTest.studentName)
	

if __name__ == "__main__": main()