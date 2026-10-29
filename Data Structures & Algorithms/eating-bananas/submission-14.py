class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # if len(piles) == 1: return piles//h

        def find_rate(ck):
            cur_hrs = 0
            for pile in piles:
                c_p_h = pile//ck
                if pile%ck > 0:
                    c_p_h += 1
                print('cur:', pile, c_p_h)
                if c_p_h + cur_hrs > h:
                    return -1
                cur_hrs += c_p_h
                # print(cur_hrs)
            return cur_hrs
        
        l, r = 1, max(piles)
        
        save_min = float('inf')
        while l<=r:
            k = (l+r)//2
            print('l, r, mid:', l, r, k)
            f = find_rate(k)
            print('k, f < h:', k, f, h)
            if f != -1: # the fin_rate got a valid hrs
                if k < save_min: save_min = k
                print('k: ', k)
                r = k -1
            if f == -1:
                l = k + 1           

        return save_min
