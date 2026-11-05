import random as r

class Solution:
    def __init__(self):
        self.url = {}
    def encode(self, longUrl: str) -> str:
        rand_id = str(r.randint(100000, 999999))
        encoded = f'https://tinyurl.com/{rand_id}'
        self.url[encoded] = longUrl
        return encoded
    def decode(self, shortUrl: str) -> str:
        return self.url[shortUrl]
