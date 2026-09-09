class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {} # {bangla: teacher_object}
        self.classrooms = {} # {eight: classroom_object}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        className = student.classrooms.name
        self.classrooms[className].add_student(student)

    @staticmethod
    def calculate_grade(marks):
        if marks >= 80 and marks <= 100:
            return 'A+'
        elif marks >= 70 and marks < 80:
            return 'A'
        elif marks >= 60 and marks < 70:
            return 'A-'
        elif marks >= 50 and marks < 60:
            return 'B'
        elif marks >= 40 and marks < 50:
            return 'C'
        elif marks >= 33 and marks < 40:
            return 'D'
        else:
            return 'F'

    @staticmethod
    def grade_to_value(grade):
        grade_values = {
            'A+': 5.0,
            'A': 4.0,
            'A-': 3.5,
            'B': 3.0,
            'C': 2.0,
            'D': 1.0,
            'F': 0.0
        }
        return grade_values[grade]

    @staticmethod
    def value_to_grade(value):
        if value >= 4.5 and value <= 5.0:
            return 'A+'
        elif value >= 3.5 and value < 4.5:
            return 'A'
        elif value >= 3.0 and value < 3.5:
            return 'A-'
        elif value >= 2.5 and value < 3.0:
            return 'B'
        elif value >= 2.0 and value < 2.5:
            return 'C'
        elif value >= 1.0 and value < 2.0:
            return 'D'
        else:
            return 'F'

    def __repr__(self):
        pass
        # all classrooms
        for key in self.classrooms.keys():
            print(key)

        # all students
        print("========== ALL Students ===========")
        result = ''
        for key, value in self.classrooms.items():
            result += f'----{key.upper()} Classroom Students\n'
            for student in value.students:
                result += f"{student.name}\n"

        print(result)

        # all subjects
        subject = ''
        for key, value in self.classrooms.items():
            subject += f'----{key.upper()} Classroom Subjects\n'
            for sub in value.subjects:
                subject += f"{sub.name}\n"

        print(subject)

        # all teachers


        # all student results
        print("======= Students Results =======")
        for key,value in self.classrooms.items():
            for student in value.students:
                for k,i in student.marks.items():
                    print(student.name, k, i, student.subject_grade[k])
                print(student.final_grade())
                
        return ''