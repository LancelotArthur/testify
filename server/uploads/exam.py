# #coding=utf-8
# import sys
# import math
#
#
# def mMul(x, n):
#     count = 0
#     for i in range(1, n + 1):
#         count += x
#         x = math.ceil(x/2)
#     return count
#
#
# if __name__ == "__main__":
#     n = list(map(int, sys.stdin.readline().strip().split()))
#     for i in range(int(n[1]/n[0]), n[1]):
#         if mMul(i, n[0]) > n[1]:
#             print(i - 1)
#             break
#coding=utf-8
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     line = list(map(int, sys.stdin.readline().strip().split()))
#     line.sort()
#     i = len(line) - 1
#     count = 0
#     while i > 0:
#         count += line[i] - line[i - 1]
#         i -= 2
#     if i == 0:
#         count += line[0]
#     print(count)
#coding=utf-8
import sys
if __name__ == "__main__":
    n = list(map(int, sys.stdin.readline().strip().split()))
    mat = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        mat.apend(line)
