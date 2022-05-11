import numpy as np



def run_pancakes(case_num):
  num_of_paying_customers = 0
  num_of_pancakes = int(input())
  pancakes_queue = np.array(list(map(int, input().split(' '))))
  left_index = 0
  right_index = num_of_pancakes-1
  pancakes_left = num_of_pancakes
  highest_delicousness_level = 0

  while pancakes_left > 0:
    chosen_del_val = 0
    if pancakes_queue[left_index] < pancakes_queue[right_index] and left_index != right_index:
      chosen_del_val = pancakes_queue[left_index]
      left_index+=1
    else:
      chosen_del_val = pancakes_queue[right_index]
      right_index-=1

    if chosen_del_val >= highest_delicousness_level:
      highest_delicousness_level = chosen_del_val
      num_of_paying_customers += 1

    pancakes_left -= 1

  print(f"Case #{case_num}: {num_of_paying_customers}")


num_cases = int(input())
for i in range(num_cases):
  run_pancakes(i+1)