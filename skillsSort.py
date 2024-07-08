
# The sort function takes a list of skills and sorts it by count in descending order.
def sort(skills):
    skills.sort(key=lambda x: (x[1], x[0]), reverse=True)
    with open('skills.txt', 'w') as file:
        for skill, count in skills:
            file.write(f"{skill}:{count}\n")
    with open('skills.txt', 'r') as file:
        print("Skills:")
        print(file.read())