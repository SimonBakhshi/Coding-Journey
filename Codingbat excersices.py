### Warmup-1:

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

# near_hundred
def near_hundred(n):
  if ((abs(100 - n) <= 10) or (abs(200 - n) <= 10)):
    return True
  return False
  
print(near_hundred(97))

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
  
