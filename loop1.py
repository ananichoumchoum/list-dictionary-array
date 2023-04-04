#Anne-Marie Smith

#Ask the user to enter a number between 0-10.
squaredNum = input("Enter a number between 0 and 10: ")
#verify that the number is between the range asked, if not ask te user to enter a number bett=ween 0-10 until they write the correct number
while int(squaredNum)>10 or int(squaredNum)<0:
    squaredNum = input("Enter a number between 0 and 10: ")
    
#for the index i in the range of 0 to the number chosen by the user ( +1 because loop start at 0)
for i in range(int(squaredNum) + 1):
    #square the number and print the loop number
    print(f"This is loop {i}, your number squared is:", i ** 2)
    
