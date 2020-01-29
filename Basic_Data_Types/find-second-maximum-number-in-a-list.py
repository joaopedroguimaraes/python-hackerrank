if __name__ == '__main__':
	students = []
	scores = []
	for _ in range(int(input())):
		name = input()
		score = float(input())
		students.append([name, score])
		if score not in scores:
			scores.append(score)

	second_lowest_score = sorted(scores)[1]
	students_with_second_lowest_score = sorted([student[0] for student in students if student[1] == second_lowest_score])
	for student_name in students_with_second_lowest_score:
		print(student_name)
