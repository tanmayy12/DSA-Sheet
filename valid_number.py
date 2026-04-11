class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        
        num = False
        dot = False
        exp = False
        
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = True
                
            elif ch in ['+', '-']:
                # sign only valid at start or after e/E
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
                
            elif ch == '.':
                # dot only once and not after exponent
                if dot or exp:
                    return False
                dot = True
                
            elif ch in ['e', 'E']:
                # exponent only once and must have number before
                if exp or not num:
                    return False
                exp = True
                num = False   # reset for digits after e
                
            else:
                return False
        
        return num