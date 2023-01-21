from typing import Any

class Element:
    def __init__(self, **attr_kwargs) -> None:
        self.children = None
        self.attr_kwargs = attr_kwargs

    def __call__(self, *children: Any) -> None:
        # for child in children:
        #     if not isinstance(child, Elt):
        #         raise ValueError("Invalid child: should not be an Elt")

        self.children = children

        return self

    def __str__(self) -> str:
        ret = f"<{self.__class__.__name__}"

        attr_kwargs_not_none = {k: v for k, v in self.attr_kwargs.items() if v is not None}

        if attr_kwargs_not_none:
            ret += " " + " ".join((
                f"{attr_name}={repr(attr_value)}"
                for attr_name, attr_value in attr_kwargs_not_none.items()
            ))

        ret += ">\n"

        if self.children is not None:
            for child in self.children:
                child_str = str(child)
                for line in child_str.splitlines():
                    ret += f"  {line}\n"

        ret += f"</{self.__class__.__name__}>\n"

        return ret
