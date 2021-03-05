class objdict:
    def __init__(self):
        self.name = 'Sudhamshu'
        self.initial = 'B N'
        self.program = 'ECE'
        self.degree = 'BE'
        self.college = 'DSCE'
        self.cgpa = '8.67'
    def pass_method(self):
        pass

print(objdict().__dict__)
