class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        
        # Step 1: Remove redundant coins
        unique_coins = []
        for coin in coins:
            if not any(coin % u == 0 for u in unique_coins):
                unique_coins.append(coin)
                
        n = len(unique_coins)
        
        # Step 2: Precompute subset LCMs grouped by subset size
        subset_lcm_by_size = defaultdict(list)
        
        for mask in range(1, 1 << n):
            subset_size = 0
            current_lcm = 1
            
            for bit in range(n):
                if (mask >> bit) & 1:
                    subset_size += 1
                    current_lcm = math.lcm(current_lcm, unique_coins[bit])
            
            subset_lcm_by_size[subset_size].append(current_lcm)
            
        def count_multiples(target: int) -> int:
            total_count = 0
            sign = 1
            for size in range(1, n + 1):
                for lcm_val in subset_lcm_by_size[size]:
                    total_count += sign * (target // lcm_val)
                sign = -sign
            return total_count

        # Step 3: Binary search on the answer
        low = unique_coins[0]
        high = unique_coins[0] * k
        answer = high
        
        while low <= high:
            mid = low + (high - low) // 2
            if count_multiples(mid) >= k:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return answer


        