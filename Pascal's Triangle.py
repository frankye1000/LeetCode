import numpy as np
numRows=5
if numRows == 0:
    print([])


else:
    rerurn_list = [[1]]
    for i in range(0, numRows - 1):
        head = np.array([0] + rerurn_list[i])
        tail = np.array(rerurn_list[i] + [0])
        rerurn_list.append((head + tail).tolist())
    print(rerurn_list)