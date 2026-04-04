#Slicing

str = "Talegaondabhade"

# T=0, a=1, l=2, e=3, g=4, a=5, o=6, n=7, d=8, a=9, b=10, h=11, a=12, d=13, e=14

print(str[1:4])
print(str[5:10])
print(str[0:15])
print(str[:10]) # from start to 9
print(str[5:]) # from 5 to end

print(str[5:len(str)]) # from 5 to end of string