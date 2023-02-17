#Write a python script to display all prime numbers within a range.
# range
#start = 15
#end = 45

for val in range(15, 43):
  if val > 1:
    for i in range(2, val):
      if (val % i) == 0:
        break
    else:
      print(val, end=" ")
