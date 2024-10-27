class Solution:
    def encode(self, strs: list[str]) -> str:
        res = []
        for s in strs:
            res.append(f'{len(s)}#{s}')
        return ''.join(res)
    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res

if __name__ == "__main__":
    s1 = ["neet","code","love","you"]
    es1 = Solution().encode(s1)
    ds1 = Solution().decode(es1)
    print(es1, ds1)
