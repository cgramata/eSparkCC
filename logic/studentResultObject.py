class StudentResultObject:
    def __init__(self, name, studentScoreList):
        self.studentName = name
        self.RF = studentScoreList[0]
        self.RL = studentScoreList[1]
        self.RI = studentScoreList[2]
        self.L = studentScoreList[len(studentScoreList) - 1]
