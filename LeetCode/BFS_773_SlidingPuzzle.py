# https://github.com/chris-chris/master-leetcode/blob/master/code/773.py
import itertools

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = tuple(itertools.chain(*board))
        target = (1, 2, 3, 4, 5, 0)
        # BFS 
        Q = deque()
        Q.append((start, 0))
        visited = set()

        while Q:
            node, step = Q.popleft()
            visited.add(node)

            # finish condition
            if node == target:
                return step

            nlist = list(node)
            zi = -1 # zero's current index 
            for i, n in enumerate(nlist)
                if n == 0:
                    zi  = i

            # Properity test
            for di in [-1, 1, -3, 3]:
                nlist = list(node)
                i2 = zi + di # new zi - zero's index
                # 
                if i2 < 0 or i2 >= 6:
                    continue
                if not (abs(i2 % 3 - zi % 3) == 1 or abs(i2 - z2) == 3):
                    continue # 왜 continue 지...? 이건 들어봐야 알겠다. 

                # swap
                nlist[i2], nlist[zi] = nlist[zi], nlist[i2]
                next_node = tuple(nlist)
                if next_node in visited:
                    continue
                Q.append((next_node, step + 1))

        return -1