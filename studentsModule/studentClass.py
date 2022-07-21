import io

class Student:

    Scores = {}

    # initializing the constructor method
    
    def __init__(self, name, grade):
        name = name
        grade = grade

    def getScores(self):

        answer_key = []
        # read ("NOTE: READ") into answer_key list, the answer key from file answers.txt
        try:
            answer_key = [line.strip() for line in open("answers.txt", 'w')]
        except FileNotFoundError as f:
            print(f)
        except io.UnsupportedOperation as i:
            print(i)

       
        student_answers = []
        # read ("NOTE: READ") into student_answers list, student answers from file data.txt
        try: 
            student_answers = [line.strip().split(',') for line in open("data.txt", 'w')]
        except FileNotFoundError as f:
            print(f)
        except io.UnsupportedOperation as i:
            print(i)

        total_score = 100

        length = len(answer_key) + 1
        
        for index in range(student_answers):
            student_record = student_answers[index]
            i = 1
            if(self.name == student_record[0]):
                while( i < length):
                    if(answer_key[i - 1] != student_record[i]):
                        total_score -= 10
                    i += 1
        
        Scores[getName()] = total_score

    def getName(self):
        return self.name
    
    def getOldScore(self):
        return self.grade
    
    def getAverage(self):
        oldGrade = self.grade
        newGrade = Scores[getName()]
        average = (oldGrade + newGrade)/2.0
        return average
    
    def getRange(self):
        oldGrade = self.grade
        newGrade = Scores[getName()]
        range = abs(oldGrade - newGrade)
        return range


    @staticmethod
    def sortDict():
        return sorted(Scores.items())

    #---end of the class definition#