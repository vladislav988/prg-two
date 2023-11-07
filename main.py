class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_hw(self, lector, course, grade):
        if course in lector.courses_attached and course in self.courses_in_progress :
            if course in lector.grades:
                lector.grades[course] += [grade]
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
        ac = summ / a
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
student1.rate_hw(lector1, 'C#', 7)
student2.rate_hw(lector2, 'Python', 8)
student2.rate_hw(lector2, 'C#', 9)


print(student2)
print(student1)

print(lector1)
print(lector2)
print(rev1)
print(rev2)