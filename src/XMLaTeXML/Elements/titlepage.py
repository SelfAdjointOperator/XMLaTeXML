from typing import Optional

from . import Element, ChildlessMixin

class titlepage(ChildlessMixin, Element):
    def __init__(self, title: Optional[str] = None, author: Optional[str] = None, date: Optional[str] = None) -> None:
        super().__init__(title = title, author = author, date = date)
