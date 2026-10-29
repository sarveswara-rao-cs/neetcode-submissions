class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(s.split())
        s1 = s1.lower()

        def clear_extra(t):
            nt = ''
            for c in t:
                # print(f'Before: {c}', ord('a'), ord(c), ord('z'))
                if (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9')):
                    nt += c
                    # print(f'after: {c}')
            return nt
        s1 = clear_extra(s1)
        s2 = s1[::-1]
        print(s1, s2)
        if s1==s2: 
            return True 
        else:
            return False