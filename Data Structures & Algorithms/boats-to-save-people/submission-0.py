class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        count = 0
        while l <= r:
            if l == r: 
                count += 1
                break
            sum_l_r = people[l] + people[r]
            if sum_l_r <= limit:
                l += 1
                r -= 1
                count += 1
            else:
                r -= 1
                count += 1
        return count