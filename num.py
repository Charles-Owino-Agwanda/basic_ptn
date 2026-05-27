import numpy as np

ratings = np.array([[94, 89, 63, 45], [93, 92, 48, 23], [92, 94, 56, 98]])

# print(ratings)

# print(ratings.shape)

ones = np.ones((3, 4))
# print(ones)
zeros = np.zeros((2, 3))
# print(zeros)
random = np.random.random((3, 3))
# print(random)

# print(ratings[0, :])
# print(ratings[:, 0])
# print(ratings[ratings > 90])


ratings_extra_row = np.append(ratings, [[92, 88, 78, 55]], axis=0)
# print(ratings_extra_row)

# print(ratings_extra_row.shape)
# ratings_del_row = np.delete(ratings, [2], axis=0)
# print(ratings_del_row)
# print(ratings_del_row.shape)
print(ratings)

print(ratings.sum())

print(ratings.sum(axis=0))
print(ratings.sum(axis=1))
overall_max_index = np.argmax(ratings)
print(overall_max_index)
overall_min_index = np.argmin(ratings)
print(overall_min_index)
