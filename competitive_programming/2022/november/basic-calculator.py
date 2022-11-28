'''
Created Date: 2022-11-20
Qn: Given a string s representing a valid expression, implement a basic
    calculator to evaluate it, and return the result of the evaluation.

    Note: You are not allowed to use any built-in function which evaluates
    strings as mathematical expressions, such as eval()
Link: https://leetcode.com/problems/basic-calculator/
Notes:
    - rpn doesn't work because of unary minus
    - handle digits, +-, (, ) seperately
    - update output when you encounter sign
    - store the last output when you encounter opening bracket
'''
def calculate(s: str) -> int:
    output, cur, sign, stack = 0, 0, 1, []

    for c in s:
        # 1234
        if c.isdigit():
            cur = cur * 10 + int(c)
        # +-
        elif c in '+-':
            output += (cur * sign)
            cur = 0
            if c == '+':
                sign = 1
            else:
                sign = -1
        # (
        elif c == '(':
            stack.append(output)
            stack.append(sign)
            output = 0
            sign = 1
        # )
        elif c == ')':
            output += (cur * sign)
            output *= stack.pop()
            output += stack.pop()
            cur = 0
    return output + (cur * sign)

    # def parse(input: str) -> list[str]:
    #     output = []
    #     operator_stack = []
    #
    #     for token in input:
    #         if token.isdigit():
    #             output.append(token)
    #         elif token == ')':
    #             while operator_stack[-1] != '(':
    #                 output.append(operator_stack.pop())
    #             operator_stack.pop()
    #         elif token != ' ':
    #             operator_stack.append(token)
    #
    #
    #     output.extend(operator_stack)
    #
    #     return output
    #
    # def evaluate(rpn: list[str]) -> int:
    #     number_stack = []
    #     for token in rpn:
    #         if token.isdigit():
    #             number_stack.append(token)
    #         else:
    #             left = int(number_stack.pop())
    #             right = int(number_stack.pop())
    #
    #             if token == '+':
    #                 number_stack.append(right + left)
    #             else:
    #                 number_stack.append(right - left)
    #     print(f'{number_stack=}')
    #     return number_stack.pop()
    # rpn = parse(s)
    # print(f'{rpn=}')
    # return evaluate(rpn)

if __name__ == '__main__':
    s1 = "1 + 1"
    s2 = "2-1 + 2"
    s3 = "(1+(4+5+2)-3)+(6+8)"

    print(calculate(s1))
    print(calculate(s2))
    print(calculate(s3))
