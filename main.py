list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
new_list = []
for i in list1:
    for x in list2:
        if i == x:
            new_list.append(x)
print(new_list)


numbers = [1, 2, 2, 3, 4, 4, 5, 1]
remove_duplicates = []
for x in numbers:
    if x not in remove_duplicates:
        remove_duplicates.append(x)
print(remove_duplicates)


vowels = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count_vowels = 0
for x in vowels:
    if x in word:
        count_vowels += 1
print(count_vowels)

# numbers = [10, 50, 30, 90, 70, 90]
# largest_number = numbers[0]
# second_largest_number = numbers[0]
# for number in numbers:
#     if number > largest_number:
#         largest_number = number
#         second_largest_number = number
#     elif number < second_largest_number:
#         second_largest_number = number
# print(largest_number)
# print(second_largest_number)

# numbers = [1, 5, 3, 9, 7, 9]
# largest = numbers[0]
# second_largest = numbers[0]
# for number in numbers:
#     if number > largest:
#         largest = number
#         second_largest = number
#     elif number < second_largest:
#         second_largest = number
# print(largest)
# print(second_largest)

# numbers = [1, 2, 2, 3, 3, 3, 4]
# for number in numbers:
#     count = 0
#     for i in numbers:
#         if i == number:
#             count += 1
#     if number not in numbers[:numbers.index(number)]:
#         print(number,"appears",count,"times")

# numbers = [2, 5, 2, 7, 2, 8, 5]
# count = 0
# for number in numbers:
#     if number == 2:
#         count += 1
# print("2 appears",count,"times")
