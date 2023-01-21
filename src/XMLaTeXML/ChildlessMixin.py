class ChildlessMixin:
    def __str__(self) -> str:
        ret = f"<{self.__class__.__name__}"

        attr_kwargs_not_none = {k: v for k, v in self.attr_kwargs.items() if v is not None}

        if attr_kwargs_not_none:
            ret += " " + " ".join((
                f"{attr_name}={repr(attr_value)}"
                for attr_name, attr_value in attr_kwargs_not_none.items()
            ))

        ret += "/>\n"

        return ret
