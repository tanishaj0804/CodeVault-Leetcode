class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        deadend = set(deadends)

        if target in deadend or '0000' in deadend:
            return -1

        q = deque()
        q.append(('0000', 0))

        visited = {'0000'}

        while q:

            curr, step = q.popleft()

            if curr == target:
                return step

            for i in range(4):

                for j in [-1, 1]:

                    neww = (int(curr[i]) + j) % 10

                    newc = curr[:i] + str(neww) + curr[i+1:]

                    if newc not in visited and newc not in deadend:
                        visited.add(newc)
                        q.append((newc, step + 1))

        return -1