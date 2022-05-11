def process_dice(case_num):
  num_of_dice = int(input())
  dice_values = list(map(int, input().split(' ')))
  dice_values.sort()
  curr_index = 1
  count = 0

  for val in dice_values:
    if val >= curr_index:
      curr_index+=1
      count+=1

  print(f"Case #{case_num}: {count}")

num_cases = int(input())
for i in range(num_cases):
  process_dice(i+1)