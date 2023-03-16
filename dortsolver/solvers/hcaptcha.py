from typing import Union

from dortsolver._base_solver import BaseSolver


class HCaptchaSolver(BaseSolver):
    def __init__(self, api_key: str, site_url: str, site_key: str, proxy_url: Union[str, None] = None,
                 rqdata: Union[str, None] = None, enterprise: bool = False) -> None:
        super().__init__("hc-enterprise" if enterprise else "hc", api_key=api_key, site_url=site_url, site_key=site_key,
                         proxy_url=proxy_url, rqdata=rqdata)
