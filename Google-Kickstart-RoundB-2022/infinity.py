import math

def calc_area_of_circle(radius):
  return math.pi*(radius**2)

def run_infinity_circles(case_num):
  (R, A, B) = tuple(map(int, input().split(' ')))

  sum_of_areas = calc_area_of_circle(R)
  last_radius = R

  while last_radius > 0:
    #cal left circle
    last_radius = last_radius*A
    sum_of_areas += calc_area_of_circle(last_radius)

    #cal right circle
    last_radius = int(last_radius/B)
    sum_of_areas += calc_area_of_circle(last_radius)

  print(f"Case #{case_num}: {sum_of_areas}")


num_cases = int(input())
for i in range(num_cases):
  run_infinity_circles(i+1)