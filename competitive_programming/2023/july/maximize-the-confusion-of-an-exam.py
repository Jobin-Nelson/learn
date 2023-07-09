'''
Created Date: 2023-07-07
Qn: A teacher is writing a test with n true/false questions, with 'T' denoting
    true and 'F' denoting false. He wants to confuse the students by maximizing
    the number of consecutive questions with the same answer (multiple trues or
    multiple falses in a row).

    You are given a string answerKey, where answerKey[i] is the original answer
    to the ith question. In addition, you are given an integer k, the maximum
    number of times you may perform the following operation:

        Change the answer key for any question to 'T' or 'F' (i.e., set
        answerKey[i] to 'T' or 'F').

    Return the maximum number of consecutive 'T's or 'F's in the answer key
    after performing the operation at most k times.
Link: https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
Notes:
    - use sliding window
'''
from collections import Counter

def maxConsecutiveAnswers(answerKey: str, k: int) -> int:
    res = 0
    count = Counter()

    for r in range(len(answerKey)):
        count[answerKey[r]] += 1
        if min(count['T'], count['F']) <= k:
            res += 1
        else:
            count[answerKey[r - res]] -= 1
    return res

if __name__ == '__main__':
    a1, k1 = "TTFF", 2
    a2, k2 = "TFFT", 1
    a3, k3 = "TTFTTFTT", 1
    
    print(maxConsecutiveAnswers(a1, k1))
    print(maxConsecutiveAnswers(a2, k2))
    print(maxConsecutiveAnswers(a3, k3))
