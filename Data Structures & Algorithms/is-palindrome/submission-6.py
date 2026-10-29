class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        s1 = ''.join(s.split())
        s1 = s1.lower()
        print('s1:', s1)

        def clear_extra(t):
            nt = ''
            for c in t:
                # print(f'Before: {c}', ord('a'), ord(c), ord('z'))
                if (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9')):
                    nt += c
                    # print(f'after: {c}')
            return nt
        s1 = clear_extra(s1)
        if len(s1) <= 1:
            return True
        # s2 = s1[::-1]
        # print(s1, s2)
        # if s1==s2: 
        #     return True 
        # else:
        #     return False
        i = 0
        print(int(len(s1)/2))
        while i<=int(len(s1)/2):
            # print(i, s1[i], s1[len(s1)-i-1])
            if s1[i] == s1[len(s1)-i-1]:
                i += 1
                continue
            else:
                return False
        return True
