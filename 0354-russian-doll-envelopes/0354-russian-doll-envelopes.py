class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key = lambda x:(x[0],-x[1]))   #sort height in descending order & width in ascending order
        lis = []
        size  =0
        for w,h in envelopes:
            if not lis or h>lis[-1]:
                lis.append(h)
                size += 1
            else:
                l,r = 0,size
                while l<r:
                    m = l+(r-l)//2
                    if lis[m] < h:
                        l = m+1
                    else:
                        r = m
                lis[l] = h
        return size
