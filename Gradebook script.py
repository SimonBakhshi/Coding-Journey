last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)

# New grades
com_sci = ["computer science", 100]
vis_art = ["visual arts", 93]

# New grades + gradebook
gradebook.append(com_sci)
print(gradebook)
gradebook.append(vis_art)
print(gradebook)
gradebook[2].remove(85)
gradebook[2].append("Pass")

#Modify visual arts grade
gradebook[-1][-1] = 98
print(gradebook)

# Combining Last semester grades with current semester grades
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook) 