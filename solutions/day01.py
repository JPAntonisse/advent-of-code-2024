import numpy as np

from utils.file_reader import read_input

locations = read_input(day=1)

loc_a = np.array([])
loc_b = np.array([])

# Part one
# Find the sum of the difference in two sorted arrays

for location in locations:
    a, b = location.split('   ')
    loc_a = np.append(loc_a, int(a))
    loc_b = np.append(loc_b, int(b))

loc_a.sort()
loc_b.sort()

sum = abs(np.subtract(loc_a, loc_b)).sum()

print(f"Part 1 Sum of these Locations: {sum}")

# Part two
# Find how many times, item in list a, is in list b and multiply by itself
# That is the similarity score

similarity_score = 0

for location_a in loc_a:
    x = np.where(loc_b == location_a, location_a, 0)
    if x.any():
        similarity_score += np.count_nonzero(x) * location_a

print(similarity_score)