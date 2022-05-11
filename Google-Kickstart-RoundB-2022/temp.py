
WALL_CHAR = "|"
CELL_CHAR = "."
CORNER_CHAR = "+"
BORDER_CHAR = "-"

def create_border_row(cols):
  border_string = CORNER_CHAR

  for _ in range(0, cols, 1):
    border_string = border_string + BORDER_CHAR + CORNER_CHAR

  return border_string

def create_cell_row(cols):

  cells_string = WALL_CHAR

  for _ in range(0, cols, 1):
    cells_string = cells_string + CELL_CHAR + WALL_CHAR

  return cells_string


def print_punched_card(case_num):
  (rows, cols) = tuple(map(int, input().split(' ')))
  top_left_cell_row_length = 2
  top_left_cell_col_length = 2
  top_left_cell_pattern = ""

  border_row = create_border_row(cols)
  cell_row = create_cell_row(cols)

  print(f"Case #{case_num}:")

  for _ in range(0, top_left_cell_col_length):
    top_left_cell_pattern = top_left_cell_pattern + CELL_CHAR

  for i in range(1, rows*2+2 , 1):
    string = ""
    if i % 2 == 0:
      string = cell_row
    else:
      string = border_row

    if i <= top_left_cell_row_length:

      string = string.replace(string[0:top_left_cell_col_length], top_left_cell_pattern, 1)
    print(string)

num_cases = int(input())
for i in range(num_cases):
  print_punched_card(i+1)