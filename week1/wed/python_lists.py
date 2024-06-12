# TASK 1 Grades sorting

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

sorted_grades = sorted(grades, reverse=True) #the instructions stated descending order so i reversed it
print(sorted_grades)

avg_grade = sum(grades) / len(grades)
print(avg_grade)

# TASK 2 temperature slicing

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
week_2 = temperatures[7:14]
print(week_2)

hottest_days = [i for i in temperatures if i >= 100]
print(hottest_days)

the_5th_through_the_10th = temperatures[4:10]
print(the_5th_through_the_10th)