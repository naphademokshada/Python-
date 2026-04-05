#Figure out a way to store 9 & 9.0 as seperate value in set.(you can take help to built-in data types)


values = {9,"9.0",8,"8.0"}
print(values)

# 2nd Solution
values = {
    ("float",9.0),
    ("int",9),
    ("float",8.0),
}
print(values)