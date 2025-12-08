import requests
from typing import Dict, Optional, Any

class Translation:
    def __init__(self, To: Optional[str], word: Optional[str]):
        self.to = To
        self.word = word
        self.__endpoint: str = f"https://clients5.google.com/translate_a/single?dj=1&dt=t&dt=sp&dt=ld&dt=bd&client=dict-chrome-ex&sl=auto&tl={To}&q={word}"
        self._data: Dict[str, Any] = {}

    def get(self):
        __response = requests.get(self.__endpoint).json()['sentences'][0]['trans']

        self._data = {
            "Text": __response,
        }

        return __response

    def __getitem__(self, item):
        """Enable dict-style access: obj['Text']"""
        if not self._data:
            self.get()
        return self._data[item]
