import bisect
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        preSum = [[0 for _ in range(n+1)] for _ in range(m)]
        print(preSum)
        for i in range(m):
            for j in range(1, n+1):
                preSum[i][j] = preSum[i][j-1] + matrix[i][j-1]
        res = float("-inf")
        for col_l in range(1, n+1):
            for col_r in range(col_l, n+1):
                slist, cur = [0], 0
                for row in range(m):
                    cur += preSum[row][col_r] - preSum[row][col_l-1]
                    idx = bisect.bisect_left(slist, cur-k)
                    if idx < len(slist):
                        res = max(res, cur - slist[idx])
                    bisect.insort(slist, cur)
        return res