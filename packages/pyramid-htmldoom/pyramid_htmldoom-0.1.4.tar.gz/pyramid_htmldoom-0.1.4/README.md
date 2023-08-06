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
from htmldoom import elements as e

from .layout import Layout


class Template(Layout):
    """Hello view renderer"""

    @property
    def content(self):
        return e.Div()(
            e.H3()(self["data"]),
        )
```

#### templates/layout.py

```python
from htmldoom import elements as e
from htmldoom.layouts import BaseLayout


class Layout(BaseLayout):
    @property
    def title(self):
        return e.Title()(self["data"])

    @property
    def body(self):
        return e.Body()(e.Div(**{"id": "main"})(self.content))

    @property
    def content(self):
        """To be implemented by renderers."""
        raise NotImplementedError()
```

Examples
--------
[Find demo and examples here](https://github.com/sayanarijit/pyramid_htmldoom/blob/master/examples)
