""""
x = [5,10,15,20]
x.append(400)
x.insert(3,200)
i=x.index(20)
x[i]=0
print(x)




first = int(input("enter the first number"))
second = int(input("enter the second number"))

if first>second:
    print("first is greater than second")
else:
    print("second is greater than first")



a= list(range(1,6))
print (a)

for i in range(1,6):
    print(i)

a = list(range(0,100,2))
print(a)



number = 23

first_guess = int(input("guess the first number"))
while first_guess == number:
    if first_guess==number:
        print("consrts")
    elif first_guess>number:
        print("guess a lower number")
        second = int(input("second"))
    



import random

a=random.randint(1,10)
print(a)



first_number =int(input("enter number 1"))
second_number =int(input("enter number 2"))
third_number =int(input("enter number 3"))

print("largest number is ",max(first_number,second_number,third_number))
print("smallest number is ",min(first_number,second_number,third_number))




# do as a list
total = 0 
for first_number in range(1,11):
    first_number =int(input("enter a number "))
    total += first_number

print(total)

"""

Months = {
    'January' : 31,
    'February' : 28,
    'March' : 31,
    'April' : 30,
    'May' : 30,
    'June' : 31,
    'July' : 30,
    'August' : 31,
    'September' : 30,
    'October' : 31,
    'November' : 30,
    'December' : 31,
}

month = input()
print(Months(month))