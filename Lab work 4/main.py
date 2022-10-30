import numpy as np
import pandas as pd

f = open('var2-rv1.txt', 'r')
#1 question
nums = []
i = 0

# for line in f:
#     nums[i] = line
#     i += 1

for line in f:
    nums.append(line.replace('\n', ''))
print(nums)

# average = 0
# i = 0
# for num in nums:
#     average += num
#     i += 1
#
# average = average / i
#
# print(average)
# #2 question
# dispers = np.var(nums)
# print(nums)


