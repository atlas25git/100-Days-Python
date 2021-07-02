numbers = [1,2,3]
new_list = [n**7 for n in numbers]
print(new_list)

#this could also be used for strings or other containers

numbers = [1,2,3]
new_list = [n**7 for n in numbers if n!=2]
print(new_list)

#dictionaries
import random
names = ["A","B","c","D"]
student_score={
    student:random.randint(1,100) for student in names
}

print(student_score)

passed = {student:score for (student,score) in student_score.items() if score>=60 }
print(passed)
#