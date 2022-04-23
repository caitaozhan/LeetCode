#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#

# @lc code=start
class Codec:

    def __init__(self):
        self.mydict = {}
        self.tiny = 'http://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = hash(longUrl)
        key = -key if key < 0 else key
        tinyurl = self.tiny + str(key)
        self.mydict[tinyurl] = longUrl
        return tinyurl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.mydict[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end

