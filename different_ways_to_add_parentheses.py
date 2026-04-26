class Solution:
    def diffWaysToCompute(self, expression: str):
        memo = {}
        
        def compute(expr):
            if expr in memo:
                return memo[expr]
            
            res = []
            
            for i in range(len(expr)):
                if expr[i] in '+-*':
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])
                    
                    for l in left:
                        for r in right:
                            if expr[i] == '+':
                                res.append(l + r)
                            elif expr[i] == '-':
                                res.append(l - r)
                            else:
                                res.append(l * r)
            
            if not res:
                res.append(int(expr))
            
            memo[expr] = res
            return res
        
        return compute(expression)