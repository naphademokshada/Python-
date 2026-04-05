#update method

student = {
    "name" : "Mokshada Naphade",

    "subject" : {
        "physics" : 80,
        "chemistry" : 90,
        "maths" : 95
    }
}

student.update({"city" : "Pune"})
print(student)


#2nd method

new_dict = {"city" : "Pune"}
new_dict = {"name" : "Mokshada"}
student.update(new_dict)
print(student)