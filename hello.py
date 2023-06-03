import numpy as np

three_dim = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
for twod in three_dim:
    """How can we print out all of the elements in the three dimensional array"""
    print("-------------------")
    for oned in twod:
        for zerod in oned:
            if zerod % 5 == 0:
                print(zerod)
