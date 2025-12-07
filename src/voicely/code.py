from typing import Optional
import base64, asyncio, httpx
from .utils import Providers
from .translation import Translation

class Audio:
    def __init__(__self, *, audio:Optional[str], Translation_To: Optional[str] = "en") -> None:
        __self.json_data = {
            'audioData': __self._encode_audio(audio),
            'mode': 'timestamp',
            'language': 'en',
            'dialect': 'US',
        }
        __self.c = Providers()
        __self.translation = Translation_To
        __self.extract_text = asyncio.run(__self.send())


    def _encode_audio(__self, audio_path):
        with open(audio_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")

    async def send(__self):
        try:
            async with httpx.AsyncClient(
                    cookies=__self.c["Cookies"],
                    headers=__self.c["Headers"],
                    timeout=httpx.Timeout(10.0)) as client:
                response = await client.post(
                        'https://quillbot.com/api/raven/stt/process-recording',
                        json=__self.json_data
                    )
                result = response.json()
                if result["message"] == "success":
                    return result["data"]["raw"]
        except Exception as e:
            return e

    def start(__self):
        return Translation(
            To=__self.translation,
            word=__self.extract_text
        ).get()



