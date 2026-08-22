# [3,10,15,54,75,25,23] print num divisible by 3,5,8 if none print none


# numbers = [3, 10, 15, 54, 75, 25, 23]

# for num in numbers:
#     if num % 3 == 0 or num % 5 == 0 or num % 8 == 0:
#         print(num)
#     else:
#         print("None")
        
        
# [10,3,5,6,7,8,9,24,3,5,6,7,78]  find the smallest and largest elements in the swap them


# numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 78]

# smallest = min(numbers)
# largest = max(numbers)

# small_index = numbers.index(smallest)
# large_index = numbers.index(largest)

# numbers[small_index], numbers[large_index] = numbers[large_index], numbers[small_index]

# print(numbers)


# [-1,3,34,-8,-91]replace -1 by 100

# numbers = [-1, 3, 34, -8, -91]

# numbers[0] = 100

# print(numbers)


# [1,2,3,4] 
# [3,4,5,6]
# find the average of 2 list
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# avg1 = sum(list1) / len(list1)
# avg2 = sum(list2) / len(list2)

# print("Average of list 1:", avg1)
# print("Average of list 2:", avg2)

# take the number as input and add 5 it if it is divisible by 3 

# num = int(input("Enter a number: "))

# if num % 3 == 0:
#     num = num + 5
#     print(num)
# else:
#     print(num)

# [3,10,15,54,75,25,23] print num divisible by 3 but not 5

# numbers = [3, 10, 15, 54, 75, 25, 23]

# for num in numbers:
#     if num % 3 == 0 and num % 5 != 0:
#         print(num)


# [10,3,5,6,7,8,9,24,3,5,6,7,89] find the elements grater than 20

# numbers = [10,3,5,6,7,8,9,24,3,5,6,7,89]

# for num in numbers:
#     if num > 20:
#         print(num)

# [-1,3,34,-8,-9,1] print only negetive numbers

# numbers = [-1, 3, 34, -8, -9, 1]

# for num in numbers:
#     if num < 0:
#         print(num)

# [1,2,3,4,5,6,7,8,9]
# find the count of list

# numbers = [1,2,3,4,5,6,7,8,9]

# print(len(numbers))

# take the as input and multiply 5 it if it is divisible by  

# num = int(input("Enter a number: "))

# if num % 3 == 0:
#     print(num * 5)
# else:
#     print(num)

# take a 2 num as input from user and 
# check wheather the sum is divisible by 5

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# sum = num1 + num2

# if sum % 5 == 0:
#     print("The sum is divisible by 5")
# else:
#     print("The sum is not divisible by 5")

# [10,3,5,6,7,8,9,24,3,5,6,7,89] find prime numbers

# numbers = [10,3,5,6,7,8,9,24,3,5,6,7,89]

# for num in numbers:
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

# [-1,3,34,-8,-9,1] perform list operation

# numbers = [-1, 3, 34, -8, -9, 1]

# print("List:", numbers)
# print("Length:", len(numbers))
# print("Smallest:", min(numbers))
# print("Largest:", max(numbers))
# print("Sum:", sum(numbers))
# print("Sorted:", sorted(numbers))
# print("Reversed:", numbers[::-1])

# [1,2,3,4,5,6,7,8,9]
# find the average of list

# numbers = [1,2,3,4,5,6,7,8,9]

# average = sum(numbers) / len(numbers)

# print("Average:", average)

# take the divisiors from 1to 10 and check 1578693 is divisible or not 
# if divisible create list of divisiors that divide it

# num = 1578693
# divisors = []

# for i in range(1, 11):
#     if num % i == 0:
#         divisors.append(i)

# print("Divisors:", divisors)


# take a 2 num as input from user and if it divisible by 5
# square the number

# num = int(input("Enter a number: "))

# if num % 5 == 0:
#     print("Square:", num * num)
# else:
#     print("Number is not divisible by 5")

# [10,3,5,6,7,8,9,24,3,5,6,7,89] 
# find the prime numbers, even numbers and odd numbers 

# numbers = [10, 3, 5, 6, 7, 8, 9, 24, 3, 5, 6, 7, 89]

# prime = []
# even = []
# odd = []

# for num in numbers:
#     # Check even/odd
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

#     # Check prime
#     if num > 1:
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break

#         if is_prime:
#             prime.append(num)

# print("Prime numbers:", prime)
# print("Even numbers:", even)
# print("Odd numbers:", odd)

# [-1,3,34,-8,-9,1] remove negative numbers and numbers divisible by 3

# numbers = [-1, 3, 34, -8, -9, 1]

# new_list = []

# for num in numbers:
#     if num >= 0 and num % 3 != 0:
#         new_list.append(num)

# print(new_list)

# [1,2,3,,4,5,6,7,8,9]
# find the average sum,count of list

# numbers = [1,2,3,4,5,6,7,8,9]

# total = sum(numbers)
# count = len(numbers)
# average = total / count

# print("Sum:", total)
# print("Count:", count)
# print("Average:", average)

# take the divisiors from 1 to 10 and check 1578693 is divisible
# or not if divisible -100 from it

# num = 1578693

# for i in range(1, 11):
#     if num % i == 0:
#         print(num, "is divisible by", i)
#         print("After subtracting 100:", num - 100)
#     else:
#         print(num, "is not divisible by", i)

# "university" count  vowels in it 

# s = "university"
# count = 0

# for ch in s:
#     if ch in "aeiou":
#         count += 1

# print("Number of vowels:", count)

# [10,3,5,6,7,8,9,24,3,5,6,7,89]
# PRINT 89 USING INDEX AND ADD 59 TO THE LIST IN 9TH index

# numbers = [10,3,5,6,7,8,9,24,3,5,6,7,89]

# # Print 89 using index
# print(numbers[12])

# # Add 59 at 9th index
# numbers.insert(9, 59)

# print(numbers)

# [-1,3,34,-8,-9,1] square elements of the list

# numbers = [-1, 3, 34, -8, -9, 1]

# for i in numbers:
#     print(i ** 2)
    
# take a 2 numbers as input and 2 fioor division     
    
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# result = a // b

# print("Floor division:", result)    

# [10,3,5,6,7,8,9,24,3,5,6,7,897,8,54,621,57,24,3,5,6,4]
# find qnique values