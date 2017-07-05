#!usr/bin/python

# This is an example program for range() function

x = 20
total=0
for num in range(1,x+1):
  total = total+num
print("sum of 1 up to %d:%d" %(x,total))
