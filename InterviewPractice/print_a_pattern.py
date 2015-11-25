
def run_main():
	
	student1 = [700,3]
	student2 = [600,4]
	student3 = [710,2]
	student4 = [750,1.5]

	students = [student1,student2,student3,student4]

	print_a_pattern(students)

def print_a_pattern(students):

	sat_scores = []
	gpa_scores = []
	oup =[]

	for student in students:
		sat_scores.append(student[0])
		gpa_scores.append(student[1])

	#print(sat_scores)
	#print(gpa_scores)

	for sat_score,gpa_score in zip(sat_scores,gpa_scores):
		print(sat_score)
		print(gpa_score)
		oup_dict ={min(sat_scores):max(gpa_scores)}
		oup.append(oup_dict)
		sat_scores.remove(min(sat_scores))
		gpa_scores.remove(max(gpa_scores))
	print(oup)

if __name__=="__main__":
	run_main()