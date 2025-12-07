import requests
from typing import Dict, Optional, Any

class Translation:
    def __init__(self, To: Optional[str], word: Optional[str]):
        self.endpoint: str = f"https://clients5.google.com/translate_a/single?dj=1&dt=t&dt=sp&dt=ld&dt=bd&client=dict-chrome-ex&sl=auto&tl={To}&q={word}"

    def get(self):
        return requests.get(
            self.endpoint ).json()['sentences'][0]['trans']