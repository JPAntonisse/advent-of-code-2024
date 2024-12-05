import numpy as np

from utils.file_reader import read_input

word_search = np.array(read_input(day=4))

# Preprocess array; Split on each Char
word_search = list(map(list, word_search))

# Kernels must len x=y
kernel_1 = np.array([
    ['X', 'M', 'A', 'S'],
    ['.', '.', '.', '.'],
    ['.', '.', '.', '.'],
    ['.', '.', '.', '.'],
])

kernel_2 = np.array([
    ['X', '.', '.', '.'],
    ['.', 'M', '.', '.'],
    ['.', '.', 'A', '.'],
    ['.', '.', '.', 'S'],
])


def rotate_90(kernel):
    # Rotate clockwise
    return np.rot90(kernel, k=1, axes=(1, 0))


def generate_kernels(kernel_x, kernel_y):
    rotations = [kernel_x, kernel_y]
    for _ in range(3):
        kernel_x = rotate_90(kernel_x)
        rotations.append(kernel_x)

        kernel_y = rotate_90(kernel_y)
        rotations.append(kernel_y)

    return rotations


def pad_with_kernel_size(input_array, kernels):
    padding = kernels[0].shape[0] - 1

    # Apply padding using np.pad
    return np.pad(input_array, padding, mode='constant', constant_values=0)


def apply_sliding_window(input_array, kernels, func):
    size = kernels[0].shape[0]
    count = 0

    for i in range(input_array.shape[0] - (size - 1)):
        for j in range(input_array.shape[1] - (size - 1)):
            window = input_array[i:i + size, j:j + size]
            count += func(window=window, kernels=kernels)
    return count


def count_kernel_matches(window, kernels):
    count = 0
    for kernel in kernels:
        conduit = kernel != '.'
        match = np.equal(window, kernel)
        if np.all(match[conduit] == True):
            count += 1
    return count


# Setup the kernels for all the ways XMAS can be located
kernels = generate_kernels(kernel_x=kernel_1, kernel_y=kernel_2)

# Since the kernels can change orientation, we pad array
word_search = pad_with_kernel_size(input_array=word_search, kernels=kernels)

# # Go through every point in the padded search space, and check if a kernel matches
count = apply_sliding_window(input_array=word_search, kernels=kernels, func=count_kernel_matches)

print(f"Part one: {count}")

# Part 2

kernels_xmas = np.array([
    [
        ['M', '.', 'S'],
        ['.', 'A', '.'],
        ['M', '.', 'S'],
    ],
    [
        ['M', '.', 'M'],
        ['.', 'A', '.'],
        ['S', '.', 'S'],
    ],
    [
        ['S', '.', 'M'],
        ['.', 'A', '.'],
        ['S', '.', 'M'],
    ],
    [
        ['S', '.', 'S'],
        ['.', 'A', '.'],
        ['M', '.', 'M'],
    ],
])

# Go through every point in the padded search space, and check if a kernel matches
count = apply_sliding_window(input_array=word_search, kernels=kernels_xmas, func=count_kernel_matches)

print(f"Part two: {count}")
