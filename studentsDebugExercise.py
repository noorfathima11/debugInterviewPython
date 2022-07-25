from studentsModule import studentClass
Student= studentClass.Student


student_objs = [
        Student('Sammy Student',65),
        Student('Betty Sanchez', 45),
        Student('Alice Brown', 100),
        Student('Tom Schulz', 50),
        Student('Noor Fathima', 90)
]


average_grade = 0
average_range = 0
student_record = {}
student_old_score = []
student_average_grade = []

for index in student_objs:
        index.getScores()
        oldScore = index.getOldScore()
        name = index.getName()
        avg = index.getAverage()
        avg_range = index.getRange()
        student_record[index.name] = {"oldScore": oldScore }
        student_record[index.name]["avg"] = avg
        student_record[index.name]["avg_range"] = avg_range
        average_grade += avg
        average_range += avg_range

average_grade = average_grade / 5.0
average_range = average_range / 5.0

sortList = studentClass.Student.sortDict()

for k, v in sortList:
        record = student_record[k]
        print(k + " has old score: " + str(record["oldScore"]))
        print(k + " has new score: " + str(v))
        print("Average grade: " + str(record["avg"]))
        print("Grade Range: " + str(record["avg_range"]))
        print("\n")


print("Overall Average Grade: " + str(average_grade))
print("Overall Average Grade Range: " + str(average_range))

