#WAP to  enter marks of 3 subjects from the user and store then in a dictionary.Start with an empty dictionary & add one by one. Use subject name as key & marks as value


marks=  {}

x=int(input("Enter Phy:"))
marks.update({"Phy" : x})


x=int(input("Enter Chem:"))
marks.update({"Chem" : x})

x=int(input("Enter Math:"))
marks.update({"Math" : x})

print(marks)

