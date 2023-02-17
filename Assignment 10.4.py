#Write a python script to print the first 10 multiples of N in reverse order.
N = int(input( " Enter a number: "))

for i in range (1,11):
    x = N*i
    
print(str(x)[::-1])
