from typing import Dict

from . import Element

class p(Element):
    def __init__(self, style: Dict = None) -> None:
        super().__init__(style = style)
