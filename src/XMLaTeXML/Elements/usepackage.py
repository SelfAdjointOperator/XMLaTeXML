from . import Element, ChildlessMixin

class usepackage(ChildlessMixin, Element):
    def __init__(self, name: str) -> None:
        super().__init__(name = name)
