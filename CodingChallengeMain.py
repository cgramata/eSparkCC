import csv


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


def storeFileValues(domainList, scoreTestList, aDictionary, bDictionary, listOfNames, testScoresLayout):
	localDomainDictionary = aDictionary
	localTestScoreDictionary = bDictionary
	localDomainFileList = domainList
	localTestScoreFileList = scoreTestList
	localListOfNames = listOfNames
	localScoresLayout = testScoresLayout

	for row in localDomainFileList:
		row = filter(None, row)
		localDomainDictionary[row[0]] = row[1:]

	for row in localTestScoreFileList[1:]:
		row = filter(None, row)
		localTestScoreDictionary[row[0]] = row[1:]
		localListOfNames.append(row[0])

	localScoresLayout.append(localTestScoreFileList[0][1:])


def main():
	domainDictionary = {}
	testScoreDictionary = {}
	listOfStudentNames = []
	layoutOfScores = []


	domainFileReaderMain, testScoresReaderMain = importFiles()
	storeFileValues(domainFileReaderMain, testScoresReaderMain, domainDictionary, testScoreDictionary, listOfStudentNames, layoutOfScores)

	
	print(listOfStudentNames)
	print
	print(layoutOfScores)
	print
	print(domainDictionary)
	print
	print(testScoreDictionary)

if __name__ == "__main__": main()