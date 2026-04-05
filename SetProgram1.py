#You are given a list of subjects for students.Assume one classroom is required for 1 subject.How many classrooms are needed by all students
"python","java","c++","python","javascript","java","python","java","c++","c"

# we used set because it doesnt take duplicate values and we need only unique subjects to calculate the number of classrooms required

set = {"python","java","c++","python","javascript","java","python","java","c++","c"}
print("Classrooms Required:", len(set)) # 5 because duplicate values are ignored
