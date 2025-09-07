# Q1 (a)
pima2D = [[6, 148, 72, 35],
          [1, 85, 66, 29],
          [8, 183, 64, 0],
          [1, 89, 66, 23],
          [0, 137, 40, 35],
          [5, 116, 74, 0],
          [3, 78, 50, 32],
          [10, 115, 0, 0],
          [2, 197, 70, 45],
          [8, 125, 96, 0],
          [4, 110, 92, 0],
          [10, 168, 74, 0],
          [10, 139, 80, 0],
          [1, 189, 60, 23],
          [5, 166, 72, 19],
          [7, 100, 0, 0]]

count = 0
total = 0

for row in pima2D:
    for number in row:
        if number != 0:
            total += number
            count += 1

average = total / count

print("Count is: ", count)
print("Total is: ", total)
print("Average is ", average)

# (b)
for x, row in enumerate(pima2D):
    for i, number in enumerate(row):
        if number == 0:
            pima2D[x][i] = round(average, 2)

# (c)
print(pima2D)

# Q2
import random


def random_num():
    randoms = random.randint(1, 100)
    print(randoms)


# main program
for randoms in range(10):
    random_num()


# Q3

def odd_num(num1):
    for num in range(int(num1) + 1):
        if num % 2 != 0:
            print(num)


# main program
user_input = input("Enter the limit of number: ")
odd_num(user_input)


# Q4

def longest_string(string1, string2):
    if len(string1) > len(string2):
        print("The string: ", string1, "is longer")
    else:
        print("The string: ", string2, "is longer")


# main program
user_input1 = input("Enter first string: ")
user_input2 = input("Enter second string: ")
longest_string(user_input1, user_input2)
