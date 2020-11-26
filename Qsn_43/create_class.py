class Attendence(object):
    def getAttendence(self):
        return "Unknown"

class Present(Attendence):
    def getAttendence(self):
        return "Present"

class Absent(Attendence):
    def getAttendence(self):
        return "Absent"

isPresent = Present()
isAbsent = Absent()
print(isPresent.getAttendence())
print(isAbsent.getAttendence())
