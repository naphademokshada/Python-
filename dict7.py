#.get method

student = {
    "name" : "Mokshada Naphade",

    "subject" : {
        "physics" : 80,
        "chemistry" : 90,
        "maths" : 95
    }
}

#print(student['name2'])#error
print(student.get('name2'))  # Returns None instead of raising an error
print(student.get('name')) 