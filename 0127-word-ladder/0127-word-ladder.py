class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        visited = set()
        q = deque()
        q.append((beginWord,1))
        visited.add(beginWord)
        while q:
            curr, moves = q.popleft()
            if curr == endWord:
                return moves
            for i in range(len(curr)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    neww = curr[:i] + ch + curr[i+1:]
                    if neww not in visited and neww in wordList:
                        visited.add(neww)
                        q.append((neww,moves+1))
        return 0