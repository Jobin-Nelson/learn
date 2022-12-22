'''
Created Date: 2022-12-17
Qn: Evaluate the value of an arithmetic expression in Reverse Polish Notation.

    Valid operators are +, -, *, and /. Each operand may be an integer or
    another expression.

    Note that division between two integers should truncate toward zero.

    It is guaranteed that the given RPN expression is always valid. That means
    the expression would always evaluate to a result, and there will not be any
    division by zero operation.
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
Notes:
    - use stack to store digits
    - when you encounter an operation pop twice from the stack
    - perform the operation and append it back to the stack
'''
def evalRPN(tokens: list[str]) -> int:
    operations = {
        "+": lambda x,y: x + y,
        "-": lambda x,y: x - y,
        "*": lambda x,y: x * y,
        "/": lambda x,y: float(x) / y,
    }

    nums = []
    for t in tokens:
        if t not in operations:
            nums.append(int(t))
        else:
            left = nums.pop()
            right = nums.pop()
            nums.append(int(operations[t](left, right)))
    return nums.pop()

if __name__ == '__main__':
    t1 = ["2","1","+","3","*"]
    t2 = ["4","13","5","/","+"]
    t3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

    print(evalRPN(t1))
    print(evalRPN(t2))
    print(evalRPN(t3))
