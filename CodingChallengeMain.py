import csv


def importFiles():
	domainDictionary = {}

	domainFile = open("domain_order.csv")
	scoresFiles = open("student_tests.csv")

	domainFileReader = csv.reader(domainFile, delimiter=',')

	for row in domainFileReader:
		row = filter(None, row)
		storeDomainValues(row, domainDictionary)

	print(domainDictionary)

	domainFile.close()


def storeDomainValues(rowParam, aDictionary):
	localDomainDictionary = aDictionary

	localDomainDictionary[rowParam[0]] = rowParam[1:]



def main():

	importFiles()

if __name__ == "__main__": main()