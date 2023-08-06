pyramid_htmldoom
================
[htmldoom](https://github.com/sayanarijit/htmldoom) rendering library plugin for Pyramid

Usage
----
### Install

```bash
pip install pyramid_htmldoom
```

### Plug into Pyramid

#### app.py

```python
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

@view_config(route_name="hello_htmldoom", renderer="templates.hello.py")
def hello_htmldoom_view(request):
    """htmldoom rendered view"""
    return {"data": "Hello htmldoom"}


if __name__ == "__main__":
    with Configurator() as config:
        config.scan()

        config.include("pyramid_htmldoom")
        config.add_route("hello_htmldoom", "/")

        app = config.make_wsgi_app()
    server = make_server("localhost", 8080, app)
    server.serve_forever()
```

#### templates/hello.py

```python
from htmldoom import base as b
from htmldoom import elements as e
from htmldoom import render as _render
from htmldoom import renders

doctype = _render(b.doctype("html"))


@renders(e.title()("{doctitle}"))
def render_title(doctitle: str) -> dict:
    return {"doctitle": doctitle}


@renders(e.body()("{content}"))
def render_body(data: dict) -> None:
    raise NotImplementedError("You are trying to render a layout.")


@renders("{doctype}", e.html()(e.head()("{title}"), "{body}"))
def render_document(
    data: dict,
    title_renderer: callable = render_title,
    body_renderer: callable = render_body,
) -> dict:
    return {
        "doctype": doctype,
        "title": title_renderer(doctitle=data["data"]),
        "body": body_renderer(data=data),
    }


def render(data: dict) -> str:
    return render_document(data=data)
```

#### templates/layout.py

```python
from htmldoom import elements as e
from htmldoom import renders

from .layout import render_document


@renders(
    e.body()(
        e.h3()("{contents}"),
        e.a(href="/")("Home"),
        e.br(),
        e.a(href="/jinja2")("jinja2"),
    )
)
def render_body(data: dict) -> dict:
    return {"contents": data["data"]}


def render(data: dict) -> str:
    return render_document(data, body_renderer=render_body)
```

Examples
--------
[Find demo and examples here](https://github.com/sayanarijit/pyramid_htmldoom/blob/master/examples)
