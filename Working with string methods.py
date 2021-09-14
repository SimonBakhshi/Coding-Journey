# The following excersices will be using string methods to manipulate strings:

# title() and upper()
poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
poem_author_fixed = poem_author.upper()
print(poem_title)
print(poem_title_fixed)
print(poem_author_fixed)

# split()
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