# A2.3 - Ten Subject Marks

marks = []

for i in range(10):
    mark = int(input("Enter marks: "))
    marks.append(mark)

highest = marks[0]
lowest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

print("Marks:", marks)
print("Highest marks:", highest)
print("Lowest marks:", lowest)