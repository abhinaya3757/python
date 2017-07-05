#!usr/bin/python

# This is an example for nested if statement

letter = ["A","B","C","D","E"]
words = ["ABC","DEF","GHI","JKL","IJQ"]
search = input("Please enter the alphabet: \n -->>")
if search in letter:
   print(" You have searched for: " +search+ "\n We have found the search result as letter")
elif search in words:
   print(" you searched for: " +search+ "\n We have found your search result as words")
else:
   print ("Sorry, We couldn't found your search. Please try again with another word")

