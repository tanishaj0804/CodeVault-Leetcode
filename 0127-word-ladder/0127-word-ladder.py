class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        q = deque()
        visited = set()
        visited.add(beginWord)
        q.append((beginWord,1))
        while q:
            curr,moves = q.popleft()
            if curr == endWord:
                return moves
            for i in range(len(curr)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    neww = curr[:i] + ch + curr[i+1:]
                    if neww not in visited and neww in wordList:
                        visited.add(neww)
                        q.append((neww,moves+1))
        return 0
            