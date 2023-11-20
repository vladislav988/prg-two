
students = []
lectors = []
def average_rating_st(list, cours):
    summ = 0
    b = 0
    for i in list:
        if cours in i["courses_in_progress"]:
            for j in i["grades"][cours]:
                b += 1
                summ += j
    if b != 0:
        ar = summ / b
        print(f"средняя оценка студентов на курсе по {cours}: {ar}")
    else:
        print("оценок нет")
def average_rating_lc(list, cours):
    summ = 0
    b = 0
    for i in list:
        if cours in i["courses_attached"]:
            for j in i["grades"][cours]:
                b += 1
                summ += j
    if b != 0:
        ar = summ / b
        print(f"средняя оценка лекторов на курсе по {cours}: {ar}")
    else:
        print("оценок нет")
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        params = [{"name":self.name, "surname": self.surname,"courses_in_progress": self.courses_in_progress, "grades": self.grades }]
        global students
        students += params
    def rate_hw(self, lector, course, grade):
        if course in lector.courses_attached and course in self.courses_in_progress :
            if course in lector.grades:
                lector.grades[course] += [grade]
                # for i in lectors:
                #     if i.name == lector.name and i.surname == lector.surname:
                #         lectors[i] = lector
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        a = 0
        summ = 0
        b = 0
        courses = ""
        for i in self.grades:
            if b > 0:
                courses += ", "
            b += 1
            courses += i
            for g in self.grades[i]:
                a += 1
                summ += g
        if a != 0:
            ac = summ / a
        else:
            ac = "оценок нет"
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {ac}
Курсы в процессе изучения: {courses}
"""




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname



class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]

        else:
            return 'Ошибка'

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}"""



class Lector(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}
        self.courses_attached = []
        params = [{"name": self.name, "surname": self.surname, "courses_attached": self.courses_attached,
                  "grades": self.grades}]
        global lectors
        lectors += params




    def __str__(self):
        a = 0
        summ = 0

        courses = ""
        for i in self.grades:

            for g in self.grades[i]:
                a += 1
                summ += g
        ac = summ / a

        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {ac}"""




mentor = Mentor("Vlad", "Somoylov")

rev1 = Reviewer("Danil", "Turilin")

rev2 = Reviewer("Vladimer", "Romanov")

student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['C#']

student2 = Student('Konstantin', 'Vinogradov', 'your_gender')
student2.courses_in_progress += ['C#']
student2.courses_in_progress += ['Python']



lector1 = Lector('Some', 'Buddy')
lector1.courses_attached += ['C#']

lector2 = Lector('Valentin', 'Akimov')
lector2.courses_attached += ['Python']
lector2.courses_attached += ['C#']

rev1.rate_hw(student1, "Python", 8)
rev1.rate_hw(student1, "C#", 8)
rev1.rate_hw(student2, "C#", 9)
rev1.rate_hw(student2, "Python", 9)


rev2.rate_hw(student1, "Python", 9)
rev2.rate_hw(student1, "C#", 9)
rev2.rate_hw(student2, "Python", 10)
rev2.rate_hw(student2, "C#", 7)


student1.rate_hw(lector1, 'Python', 8)
student1.rate_hw(lector1, 'Python', 10)
student1.rate_hw(lector1, 'C#', 10)
student2.rate_hw(lector2, 'Python', 9)
student2.rate_hw(lector2, 'C#', 7)


print(student2)
print(student1)

print(lector1)
print(lector2)
print(rev1)
print(rev2)
average_rating_st(students, "C#")
average_rating_st(students, "Python")
average_rating_lc(lectors, "C#")
average_rating_lc(lectors, "Python")

# хорошей работы)