grades = {
	"Math": 90,
	"Science": 88,
	"History": 78,
	"Economics": 90,
	"English": 76
}

def average_grade(grades):
	total = sum(grades.values())
	avg = total / len(grades)
	return avg
	
print("Avg Grade:", average_grade(grades))
