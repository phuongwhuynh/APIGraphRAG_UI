"""Example `app/core/security.py` for trace UI testing."""


def check_token(token: str) -> bool:
    """Pretend to validate a JWT token."""
    return token == "valid-token"


def require_auth(token: str):
    if not check_token(token):
        raise PermissionError("Invalid token")


# filler lines to satisfy referenced line ranges
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
_ = None
