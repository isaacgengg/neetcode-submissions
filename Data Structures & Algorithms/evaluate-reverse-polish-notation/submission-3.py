class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []

        operators = {'+', '-', '*', '/'}
        

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                numStack.append(int(tokens[i]))
            else:
                num2 = numStack.pop()
                num1 = numStack.pop()
                currNum = 0
                
                if tokens[i] == '+':
                    currNum = num1 + num2
                elif tokens[i] == '-':
                    currNum = num1 - num2
                    
                elif tokens[i] == '*':
                    currNum = num1 * num2
                else:
                    currNum = int(num1 / num2)
            
                numStack.append(currNum)
            
        return numStack.pop()


        