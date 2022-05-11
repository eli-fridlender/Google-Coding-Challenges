import math
import numpy as np

def get_changes(arr, start, end, change):
  changes = 0
  for i in range(start, end, change):
    changes += abs(arr[i] - arr[(i+change)])

  return changes


def calc_pump_changes(arr1, arr2, last_pas_val, length):
  changes = abs(arr1[0] - last_pas_val)
  changes += get_changes(arr1, 0, length-1,1)
  changes += abs(arr1[length-1] - arr2[0])
  changes += get_changes(arr2, 0, length-1,1)

  return changes


def run_controlled_inflation(case_num):
  num_of_changes = 0
  last_pascal_val = 0
  (num_of_customers, num_of_items) = tuple(map(int, input().split(' ')))

  curr_customer = None
  next_customer = None

  for i in range(0, math.floor(num_of_customers/2)):
    curr_customer = list(map(int, input().split(' ')))
    next_customer = list(map(int, input().split(' ')))
    curr_customer = np.sort(curr_customer)
    next_customer = np.sort(next_customer)

    smallest_change = math.inf

    ff_changes = calc_pump_changes(curr_customer, next_customer, last_pascal_val, num_of_items)
    fb_changes = calc_pump_changes(curr_customer, np.flip(next_customer), last_pascal_val, num_of_items)
    bf_changes = calc_pump_changes(np.flip(curr_customer), next_customer, last_pascal_val, num_of_items)
    bb_changes = calc_pump_changes(np.flip(curr_customer), np.flip(next_customer), last_pascal_val, num_of_items)

    if ff_changes < smallest_change:
      smallest_change = ff_changes
      last_pascal_val = next_customer[num_of_items-1]

    if fb_changes < smallest_change:
      smallest_change = fb_changes
      last_pascal_val = next_customer[0]

    if bf_changes < smallest_change:
      smallest_change = bf_changes
      last_pascal_val = next_customer[num_of_items-1]

    if bb_changes < smallest_change:
      smallest_change = bb_changes
      last_pascal_val = next_customer[0]

    num_of_changes += smallest_change

  if num_of_customers % 2 != 0:
    last_customer = list(map(int, input().split(' ')))
    forward_changes = abs(last_customer[0] - last_pascal_val)
    back_changes = abs(last_customer[num_of_items-1] - last_pascal_val)

    forward_changes += get_changes(last_customer,0,num_of_items-1,1)
    back_changes += get_changes(np.flip(last_customer),0,num_of_items-1,1)

    if forward_changes < back_changes:
      num_of_changes += forward_changes
    else:
      num_of_changes += back_changes

  print(f"Case #{case_num}: {num_of_changes}")


num_cases = int(input())
for i in range(num_cases):
  run_controlled_inflation(i+1)
