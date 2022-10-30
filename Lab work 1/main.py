import random

from scipy.special import factorial
import numpy as np

# 1 задание
integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(integer_list)
# 2 задание
factorials = factorial(integer_list)
print(factorials)
# 3 задание сортировка в обратном порядке
integer_list_reverse = integer_list
integer_list_reverse.sort(reverse=True)
print(integer_list_reverse)
# 4 задание
number_list = np.arange(-10, 11, 1)
print(number_list)
negative_sum = 0
negative_sum = np.sum(number_list[number_list < 0])
print(negative_sum)
positive_sum = 0
positive_sum = np.sum(number_list[number_list > 0])
print(positive_sum)
# 5 задание
fiveQuest = np.random.randint(1, 100, (5, 5))
fiveQuestMin, fiveQuestMax = fiveQuest.min(), fiveQuest.max()
fiveQuestAverage = fiveQuest.mean()
print(fiveQuest)
print(fiveQuestMin)
print(fiveQuestMax)
print(fiveQuestAverage)
# 6 задание
v = np.arange(1, 26, 1)
vMatrix = v.reshape((5, 5))
print(vMatrix)
# 7 задание

a1 = vMatrix[:1, :].copy()
a2 = vMatrix[1:2, :].copy()
a3 = vMatrix[2:3, :].copy()
a4 = vMatrix[3:4, :].copy()
a5 = vMatrix[4:5, :].copy()

aMin = np.array([a1.min(), a2.min(), a3.min(), a4.min(), a5.min()]).reshape(5, 1)
aMax = np.array([a1.max(), a2.max(), a3.max(), a4.max(), a5.max()]).reshape(5, 1)
print(aMin)
print("")
print(aMax)
# 8 задание
data_norm1 = (a1.copy() - a1.copy().min()) / (a1.copy().max() - a1.copy().min())#normalize first row and other
data_norm2 = (a2.copy() - a2.copy().min()) / (a2.copy().max() - a2.copy().min())
data_norm3 = (a3.copy() - a3.copy().min()) / (a3.copy().max() - a3.copy().min())
data_norm4 = (a4.copy() - a4.copy().min()) / (a4.copy().max() - a4.copy().min())
data_norm5 = (a5.copy() - a5.copy().min()) / (a5.copy().max() - a5.copy().min())

print(data_norm1)
print(data_norm2)
print(data_norm3)
print(data_norm4)
print(data_norm5)

#for example different array
data = np.array([[13, 16, 19, 22, 23, 38, 47, 56, 58, 63, 65, 70, 71]])

#normalize all values in array
data_norm = (data - data. min ())/ (data. max () - data. min ())

#view normalized values
data_norm

#9 задание

array_9 = np.random.randint(1, 100, 10)
print(array_9)

indMin = np.unravel_index(np.argmin(array_9, axis=None), array_9.shape)
indMax = np.unravel_index(np.argmax(array_9, axis=None), array_9.shape)
array_9[indMax] = 100
array_9[indMin] = 0
print(array_9)

#10 задание

p = np.array([[1,1], [4,5]])
distance = (np.sqrt((np.power( (p[1,0] - p[0,0]), 2) + np.power( (p[1, 1] - p[0, 1]), 2) )))
print(distance)

#11 задание
array_11 = np.arange(-2, 4, 1)
print(array_11)
answer = 1 / (1 + np.exp(-(np.sum(array_11))))
print(answer)

#12 задание

d = np.array([[0, 21, 17],
 [21, 0, 42],
 [17, 42, 0]])

print(np.argsort(d) + 1)

