# this is a practice file where you can play around with the code and test your functions or try new things
#do not change the code in this file just edit on blank lines

students = {
    "jason": 90,
    "james": 80,
    "jane": 70,
    "jill": 60,
    "jerry": 50
}

weather = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

list_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

student_names = ["jason", "james", "jane", "jill", "jerry"]

# for student,value in students.items():
#     if value > 50:
#         print(student)
        
# high = students["jason"]
# print(high)
# list_num = []
# for x in list_nums:
#     list_num.append(x * 2)
# print(list_num)

# nums = {}
# for num in list_nums:
#     nums[num] = num * 2
    
# print(nums)
weathers = {}
for days,value in weather.items():
    weathers[days] = value * (9/4)
    
print(weathers)