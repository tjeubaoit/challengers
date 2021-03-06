from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [0]*n
        cols = [0]*m
        for index in indices:
            rows[index[0]] += 1
            cols[index[1]] += 1
        ans = 0
        for i in range(n):
            for j in range(m):
                if (rows[i] + cols[j]) % 2 != 0:
                    ans += 1
        return ans