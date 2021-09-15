# The following excersices will be using string methods to manipulate strings:

# .title() and upper()
poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
poem_author_fixed = poem_author.upper()
print(poem_title)
print(poem_title_fixed)
print(poem_author_fixed)

# .split()
line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words)

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
author_names = authors.split(",")
print(author_names)
author_last_names = []
for names in author_names:
  author_last_names.append(names.split()[-1])
print(author_last_names)

# .join(), and \n
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = " ".join(reapers_line_one_words)
print(reapers_line_one)

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = "\n".join(winter_trees_lines)
print(winter_trees_full)

# .strip() and .join()
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
love_maybe_lines_stripped = []
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())

love_maybe_full = "\n".join(love_maybe_lines_stripped)

print(love_maybe_full)

