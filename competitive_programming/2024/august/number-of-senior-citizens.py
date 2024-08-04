"""
Created Date: 2024-08-01
Qn: You are given a 0-indexed array of strings details. Each element of details
    provides information about a given passenger compressed into a string of
    length 15. The system is such that:

    - The first ten characters consist of the phone number of passengers.
    - The next character denotes the gender of the person.
    - The following two characters are used to indicate the age of the person.
    - The last two characters determine the seat allotted to that person.
      
    Return the number of passengers who are strictly more than 60 years old.
Link: https://leetcode.com/problems/number-of-senior-citizens/
Notes:
"""
def countSeniors(details: list[str]) -> int:
    return sum(1 for v in details if int(v[-4:-2]) > 60)

if __name__ == '__main__':
    d1 = ["7868190130M7522","5303914400F9211","9273338290F4010"]
    d2 = ["1313579440F2036","2921522980M5644"]

    print(countSeniors(d1))
    print(countSeniors(d2))
