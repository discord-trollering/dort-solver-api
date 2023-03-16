class CaptchaException(Exception):
    pass


class UnsolvableCaptchaException(CaptchaException):
    pass


class BannedAPIKeyException(CaptchaException):
    pass


class ExpiredAPIKeyException(CaptchaException):
    pass


class TooManyThreadsException(CaptchaException):
    pass


class InvalidAPIKeyException(CaptchaException):
    pass
