from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom

school = School('ABC', 'Dhaka')

# add class
eight = ClassRoom('Eight')
nine = ClassRoom('Nine')
ten = ClassRoom('Ten')

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# add student
rahim = Student("Rahim", eight)
karim = Student("karim", nine)
fahim = Student("fahim", ten)
hamim = Student("hamim", eight)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(fahim)
school.student_admission(hamim)

# add teacher
abul = Teacher("Abul Khan")
babul = Teacher("Babul Khan")
dabul = Teacher("Dabul Khan")
kabul = Teacher("Kabul Khan")

# adding subjects
bangla = Subject('Bangla', abul)
physics = Subject('Physics', babul)
chemistry = Subject('Chemistry', dabul)
biology = Subject('Biology', kabul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
eight.add_subject(biology)

nine.add_subject(bangla)
nine.add_subject(physics)
nine.add_subject(chemistry)
nine.add_subject(biology)

ten.add_subject(bangla)
ten.add_subject(physics)
ten.add_subject(chemistry)
ten.add_subject(biology)


eight.take_semester_exam()
nine.take_semester_exam()
ten.take_semester_exam()
print(school)