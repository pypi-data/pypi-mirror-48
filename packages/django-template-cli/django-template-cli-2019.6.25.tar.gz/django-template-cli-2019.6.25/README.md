<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
https://pypi.org/project/django-readme-generator/
-->

[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/django-template-cli.svg?longCache=True)](https://pypi.org/project/django-template-cli/)

#### Installation
```bash
$ [sudo] pip install django-template-cli
```

#### How it works
```
index.html
context.json (optional)
```

#### Executable modules
usage|`__doc__`
-|-
`python -m django_template_cli path` |render django template file

#### Scripts usage
command|`usage`
-|-
`django-template-cli` |`usage: django-template-cli path`

#### Examples
`index.html`:
```html
{% for v in values %}
{{ forloop.counter0 }}: {{ v }}
{% endfor %}
```

`context.json`:
```json
{
    "values": ["value1","value2","value3"]
}
```

```bash
$ django-template-cli index.html
0: value1

1: value2

2: value3
```

<p align="center">
    <a href="https://pypi.org/project/django-readme-generator/">django-readme-generator</a>
</p>