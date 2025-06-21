class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average = 0

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        sum = 0
        count = 0
        for course_f in lecturer.grades.items():
            for grade_f in list(course_f[1]):
                sum += grade_f
                count += 1
        lecturer.average = sum / count
    
    def get_average_by_course(self, course): #average grade of 1 student for current course
        for grade in self.grades.items():
            if (grade[0] in course):
                count = 0
                average_mark_for_current_grade = 0
                for mark in grade[1]:
                    average_mark_for_current_grade += mark
                    count +=1
        # print(average_mark_for_current_grade / count)
        return average_mark_for_current_grade / count


    
    def __len__(self):
        return len(self.finished_courses)
    

    def __lt__(self, other):
        return self.average < other.average
       
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average}\n\
Курсы в процессе изучения: {(', ').join(self.courses_in_progress)}\nЗавершенные курсы: {(', ').join(self.finished_courses)}"


def average_grade(students_list, course):
    summa = 0
    count = 0
    for student in students_list:
        if(course in student.courses_in_progress):
            # print(student.get_average(course))
            summa += student.get_average_by_course(course)
            count += 1
            #print(count, summa)
    return (summa/count)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        self.average = 0

    def get_average_by_course(self, course): #average grade of 1 lecturer for current course
        for grade in self.grades.items():
            if (grade[0] in course):
                count = 0
                average_mark_for_current_grade = 0
                for mark in grade[1]:
                    average_mark_for_current_grade += mark
                    count +=1
        # print(average_mark_for_current_grade / count)
        return average_mark_for_current_grade / count

    def __lt__(self, other):
        return self.average < other.average
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average}"


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        sum = 0
        count = 0
        for course_f in student.grades.items():
            for grade_f in list(course_f[1]):
                sum += grade_f
                count += 1
        student.average = sum / count
        
        
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"    

def average_grade_lecturer(lecturer_list, course):
    summa = 0
    count = 0
    for lecturer in lecturer_list:
        if(course in lecturer.courses_attached):
            summa += lecturer.get_average_by_course(course)
            count += 1
            #print(count, summa)
    return (summa/count)


lecturer = Lecturer('Иван', 'Иванов')
lecturer1 = Lecturer('Ива', 'Иван')

reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')
student1 = Student('Алёхa', 'Олa', 'M')
 
student.courses_in_progress += ['Python', 'C++']
student.finished_courses += ['C++']
student1.courses_in_progress += ['Python', 'C++']
student1.finished_courses += ['C++']

lecturer.courses_attached += ['Python', 'C++']
lecturer1.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']
 
student.rate_lecture(lecturer, 'Python', 10)   
student.rate_lecture(lecturer, 'C++', 8)
student.rate_lecture(lecturer1, 'Python', 1)   
student.rate_lecture(lecturer1, 'C++', 2)
reviewer.rate_hw(student, 'C++', 8)
reviewer.rate_hw(student, 'C++', 2)
reviewer.rate_hw(student, 'Python', 2)

reviewer.rate_hw(student1, 'C++', 8)
reviewer.rate_hw(student1, 'C++', 10)
reviewer.rate_hw(student1, 'Python', 2)

# if(student < student1):
#     print('1 хуже 2')  
# else:
#     print('1 лучше 2')  

# if(lecturer < lecturer1):
#     print('1 хуже 2')  
# else:
#     print('1 лучше 2')  


# print(reviewer)
# print(lecturer)
# print(lecturer1)
# print(student)
student_list = [student, student1]
print(average_grade(student_list, 'C++'))

lecturer_list = [lecturer, lecturer1]
print(average_grade_lecturer(lecturer_list, 'C++'))


