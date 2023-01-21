from typing import Optional

from . import Element

class section(Element):
    def __init__(self, title: Optional[str] = None) -> None:
        super().__init__(title = title)
