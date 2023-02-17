#Write a python script to print first N even natural numbers.
n = int(input( "Enter a number: "))
 
for num in range(2,n*2+1):
    if num%2 ==0:
        print (num)
