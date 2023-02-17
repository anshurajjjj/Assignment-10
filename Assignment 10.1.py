#Write a python script to print the first 10 multiples of 5.

n = int(input("Enter number: "))

print("The multiples are: ")
for i in range(1,11):
    print(n*i, end =" ")
