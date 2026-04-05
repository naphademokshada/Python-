#Search for a number x in this tuple using loop:
# linear search one by one finding (1,4,9,16,25,36,49,64,81,100)

tuple = (1,4,9,16,25,36,49,64,81,100)
x = 36

i = 0
while i < len(tuple):
    if tuple[i] == x:
        print("Number found at index ",i)
    else :
            print("Number not found at index ",i)
    i += 1

