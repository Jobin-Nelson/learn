'''
Created Date: 2023-05-12
Qn: You are given a 0-indexed 2D integer array questions where questions[i] =
    [pointsi, brainpoweri].

    The array describes the questions of an exam, where you have to process the
    questions in order (i.e., starting from question 0) and make a decision
    whether to solve or skip each question. Solving question i will earn you
    pointsi points but you will be unable to solve each of the next brainpoweri
    questions. If you skip question i, you get to make the decision on the next
    question.

        - For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]: 
            - If question 0 is solved, you will earn 3 points but you will be
              unable to solve questions 1 and 2. 
            - If instead, question 0 is skipped and question 1 is solved, you
              will earn 4 points but you will be unable to solve questions 2
              and 3.

    Return the maximum points you can earn for the exam.
Link: https://leetcode.com/problems/solving-questions-with-brainpower/
Notes:
    - use dp bottom up approach
    - at each position there are two choices solve or skip
'''
def mostPoints(questions: list[list[int]]) -> int:
    N = len(questions)
    dp = [0] * N

    for i in range(N-1, -1, -1):
        next_qn = i + questions[i][1] + 1
        solve = questions[i][0]
        solve += dp[next_qn] if next_qn < N else 0
        skip = dp[i+1] if i+1 < N else 0
        dp[i] = max(solve, skip)
    return dp[0]

    # recursive 
    # n = len(questions)
    # def dfs(i: int) -> int:
    #     if i >= n: return 0
    #     return max(questions[i][0] + dfs(i + questions[i][1] + 1), dfs(i+1))
    # return dfs(0)

if __name__ == '__main__':
    q1 = [[3,2],[4,3],[4,4],[2,5]]
    q2 = [[1,1],[2,2],[3,3],[4,4],[5,5]]

    print(mostPoints(q1))
    print(mostPoints(q2))
