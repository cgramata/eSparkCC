import csv


def importFiles():
	listOfRows = []
	domainFile = open("domain_order.csv")
	scoresFiles = open("student_tests.csv")

	domainFileReader = csv.reader(domainFile, delimiter=',')

	for row in domainFileReader:
		listOfRows.append(row)

	domainFile.close()

	return (listOfRows)


def storeDomainValues(domainReader, aDictionary):
	localDomainDictionary = aDictionary
	localDomainFileReader = domainReader

	for row in localDomainFileReader:
		row = filter(None, row)
		localDomainDictionary[row[0]] = row[1:]


def main():
	domainDictionary = {} 

	domainFileReaderMain = importFiles()
	storeDomainValues(domainFileReaderMain, domainDictionary)

	print(domainDictionary)

if __name__ == "__main__": main()