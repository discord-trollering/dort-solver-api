import httpx
from httpx import post, Response

from dortsolver.exceptions import TooManyThreadsException, UnsolvableCaptchaException, \
    ExpiredAPIKeyException, BannedAPIKeyException, CaptchaException, InvalidAPIKeyException


class BaseSolver(object):
    def __init__(self, base_url, **kwargs) -> None:
        self.path = base_url
        self.__dict__.update(**kwargs)

    def solve(self) -> str:
        try:
            response: Response = post(f"https://api.dort.shop/captcha/solve/{self.path}",
                                      json=self.__dict__, timeout=60)
            data: dict = response.json()
            error: str = data.get('solver[error]')
            if error:
                __switcher__: dict = {
                    "too many active threads for api key.": TooManyThreadsException,
                    "no user found for provided api key.": InvalidAPIKeyException,
                    "failed to solve.": UnsolvableCaptchaException,
                    "expired api key.": ExpiredAPIKeyException,
                    "you are banned.": BannedAPIKeyException
                }
                raise __switcher__.get(error, CaptchaException)()
            return data.get('game[token]')
        except httpx.TimeoutException:
            raise UnsolvableCaptchaException()
