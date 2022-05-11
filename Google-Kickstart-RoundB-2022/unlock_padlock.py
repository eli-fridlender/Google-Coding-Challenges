import numpy as np

def find_longest_chain(arr):
  curr_start_index=0
  largest_range_start_index = 0
  largest_range_end_index = 0
  for i in range(0,len(arr), 1):
    if arr[i] == 0 or i == len(arr)-1:
      if(i-curr_start_index) > (largest_range_end_index-largest_range_start_index):
        largest_range_start_index = curr_start_index
        if arr[i] == 0:
          largest_range_end_index = i-1
        else:
          largest_range_end_index = i
        curr_start_index = i+1
  return largest_range_start_index, largest_range_end_index


def find_largest_num(arr):
  largest_num = arr[0]
  for i in arr:
    if(i > largest_num):
      largest_num = i
  return largest_num



def run_unlock_padlock(case_num):
  (num_dials, size_dials) = tuple(map(int, input().split(' ')))
  dials = np.array(list((map(int, input().split(' ')))))

  downwards_list = np.zeros(num_dials)
  upwards_list = np.zeros(num_dials)
  dials_remaining = num_dials
  shared_indices = []
  moves = 0


  for i in range(0, num_dials, 1):
    if dials[i] < (size_dials - dials[i] + 1):
      downwards_list[i] = dials[i]
    elif dials[i] == 0:
      dials_remaining -= 1
    elif dials[i] == (size_dials - dials[i] + 1):
      downwards_list[i] = dials[i]
      upwards_list[i] = dials[i]
      shared_indices.append(i)
    else:
      upwards_list[i] = dials[i]

    while dials_remaining > 0:
      (up_start, up_end) = find_longest_chain(upwards_list)
      (down_start, down_end) = find_longest_chain(downwards_list)

      if (up_end - up_start) > (down_end - down_start):
        print("Longest chain up")
        print(upwards_list[up_start:up_end])
        moves += find_largest_num(upwards_list[up_start:up_end])
        dials_remaining -= (up_end-up_start)
        upwards_list[up_start:up_end] = 0

      else:
        print("Longest chain down")
        print(down_start)
        print(down_end)
        print(upwards_list[down_start:down_end])

        moves += find_largest_num(downwards_list[down_start:down_end])
        dials_remaining -= (down_end-down_start)
        downwards_list[down_start:down_end] = 0

      print(f"Case #{case_num}: {moves}")


num_cases = int(input())
for i in range(num_cases):
  run_unlock_padlock(i+1)
