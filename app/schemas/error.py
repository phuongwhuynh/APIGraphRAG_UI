"""Example `app/schemas/error.py` for trace UI testing."""


class ErrorResponse:
    def __init__(self, error: str, message: str, details: dict = None):
        self.error = error
        self.message = message
        self.details = details or {}


class ValidationErrorResponse:
    def __init__(self, errors: list = None):
        self.errors = errors or []


# filler to reach >=50 lines
def _h(n):
    return None


_h(1)
_h(2)
_h(3)
_h(4)
_h(5)
_h(6)
_h(7)
_h(8)
_h(9)
_h(10)
_h(11)
_h(12)
_h(13)
_h(14)
_h(15)
_h(16)
_h(17)
_h(18)
_h(19)
_h(20)
_h(21)
_h(22)
_h(23)
_h(24)
_h(25)
_h(26)
_h(27)
_h(28)
_h(29)
_h(30)
_h(31)
_h(32)
_h(33)
_h(34)
_h(35)
_h(36)
_h(37)
_h(38)
_h(39)
_h(40)
_h(41)
_h(42)
_h(43)
_h(44)
_h(45)
_h(46)
_h(47)
_h(48)
_h(49)
_h(50)
