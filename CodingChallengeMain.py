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


def storeDomainValues(domainList, scoreTestList, aDictionary, bDictionary):
	localDomainDictionary = aDictionary
	localTestScoreDictionary = bDictionary
	localDomainFileList = domainList
	localTestScoreFileList = scoreTestList

	for row in localDomainFileList:
		row = filter(None, row)
		localDomainDictionary[row[0]] = row[1:]

	for row in localTestScoreFileList:
		row = filter(None, row)
		localTestScoreDictionary[row[0]] = row[1:]


def main():
	domainDictionary = {}
	testScoreDictionary = {}

	domainFileReaderMain, testScoresReaderMain = importFiles()
	storeDomainValues(domainFileReaderMain, testScoresReaderMain, domainDictionary, testScoreDictionary)

	print(domainDictionary)
	print(testScoreDictionary)

if __name__ == "__main__": main()