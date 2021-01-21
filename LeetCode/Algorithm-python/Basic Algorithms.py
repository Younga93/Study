'''
Notion page: (Written in Korean)
https://www.notion.so/03c48355b59f42609cc6519c9d8e8442
'''

'''
Sum of numbers from 0 to N
'''
# n = 100
# sum = 0

# for num in range(n):
# 	sum += num

# print(sum)

# # result:
# # 4950

'''
Fibonachi array
'''
# fibonachi = []

# fibonachi.append(0) # first element
# fibonachi.append(1) # second element

# for x in range(10):
#     fibonachi.append(fibonachi[x] + fibonachi[x+1])

# print(fibonachi)

# # result:
# # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

'''
Sum of array's elements
'''
# array = [7, 5, 3, 4, 9, 13, 55, 48, 16]
# sum = 0

# for num in array:
# 	sum += num

# print(sum)

# # result:
# # 160
'''
Number of array's elements
'''
# array = [7, 5, 3, 4, 9, 13, 55, 48, 16]
# counter = 0

# for x in array:
# 	counter += 1

# print(counter)

# # result:
# # 0
'''
Average of array's elements
'''
# array = [7, 5, 3, 4, 9, 13, 55, 48, 16]
# sum = 0
# counter = 0

# for num in array:
# 	sum += num
# 	counter += 1

# average = sum/counter
# print(average)

# # result:
# # 17.77777777777778
'''
Maxinum number in the array
'''
# array = [7, 5, 3, 4, 9, 13, 55, 48, 16]
# max = 0

# for num in array:
# 	if num > max:
# 		max = num

# print(max)

# # result:
# # 55
'''
Minimum number in the array
'''
# array = [7, 5, 3, 4, 9, 13, 55, 48, 16]
# min = 999 # depends on the range of the numbers in the array
#           # or it can be the first element of the array

# for num in array:
# 	if num < min:
# 		min = num

# print(min)

# # result:
# # 3
'''
Rank for the array elements (descending order)
'''
# array = [7, 5, 3, 4, 9, 13, 55, 48, 16]
# rank = []

# for i in array:
# 	current_rank = 1
# 	for j in array:
# 		if i < j:
# 			current_rank += 1
# 	rank.append(current_rank)

# print(rank)

# # result:
# # [6, 7, 9, 8, 5, 4, 1, 2, 3]
'''
Comparison between two times
'''
# first_time = [2, 50, 15] # 2h 50m 15s
# second_time = [2, 13, 50] # 2h 13m 50s

# first_in_seconds = first_time[0] * 60 * 60 + first_time[1] * 60 + first_time[2]
# second_in_seconds = second_time[0] * 60 * 60 + second_time[1] * 60 + second_time[2]

# if first_in_seconds > second_in_seconds:
# 	print("2h 50m 15s is Greater than 2h 13m 50s")
# else:
# 	print("2h 13m 50s is Greater than 2h 50m 15s")

# # result:
# # 2h 50m 15s is Greater than 2h 13m 50s
'''
Subtraction between two times
'''
# first_time = [2, 50, 15] # 2h 50m 15s
# second_time = [2, 13, 50] # 2h 13m 50s

# # get times in seconds
# first_in_seconds = first_time[0] * 60 * 60 + first_time[1] * 60 + first_time[2]
# second_in_seconds = second_time[0] * 60 * 60 + second_time[1] * 60 + second_time[2]

# # subtract from greater and get difference between them
# difference_in_seconds = 0
# if first_in_seconds > second_in_seconds:
# 	difference_in_seconds = first_in_seconds - second_in_seconds
# else:
# 	difference_in_seconds = second_in_seconds - first_in_seconds

# # get times in minutes and seconds
# difference = [0, 0, difference_in_seconds] # 0h 0m 0s
# difference[1] = int(difference[2] / 60) # get minutes
# difference[2] = int(difference[2] % 60) # remainder for seconds

# # get times in hours and minutes
# difference[0] = int(difference[1] / 60) # get hours
# difference[1] = int(difference[1] % 60) # remainder for minutes

# print(str(difference[0]) + "h " + str(difference[1]) + "m " + str(difference[2]) + "s")
# # result:
# # 0h 36m 25s
'''
Exchange two values in variables
'''
# x = 100
# y = 500

# temp = x
# x = y
# y = temp

# print("x is " + str(x))
# print("y is " + str(y))

# # result:
# # x is 500
# # y is 100
'''
Get the Greatest Common Denominator (GCD) between two numbers
'''
# constraint
# x is greater or equal to y
x = 196
y = 72

while y != 0:
    temp_x = x
    temp_y = y
    x = temp_y
    y = temp_x % temp_y

print("The Greate Common Denominator is " + str(x))

# result:
# The Greate Common Denominator is 4
'''
Bucket Sort
'''
array = [3, 1, 6, 2, 8, 4, 9] # numbers between 1 to 10
buckets = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
result = []

for num in array:
	buckets[num] = num

for num in buckets:
	if num != 0:
		result.append(num)

print(result)

# result:
# [1, 2, 3, 4, 6, 8, 9]
'''

'''
'''

'''
'''

'''