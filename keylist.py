#!/usr/bin/python
#Anne-Marie Smith
#From the kwlist library sort the list in alphabetic order and print the words
#in 5 different column and pad the words so they are all starting at the 
#same place and have 2 space appart minimum.

from keyword import kwlist

key1 = kwlist
key1.sort(key=str.casefold)
size = len(max(key1, key=len))
for index, item in enumerate(key1):
    if (index + 1) % 5 == 0:
        print(item.rjust(size + 2))
    else:
        print(item.rjust(size + 2), end=" ")
    
