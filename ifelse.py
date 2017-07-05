#!usr/bin/python

# this is an example for if else condition

shoes = ["Nike","Adidas","Converse","Reebok","Puma"]

order = input("WHOHO!!!Please enter a brand.\n")
if order in shoes:
 print("We have  it on stock\n " "Please walkin to the store!! \n we have the best people over there to guide you!")
else:
 print("Sorry,but "+order+" is out of stock")