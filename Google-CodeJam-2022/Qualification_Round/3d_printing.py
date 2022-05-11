NUM_OF_PRINTERS = 3
INK_REQUIRED = 10**6
NUM_OF_INK_TYPES = 4

def process_3d_printing(case_num):
  amounts_string = ""
  lowest_ink_amounts = [INK_REQUIRED]*NUM_OF_INK_TYPES
  for i in range(NUM_OF_PRINTERS):
    printer_amounts = tuple(map(int, input().split(' ')))

    for i in range(0, NUM_OF_INK_TYPES, 1):
      if printer_amounts[i] < lowest_ink_amounts[i]:
        lowest_ink_amounts[i] = printer_amounts[i]


  total = sum(lowest_ink_amounts)

  if total < INK_REQUIRED:
    amounts_string = "IMPOSSIBLE"
  else:
    amount_to_reduce = total - INK_REQUIRED
    for amount in lowest_ink_amounts:
      new_amount = 0

      if amount - amount_to_reduce >= 0:
        new_amount = amount - amount_to_reduce
        amount_to_reduce = 0
      else:
        amount_to_reduce -= amount
        new_amount = 0

      amounts_string += (str(new_amount) + " ")

  amounts_string = amounts_string.strip()

  print(f"Case #{case_num}: {amounts_string}")



num_cases = int(input())
for i in range(num_cases):
  process_3d_printing(i+1)
