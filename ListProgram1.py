#WAP to ask the user to enter names of their 3 favourite movies & store them in a list
#1st Method
movie1 = input("Enter First Movie Name: ")
movie2 = input("Enter Second Movie Name: ")
movie3 = input("Enter Third Movie Name: ")

list= [movie1,movie2,movie3]
print("Your Favourite Movie List Is:",list)

#2nd Method
movies=[]
mov1 = input("Enter First Movie Name: ")
mov2 = input("Enter Second Movie Name: ")
mov3 = input("Enter Third Movie Name: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print("Your Favourite Movie List Is:",movies)

#3rd Method
movies = []
mov = input("Enter Movie Name: ")
movies.append(mov)
mov = input("Enter Movie Name: ")
movies.append(mov)
mov = input("Enter Movie Name: ")
movies.append(mov)

print("Your Favourite Movie List Is:",movies)

#4th Method

movies = []
movies.append(input("Enter Movie Name: "))
movies.append(input("Enter Movie Name: "))
movies.append(input("Enter Movie Name: "))
print("Your Favourite Movie List Is:",movies)
