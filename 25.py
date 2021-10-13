num = int(input("Enter a number: ")) 

sum = 0
n=num
while(num > 0):
    sum += num
    num -= 1

print("The sum of first",n , "natural numbers is: ", sum)