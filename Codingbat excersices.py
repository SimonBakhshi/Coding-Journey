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
