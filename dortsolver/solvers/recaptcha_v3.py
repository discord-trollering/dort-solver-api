import secrets
from typing import Union

from dortsolver._base_solver import BaseSolver


class ReCaptchaV3Solver(BaseSolver):
    def __init__(self, api_key: str, site_url: str, site_key: str, proxy_url: Union[str, None] = None) -> None:
        super().__init__("rc3", api_key=api_key, site_url=site_url, site_key=site_key, proxy_url=proxy_url,
                         callback=secrets.token_hex(4), type='invisible')
