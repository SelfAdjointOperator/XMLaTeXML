#!/usr/bin/env python3

from XMLaTeXML import *

def main() -> None:
    test = latex()(
        head()(
            usepackage("fontspec")
        ),
        body(_class = "article")(
            document()(
                titlepage(title = "Hello World", author = "Me", date = "2023/01/20"),
                section(title = "Foo")(
                    p()("""Lorem Ipsum""")
                ),
                section(title = "Bar")(
                    p()("dolor sit amet")
                )
            )
        )
    )

    print(test, end = "")

if __name__ == "__main__":
    main()
