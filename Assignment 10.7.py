#Write a python script to print first N  odd natural numbers.
n = int(input( "Enter a number: "))
 
for num in range(2*n):
    if num%2 != 0:
        print (num)
