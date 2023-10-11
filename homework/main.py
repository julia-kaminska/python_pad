from homework.task_1 import check_range, bool_range
from homework.task_2 import unique_list
from homework.task_3 import volume_of_sphere
from homework.task_4 import num_fact

# task_1 - function check_range()
print('task 1')
result = check_range(34, 9, 228)
print(result)

result2 = check_range(7, 2, 5)
print(result2)

# task_1 - function bool_range()
result3 = bool_range(34, 9, 228)
print(result3)

result4 = bool_range(7, 2, 5)
print(result4, '\n')

# task_2 - function unique_list()
print('task 2')
my_list = [1, 3, 5, 6, 4, 3, 2, 3, 3, 4, 3, 4, 5, 6, 6, 4, 3, 2, 12, 3, 5, 63, 4, 5, 3, 3, 2]
result5 = unique_list(my_list)
print(result5)

# task_2 - solution without defining the function
unique_list = list(set(my_list))
print(unique_list, '\n')

# task_3 - function volume_of_sphere
print('task 3')
volume = volume_of_sphere(2)
print(volume, '\n')

# task_4 - function num_fact
print('task 4')
factorial = num_fact(10)
print(factorial)
