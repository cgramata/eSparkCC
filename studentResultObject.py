class StudentResultObject:

	def __init__(self, name, aList):
		self.studentName = name
		self.RF = aList[0]
		self.RL = aList[1]
		self.RI = aList[2]
		self.L = aList[len(aList)-1]
