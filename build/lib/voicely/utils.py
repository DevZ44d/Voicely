from typing import Dict, Optional, Any

class Providers:
    def __init__(self) -> None:
        self.headers: Dict[str, Any]= {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.7',
            'baggage': 'sentry-environment=prod,sentry-release=v38.10.1,sentry-public_key=5743ef12f4887fc460c7968ebb2de54d,sentry-trace_id=512010a9386b4033861df903ad601329,sentry-sampled=false,sentry-sample_rand=0.9049516425471105,sentry-sample_rate=0.01',
            'content-type': 'application/json',
            'origin': 'https://quillbot.com',
            'platform-type': 'webapp',
            'priority': 'u=1, i',
            'referer': 'https://quillbot.com/tools/speech-to-text',
            'sec-ch-ua': '"Brave";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'sentry-trace': '512010a9386b4033861df903ad601329-84fa3d50c8705a54-0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
            'useridtoken': 'empty-token',
            'webapp-version': '38.10.1'
        }

        self.cookies: Dict[str, Any] = {
            'abIDV2': '546',
            'anonID': 'f7ceed385778e221',
            'authenticated': 'false',
            'premium': 'false',
            'acceptedPremiumModesTnc': 'false',
            '__cf_bm': '5oz6F928rmOywKoojckMRR3P8GB7A8_szhd_3J9nFhc-1765045614-1.0.1.1-LRQUyfZijt7WEqqnOLdF.yiDSeEy3_syQsJb9XZgtNUvvxPrKvWfZRcmCrZphjZdGUklsAkQjp14rkHo5wK6rFkLRLenur.Hzov0arODrio',
            '_sp_ses.48cd': '*',
            'connect.sid': 's%3AbN7340Rs_cy1oRIomc-GBnTSOz73VwmA.dyJ1NsdoNviAx%2BZAfj%2BNNR6HZigwO2qirevcfJKbcd8',
            'qdid': '2978193014202472763',
            'g_state': '{"i_l":0,"i_ll":1765045665975,"i_b":"BnUEx95FwI4ZE2tvFg0mCoKnQubBtBa0bDQZTFgfgI8"}',
            '_sp_id.48cd': '37c7e1f4-cd04-4797-afdf-d0b8e6ae880f.1760000217.2.1765045726.1760000263.61f3f5c0-2893-4aff-b352-b6e5666f54e9.b760f49e-b39d-4e2e-8ad9-bc70a1125d8b.7274f374-e043-4af9-aaf1-b29422bfe9ff.1765045665501.3',
        }

        self.provides = {
            "Headers": self.headers,
            "Cookies": self.cookies
        }

    def __getitem__(self, item):
        return self.provides[item]



