from typing import Union

from dortsolver._base_solver import BaseSolver


class FunCaptchaSolver(BaseSolver):
    def __init__(self, api_key: str, site_url: str, site_key: str, proxy_url: Union[str, None] = None,
                 data: Union[dict, None] = None, captcha_type: str = "audio-test") -> None:
        if data is None:
            data = {}
        super().__init__("fc", api_key=api_key, site_url=site_url, site_key=site_key, proxy_url=proxy_url, data=data,
                         type=captcha_type)
