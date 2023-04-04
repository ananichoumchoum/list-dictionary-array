#Annemarie smith
#ITSC203
# how to sort a list where the first value is always the name and second one username in the directory
from prettytable import PrettyTable
x = PrettyTable()

mylist = ('kenny rogers', 'home/users/KRogers',
         'tony robbins', 'home/users/TRobbins',
         'johnny cash', 'home/users/JCash',
         'tito jackson', 'home/users/TJackson',
         'tim tzuyu', 'home/users/TTzuyu',
         'kareena kapoor', 'home/users/KKapoor')
          
odd_i = []
even_i = []
for i in range(len(mylist)):
    if i % 2:
        odd_i.append(mylist[i])
    else :
        even_i.append(mylist[i])
print("\n+-------------------------------------------+")
print("|  ",even_i[0].title(),"  |  ",odd_i[0],"  |") 
print("|  ",even_i[1].title(),"  |  ",odd_i[1]," |") 
print("|  ",even_i[2].title(),"   |  ",odd_i[2],"    |") 
print("|  ",even_i[3].title(),"  |  ",odd_i[3]," |") 
print("|  ",even_i[4].title(),"     |  ",odd_i[4],"   |") 
print("|  ",even_i[5].title(),"|  ",odd_i[5],"  |") 
print("+-------------------------------------------+")     

#now try and only print the name and username using prettytable
x.field_names = ['Name','Username']
username = []
for i in range(len(odd_i)):
    splits = (odd_i[i].split('/'))
    username.append(splits[2])
    #using title to change the first letter of the word for capital
    x.add_row([even_i[i].title(), username[i]])
print(x)
