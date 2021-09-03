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
  if ((a > 0 and b < 0) and (negative == False)):
    return True
  elif ((a < 0 and b > 0) and (negative == False)):
    return True
  elif ((negative == True) and (a < 0 and b < 0)):
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

# array_count9:
def array_count9(nums):
  count = 0
  for n in nums:
    if n == 9:
      count += 1
  return count

# array_front9:
def array_front9(nums):
  for n in nums:
    if n == 9 in nums[0:4]:
      return True
  return False

 # array123:
 # Take a look at the excersice again! 

### String-1:

# hello_name:
def hello_name(name):
  return "Hello " + name + "!"

# make_abba:
def make_abba(a, b):
  return a + b + b + a

# make_tags:
def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"

# make_out_word:
def make_out_word(out, word):
  return out[0:2] + word + out[2:4]

# extra_end:
def extra_end(str):
  end = str[-2:]
  return end + end + end

# first_two:
def first_two(str):
  return str[:2]

# first_half:
def first_half(str):
  return str[:len(str) / 2]

# without_end:
def without_end(str):
  return str[1:-1]

# combo_string:
def combo_string(a, b):
  if len(b) > len(a):
    return a + b + a
  return b + a + b

# non_start:
def non_start(a, b):
  return a[1:] + b[1:]

# left2:
def left2(str):
  return str[2:] + str[:2]
 
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

# date_fashion:
def date_fashion(you, date):
  if (you >= 8 and date > 2) or (date >= 8 and you > 2):
    return 2
  elif (you <= 2) or (date <= 2):
    return 0
  return 1

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

# in1to10:
def in1to10(n, outside_mode):
  if (outside_mode == True) and (n <= 1 or n >= 10):
    return True
  elif (outside_mode == False) and (n >= 1 and n <= 10):
    return True
  return False

# near_ten:
def near_ten(num):
  return num % 10 <= 2 or num % 10 >= 8  

### Logic-2:

# lone_sum: 
def lone_sum(a, b, c):
  if (a == b) and (b == c) and (a == c):
    sum = 0
  elif (a == b): 
    sum = c  
  elif (b == c):
    sum = a  
  elif (c == a):
    sum = b 
  else:
    sum = (a + b + c)
  return sum

# lucky_sum:
def lucky_sum(a, b, c):
  if a == 13:
    sum = 0
  elif b == 13:
    sum = a
  elif c == 13:
    sum = a + b
  else:
    sum = a + b + c
  return sum
    
### String-2:

# double_char:
# solution 1
def double_char(str):
  return "".join(c + c for c in str)

# solution 2
def double_char(str):
  string = ""
  for c in str:
    string += c + c
  return string

# solution 3
def double_char(str):
  string = ""
  for i in range(len(str)):
    string += str[i] + str[i]
  return string

# count_hi:
# solution 1
def count_hi(str):
  return str.count("hi")

# solution 2
def count_hi(str):
  count = 0
  sub_string = "hi"
  for i in range(len(str)-1):
    if (str[i:i+2] == sub_string):
      count += 1
  return count

# solution 3
def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if (str[i:i+2] == "hi"):
      count += 1
  return count  


 
