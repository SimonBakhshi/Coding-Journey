### Warmup-1:

# sleep_in:
def sleep_in(weekday, vacation):
  return not weekday or vacation
 
# monkey_trouble:
def monkey_trouble(a_smile, b_smile):
  return (a_smile and b_smile) or (not a_smile and not b_smile)

# sum_double:
def sum_double(a, b):
  if a == b:
    return (a + b) * 2
  return a + b  

# diff21:
def diff21(n):
  if n > 21:
    return abs(n - 21) * 2
  else:
    return abs(n - 21)

# parrot_trouble:
def parrot_trouble(talking, hour):
  if talking and (hour < 7 or hour > 20):
    return True
  return False

# makes10:
def makes10(a, b):
  if (a == 10 or b == 10 or a+b == 10):
    return True
  return False

# near_hundred:
def near_hundred(n):
  if ((abs(100 - n) <= 10) or (abs(200 - n) <= 10)):
    return True
  return False

# pos_neg:
# solution 1
def pos_neg(a, b, negative):
  if (a > 0 and b < 0 and negative == False):
    return True
  elif (a < 0 and b > 0 and negative == False):
    return True
  elif negative == True and (a < 0 and b < 0):
    return True
  else:
    return False

# solution 2 
def pos_neg(a, b, negative):
  if negative:
   return (a < 0 and b < 0)
  else:
    return ((a > 0 and b < 0) or (a < 0 and b > 0)) 

# not_string:
def not_string(str):
  word_list = str.split()
  if word_list[0] == "not":
    return str
  return "not " + str

# missing_char:
# solution 1
def missing_char(str, n):
  lst = list(str)
  lst.pop(n)
  return "".join(lst)

# solution 2
def missing_char(str, n):
  front = str[:n]
  back = str[n+1:]
  return front + back

# front_back:
def front_back(str):
  if len(str) < 2:
    return str
  return str[-1] + str[1:-1] + str[0]

# front3:
def front3(str):
  front = str[0:3] * 3
  return front

### Warmup-2:

# string_times:
# solution 1
def string_times(str, n):
  return str * n

# solution 2
def string_times(str, n):
  result = ""
  for i in range(n):
    result += str 
  return result

# front_times:
def front_times(str, n):
  front = str[0:3] * n
  return front 

# string_bits:
def string_bits(str):
  new_str = str[0:20:2]
  return new_str
    
### List-1:

# first_last6: 
def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  return False

# same_first_last:
def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[-1]

# make_pi:
def make_pi():
  return [3, 1, 4]

# common_end: 
def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

# sum3:
def sum3(nums):
  return sum(nums)  

# rotate_left3:
def rotate_left3(nums):
  return nums[1:] + [nums[0]]

# reverse3:
def reverse3(nums):
  reversed_list = reversed(nums)
  return list(reversed_list)

# max_end3:
def max_end3(nums):
  nums_0_largest = [nums[0]] * 3
  nums_2_largest = [nums[2]] * 3
  if nums[0] > nums[2]:
    return nums_0_largest
  else: 
    return nums_2_largest  

# sum2:
def sum2(nums):
  if len(nums) >= 2:
    return nums[0] + nums[1]
  elif len(nums) == 1:
    return nums[0]
  else:
    return 0

# middle_way:
def middle_way(a, b):
  new_list = [a[int(len(a)/2)], b[int(len(b)/2)]]
  return new_list 

# make_ends:
def make_ends(nums):
 new_list = [nums[0], nums[-1]]
 return new_list

# has23:
def has23(nums):
  for n in nums:
    if n == 2 or n == 3:
      return True
  return False

### Logic-1:

# cigar_party:
def cigar_party(cigars, is_weekend):
  if (cigars >= 40 and cigars <= 60):
    return True
  elif (cigars >= 40 and is_weekend):
    return True
  return False

# squirrel_play:
def squirrel_play(temp, is_summer):
  if (temp >= 60 and temp <= 90):
    return True
  elif (temp >= 60 and temp <= 100):
    return is_summer
  return False

print(squirrel_play(60, 200))

# caught_speeding:
def caught_speeding(speed, is_birthday):
  if (speed <= 60):
    return 0
  elif (speed <= 65 and is_birthday):
    return 0
  elif (speed >= 61 and speed <= 80):
    return 1
  elif (speed >= 66 and speed <= 85 and is_birthday):
    return 1
  elif speed >= 81:
    return 2

# sorta_sum:
def sorta_sum(a, b):
  if a + b >= 10 and a + b <= 19:
    return 20
  return (a + b)

# alarm_clock:
def alarm_clock(day, vacation):
  weekend = int(day) in (0, 6)
  if weekend and vacation:
      return "off"
  elif weekend or vacation:
    return "10:00"
  return "7:00"

# love6:
def love6(a, b):
  sum_ab = a + b
  diff_ab = a - b
  return ((sum_ab == 6 or abs(diff_ab) == 6) or (a == 6 or b == 6))

print(love6(7, 1))
  
