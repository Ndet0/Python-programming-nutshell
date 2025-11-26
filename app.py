from teacher import Teacher

Teacher.create_table()

teacher= Teacher.create("peter", " principal")
teacher= Teacher("muturi", " principal")

print(teacher)

# teacher.save()

# print(teacher)