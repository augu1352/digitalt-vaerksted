class Student:
    def __init__(self, studentKey, studentName):
        self.studentKey = studentKey
        self.studentName = studentName

    def get_key(self):
        return self.key

    def set_key(self, newKey):
        self.key = newKey

    def get_name(self):
        return self.studentName

    def set_name(self, newStudentName):
        self.studentName = newStudentName
