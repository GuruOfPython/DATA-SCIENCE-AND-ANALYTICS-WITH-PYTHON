from __future__ import division

import natsort

# 1. Sort File Names in a proper way

## Make a list of file names like P_0.png, P_1.png
file_names = [f'P_{index}.png' for index in range(200)]
print('New List\t', file_names)

## Sort by sort()
file_names.sort()
print('Sort by sort\t', file_names)

## Sort by index
def takeFirstElement(elem):
    return elem[0]

file_names.sort(key=takeFirstElement)
print('Sort by index\t', file_names)

## Sort by sorted
student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])   # sort by age
print('Sort by sorted\t', student_tuples)

## Sort by natsort
file_names = natsort.natsorted(file_names, reverse=False)
print('Sort by natsort\t', file_names)




