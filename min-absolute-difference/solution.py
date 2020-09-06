#!/usr/bin/env python

# Observations:
# We could find an answer to this problem by brute-forcing it:
# Keep a running track of the minimum difference for each number in the array, compared with every other number
# That would require O(n * (n + 1)/2), or simply O(n^2)

# Would trim this down if we first sorted the array, because now each number only needs to be compared to its neighbor.
# In this case, it takes O(n * log n) time to sort the array, and then O(n) time to figure out the minimum, meaning O(n * log n) total time.
# Assuming we cannot mutate the original array, we need O(n) extra storage space to hold the sorted array

from functools import reduce


def absolute_min_reduction(acc, element):
    minFound, last = acc
    diff = abs(element - last)
    if diff < minFound:
        minFound = diff

    return minFound, element


INDEX_MIN_FOUND = 0


def minimumAbsoluteDifference(nums):
    sortedNums = sorted(nums)
    initial = (abs(sortedNums[0] - sortedNums[1]), sortedNums[1])
    reduced = reduce(absolute_min_reduction, sortedNums[2:], initial)
    return reduced[INDEX_MIN_FOUND]
