from typing import Any


class ZeroQuantityProduct(Exception):

    def __init__(self, message: Any = None) -> None:
        super.__init__(message)
