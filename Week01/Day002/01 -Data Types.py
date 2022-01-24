# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#My code
#num1 = two_digit_number[0]
#num2 = two_digit_number[1]
#str1 = int(num1) + int(num2)
#num3 = str(str1)

#print(num1 + ' + ' + num2 + ' = ' + num3)
#print(num3)


#Instructors code, combined "str1" with "num1" and "num2"
# Also, the instructor did not print out the equation (3 + 5 = 8), only the result

num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])
num3 = num1 + num2

print(str(num1) + ' + ' + str(num2) + ' = ' + str(num3))
print(num3)