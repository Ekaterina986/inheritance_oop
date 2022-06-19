class Student:
	def __init__ (self, name, surname,gender):
		self.name = name
		self.surname = surname
		self.gender = gender
		self.finished_courses = []
		self.courses_in_progress = []
		self.grades = {}

# оценка лектора	

	def rate_lecturer(self, lecturer, course, grade):
		if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
			if course in lecturer.grades_lecturer:
	 			lecturer.grades_lecturer[course] += [grade]
			else:
				lecturer.grades_lecturer[course] = [grade]
		else:
			return 'Ошибка'

# расчет средней оценки
	def count_average(self):
		summa = 0
		count = 0
		for grades in self.grades.values():
			for grade in grades:
				summa += grade
				count += 1
		if count == 0:
			return 'Пока нет оценок'
		return summa / count

# сравнить студентов по средней оценке

	def __lt__(self, foe):
		if not isinstance(foe, Student):
			print('Нет такого студента')
			return
		return self.count_average() < foe.count_average()

# метод str

	def __str__(self):
		finish_str = ', '.join(self.finished_courses)
		progress_str = ', '.join(self.courses_in_progress)
		res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.count_average()}\nКурсы в процессе изучения: {progress_str}\nЗавершенные курсы: {finish_str}'
		return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
	def __init__(self,name, surname):
		super().__init__(name, surname)
		self.grades_lecturer = {}

# расчет средней оценки

	def count_average(self):
		summa = 0
		count = 0

		for grades in self.grades_lecturer.values():
			for grade in grades:
				summa += grade
				count += 1
		if count == 0:
			return 'Пока нет оценок'
		return summa / count

# сравнить лекторов по средней оценке

	def __lt__(self, foe):
		if not isinstance(foe, Lecturer):
			print('Нет такого лектора')
			return
		return self.count_average() < foe.count_average()

# метод str 
	def __str__(self):
		res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.count_average()}'
		return res



class Reviewer(Mentor):

# оценка студента

	def rate_student(self, student, course, grade):
		if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
			if course in student.grades:
				student.grades[course] += [grade]
			else:
				student.grades[course] = [grade]
		else:
			return 'Ошибка'

# метод str 

	def __str__(self):
		res = f'Имя: {self.name}\nФамилия: {self.surname}'
		return res

cool_lecturer = Lecturer('Sherlock', 'Holmes')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['C++']

best_lecturer = Lecturer('Hercule', 'Poirot')
best_lecturer.courses_attached += ['JS']
best_lecturer.courses_attached += ['C++']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['C++']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['JS']
best_student.finished_courses += ['C++']

best_student.rate_lecturer(cool_lecturer, 'Python',10)
best_student.rate_lecturer(cool_lecturer, 'JS',8)
best_student.rate_lecturer(cool_lecturer, 'C++',9)

best_student.rate_lecturer(best_lecturer, 'Python',10)
best_student.rate_lecturer(best_lecturer, 'JS',9)
best_student.rate_lecturer(best_lecturer, 'C++',10)

worst_student = Student('Oleg', 'Oleg', 'your_gender')
worst_student.courses_in_progress += ['Python']
worst_student.courses_in_progress += ['Java']
worst_student.finished_courses += ['C++']

worst_student.rate_lecturer(cool_lecturer, 'Python',6)
worst_student.rate_lecturer(cool_lecturer, 'Python',6)
worst_student.rate_lecturer(cool_lecturer, 'C++',10)

cool_reviewer.rate_student(worst_student, 'Python', 4)
cool_reviewer.rate_student(worst_student, 'C++', 6)
cool_reviewer.rate_student(worst_student, 'Python', 8)
 
cool_reviewer.rate_student(best_student, 'Python', 10)
cool_reviewer.rate_student(best_student, 'C++', 6)
cool_reviewer.rate_student(best_student, 'Python', 8)

