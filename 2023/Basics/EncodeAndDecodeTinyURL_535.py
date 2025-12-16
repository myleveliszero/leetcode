# Status: Bad

class Codec:

    def __init__(self) -> None:
        self.url = "SOMETHING"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        bytes_encoded = longUrl.encode()
        self.url = bytes_encoded.decode()

        return bytes_encoded
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url

url_ = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
encode = codec.encode(url_)
print(encode)
decode = codec.decode(encode)
print(decode)