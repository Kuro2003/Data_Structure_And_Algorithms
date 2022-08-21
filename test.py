# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'circularArrayRotation' function below.
# #
# # The function is expected to return an INTEGER_ARRAY.
# # The function accepts following parameters:
# #  1. INTEGER_ARRAY a
# #  2. INTEGER k
# #  3. INTEGER_ARRAY queries
# #

# def circularArrayRotation(a, k, queries):
#     # Write your code here
#     for _ in range(k-1):
#         for i in range(len(a),0):
#             a[i] = a[i-1]
#         a[0] = a[len(a)-1]
#         a.pop()
#     b = []
#     for i in range(queries):
#         b.append(a[queries[i]])
#     return b
        

# if __name__ == '__main__':
#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     k = int(first_multiple_input[1])

#     q = int(first_multiple_input[2])

#     a = list(map(int, input().rstrip().split()))

#     queries = []

#     for _ in range(q):
#         queries_item = int(input().strip())
#         queries.append(queries_item)

#     result = circularArrayRotation(a, k, queries)
#     print(result)
for i in range(10,0,-1):
    print(i)