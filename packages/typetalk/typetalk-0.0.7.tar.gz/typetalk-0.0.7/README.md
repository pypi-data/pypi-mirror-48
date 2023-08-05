typetalk-py
===

[![PyPI](https://img.shields.io/pypi/v/typetalk.svg)](https://pypi.python.org/pypi/typetalk)
[![Build Status](https://travis-ci.com/is2ei/typetalk-py.svg?branch=master)](https://travis-ci.com/is2ei/typetalk-py)
[![Coverage Status](https://coveralls.io/repos/github/is2ei/typetalk-py/badge.svg?branch=master)](https://coveralls.io/github/is2ei/typetalk-py?branch=master)

Typetalk API client written in Python

Usage
---

#### Simple bot example

```python
import os
import typetalk

bot = typetalk.bot(token=os.environ['TYPETALK_TOKEN'])

response = bot.post_message(
    topic_id='12345'
    message="Hello, world!")
)
assert response["ok"]
assert response["post"]["message"] == "Hello world!"
```

Links
---

- [Typetalk API Document](https://developer.nulab.com/docs/typetalk/)
