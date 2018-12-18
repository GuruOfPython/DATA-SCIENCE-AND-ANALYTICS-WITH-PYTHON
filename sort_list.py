from __future__ import division

import natsort

# 1. Sort File Names in a proper way

## Make a list of file names like P_0.png, P_1.png
file_names = [f'P_{index}.png' for index in range(200)]
print(file_names)

## Sort by sort()
file_names.sort()
print(file_names)

## Sort by natsort
file_names = natsort.natsorted(file_names, reverse=False)
print(file_names)
