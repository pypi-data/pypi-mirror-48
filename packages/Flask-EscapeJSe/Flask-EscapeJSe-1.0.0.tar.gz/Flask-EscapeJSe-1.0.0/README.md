<!--
  Title: Escape curly braces in jinja template
  Description: Escape curly braces used by JavaScript frameworks to indicate a expression in jinja templates.
  Author: Akhil Harihar
  -->

# flask_escapejstv
![PyPI](https://img.shields.io/pypi/v/Flask-EscapeJSe.svg)
[![Build Status](https://travis-ci.com/akhilharihar/Flask-EscapeJSe.svg?branch=master)](https://travis-ci.com/akhilharihar/Flask-EscapeJSe)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

Flask extension which provides a filter to escape "curly" braces `{{ }}` in Jinja templates for use in JavaScript frameworks as few Javascript frameworks use "curly" braces to display the value of an expression or variable.

## Installing
Install and update using [pip](https://pip.pypa.io/en/stable/quickstart/) :
```
pip install Flask-EscapeJSe
```

To enable this filter in your flask app, register this extension.

```
from flask_escapejse import EscapeJSe

EscapeJSe(app)
```

Like other Flask extensions, you can register it lazily:

```
ejse = EscapeJSe()

def create_app():
    app = Flask(__name__)
    ejse.init_app(app)
```

## Usage
```
{{ "js_variable_name"|jse }}
```

For more information on jinja filters, visit [http://jinja.pocoo.org/docs/2.10/templates/#filters](http://jinja.pocoo.org/docs/2.10/templates/#filters)
