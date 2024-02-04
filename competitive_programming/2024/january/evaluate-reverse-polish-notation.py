"""
Created Date: 2024-01-30
Qn: You are given an array of strings tokens that represents an arithmetic
    expression in a Reverse Polish Notation.

    Evaluate the expression. Return an integer that represents the value of the
    expression.

    Note that:

        - The valid operators are '+', '-', '*', and '/'. 
        - Each operand may be an integer or another expression. 
        - The division between two integers always truncates toward zero. 
        - There will not be any division by zero. 
        - The input represents a valid arithmetic expression in a reverse
          polish notation. 
        - The answer and all the intermediate calculations can be represented
          in a 32-bit integer.
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
Notes:
    - use number stack to hold numbers and evaluate when encountering an operation
"""
def evalRPN(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        if len(token) > 1 or token.isdigit():
            stack.append(int(token))
        else:
            a = stack.pop()
            b = stack.pop()
            if token == "*":
                stack.append(a * b)
            elif token == '/':
                stack.append(int(b / a))
            elif token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(b - a)
    return stack.pop()


if __name__ == '__main__':
    t1 = ["2","1","+","3","*"]
    t2 = ["4","13","5","/","+"]
    t3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    t4 = ["4", "3", "-"]

    print(evalRPN(t1))
    print(evalRPN(t2))
    print(evalRPN(t3))
    print(evalRPN(t4))
