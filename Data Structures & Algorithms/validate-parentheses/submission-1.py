class Solution:
    def isValid(self, s: str) -> bool:
        brackets: dict[str,str] = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        stack: list[str] = list()

        for c in s:
            if c not in "([{}])":
                continue
            elif c in "([{":
                stack.append(brackets[c])
            else:
                if len(stack) == 0 or c != stack[-1]:
                    return False
                else:
                    stack.pop()
                    
        return len(stack) == 0

            
