'''

Find the k post offices located closest to you, given your location and a list of locations of all post offices available.
Locations are given in 2D coordinates in [X, Y], where X and Y are integers.
Euclidean distance is applied to find the distance between you and a post office.
Assume your location is [m, n] and the location of a post office is [p, q], the Euclidean distance between the office and
you is SquareRoot((m - p) * (m - p) + (n - q) * (n - q)).
K is a positive integer much smaller than the given number of post offices. from aonecode.com

e.g.
Input
you: [0, 0]
post_offices: [[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]]
k = 3

Output from aonecode.com
[[-1, 2], [0, 3], [4, 3]]
'''

# [m, n] - subject's location

import numpy as np

origin = [0,0]

dist_dict = {}


def get_k_nearest_post_offices(post_ofcs, k):
    for ind, val in enumerate(post_ofcs):
        eucl_dist = np.sqrt((origin[0] - val[0]) * (origin[0] - val[0]) + (origin[1] - val[1]) * (origin[1] - val[1]))
        dist_dict[eucl_dist] = val

    #print(dist_dict)
    return sorted(dist_dict)[:k]


k_nearest_po_keys = get_k_nearest_post_offices([[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]], 3)

for key in k_nearest_po_keys:
    print(dist_dict[key])




# to preserve duplicate keys if needed
# from collections import defaultdict
#
# d = defaultdict(list)
#
#
# def get_k_nearest_post_offices(post_ofcs, k):
#     for ind, val in enumerate(post_ofcs):
#         eucl_dist = np.sqrt((origin[0] - val[0]) * (origin[0] - val[0]) + (origin[1] - val[1]) * (origin[1] - val[1]))
#         d[eucl_dist].append(val)
#     return sorted(dist_dict)[:k]
#
# k_nearest_po_keys = get_k_nearest_post_offices([[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]], 3)
#
# for key in k_nearest_po_keys:
#     print(dist_dict[key])