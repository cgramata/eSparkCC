import csv


class ImportExportData:
    def importDomainFile(self):
        listOfDomainRows = []

        try:
            domainFile = open("../csvFiles/domain_order.csv")
        except IOError:
            print("Domain file not found, make sure the file is in the directory")
        else:
            with domainFile:
                domainFileReader = csv.reader(domainFile, delimiter=",")
                for row in domainFileReader:
                    listOfDomainRows.append(row)

        return listOfDomainRows

    def importStudentTestFile(self):
        listOfTestScoreRows = []

        try:
            scoresFile = open("../csvFiles/student_tests.csv")
        except IOError:
            print("Student test file not found, make sure the file is in the directory")
        else:
            with scoresFile:
                scoresFileReader = csv.reader(scoresFile, delimiter=",")
                for row in scoresFileReader:
                    listOfTestScoreRows.append(row)

        return listOfTestScoreRows

    #creates the final curriculum file in csvFiles Folder
    def writeCurriculumForStudent(self, finalCurriculumList):

        with open("../csvFiles/resultingStudentCurriculum.csv", "w") as studentCurriculum:
            writer = csv.writer(studentCurriculum)
            writer.writerows(finalCurriculumList)