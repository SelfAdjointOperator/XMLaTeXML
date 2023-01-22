# XMLaTeXML

Using Python to programmatically generate XML-ish code, procrastinating against LaTeX.

## Examples

`./examples/example-01.py` currently yields

```xml
<latex>
  <head>
    <usepackage name='fontspec'/>
  </head>
  <body _class='article'>
    <document>
      <titlepage title='Hello World' author='Me' date='2023/01/20'/>
      <section title='Foo'>
        <p>
          Lorem Ipsum
        </p>
      </section>
      <section title='Bar'>
        <p>
          dolor sit amet
        </p>
      </section>
    </document>
  </body>
</latex>
```

---

## EOF

Probably will just fork [PyLaTeX](https://github.com/JelteF/PyLaTeX) which I've used before.

Replacing $\LaTeX$'s backend looks like a behemoth task, not a task for one person.

Project archived to Area51

---
