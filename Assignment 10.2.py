#Write a python script to print the first 10 multiples of N.

n = (input("Enter number: "))

print("The multiples are: ")
for i in range(1,11):
    print(n*i, end =" ")
