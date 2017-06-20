def importFiles():
	domainFile = open("domain_order.csv")
	scoresFiles = open("student_tests.csv")

	for row in domainFile:
		print(row)

	domainFile.close()


def main():
	importFiles()

if __name__ == "__main__": main()