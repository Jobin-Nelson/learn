'''
Qn: TinyURL is a URL shortening service where you enter a URL such as 
https://leetcode.com/problems/design-tinyurl and it returns a short URL 
such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.
Link:https://leetcode.com/problems/encode-and-decode-tinyurl/
Notes:
- use two hashmaps to store and retrive long & short urls
'''
class Codec:
    def __init__(self):
        self.encode_map = {}
        self.decode_map = {}
        self.base = 'https://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encode_map:
            shortUrl = self.base + str(len(self.encode_map) + 1)
            self.encode_map[longUrl] = shortUrl
            self.decode_map[shortUrl] = longUrl
        return self.encode_map[longUrl]
        
    def decode(self, shortUrl: str) -> str:
        return self.decode_map[shortUrl]

if __name__ == '__main__':
    url = "https://leetcode.com/problems/design-tinyurl"
    obj = Codec()
    tiny = obj.encode(url)
    print(tiny)
    long = obj.decode(tiny)
    print(long)
