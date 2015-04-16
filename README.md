# mdx_bleach

Python-Markdown extension to sanitize the output of untrusted Markdown documents.

## Installation

    pip install mdx_bleach

## Basic Usage

```python
>>> import markdown
>>> from mdx_bleach.extension import BleachExtension
>>> bleach = BleachExtension()
>>> md = markdown.Markdown(extensions=[bleach])
>>> md.convert('<span>is not allowed</span>')
u'<p>&lt;span&gt;is not allowed&lt;/span&gt;</p>'
```

## Overview

By design, all HTML markup is allowed in Markdown documents. Unless written
inside a code block, raw HTML is not escaped and is therefore rendered by the
web browsers. While this is a nice authoring feature, it also exposes some XSS
vulnerabilities. That becomes a problem when the source of the Markdown document
is untrusted.

**mdx_bleach** is a safer and more flexible alternative to
[Python-Markdown](https://pythonhosted.org/Markdown/reference.html)'s deprecated
safe mode. It uses [Bleach](http://bleach.readthedocs.org/en/latest/), a robust
whitelist-based HTML sanitizer, to sanitize the output of Markdown documents.

## Configuration

To configure the extension, pass the following keyword arguments to ``BleachExtension``:
* ``tags`` Tag Whitelist
* ``attributes`` Attribute Whitelist
* ``styles`` Styles Whitelist
* ``strip`` Stripping Markup
* ``strip_comments`` Stripping Comments

The following example reflects the default configuration::

```python
from mdx_bleach.whitelist import ALLOWED_TAGS, ALLOWED_ATTRIBUTES, ALLOWED_STYLES
bleach = BleachExtension(tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES,
    styles=ALLOWED_STYLES, strip=False, strip_comments=True)
md = markdown.Markdown(extensions=[bleach])
```

### Tag Whitelist

The ``tags`` kwarg is a whitelist of allowed HTML tags. It should be a list,
tuple, or other iterable. Any other HTML tags will be escaped or stripped from
the text. This applies to the HTML output that Markdown produces.

Since Markdown commonly generates HTML elements like ``p``, ``a``, ``img``, etc.
it is recommended to allow at least the default minimal list of tags found in
``mdx_bleach.whitelist.ALLOWED_TAGS``.

For example::

```python
>>> from mdx_bleach.whitelist import ALLOWED_TAGS
>>> bleach = BleachExtension(tags=ALLOWED_TAGS + ['small'])
>>> md = markdown.Markdown(extensions=[bleach])
>>> md.convert('<small>is allowed</small>')
u'<p><small>is allowed</small></p>'
```

This will allow authored ``small`` tags and any tag from the default whitelist.
Note that if a third party extension that can generate more specific tags is
installed, you might want to whitelist those additional tags as well.

### Attribute Whitelist

The ``attributes`` kwarg is a whitelist of attributes. It can be a list, in
which case the attributes are allowed for any tag, or a dictionary, in which
case the keys are tag names (or a wildcard: ``*`` for all tags) and the values
are lists of allowed attributes.

The default value is a conservative dictionary found in ``mdx_bleach.whitelist.ALLOWED_ATTRIBUTES``.
If you override the ``attributes`` kwarg and still want to support images and
links, make sure to allow the ``href`` and ``title`` attributes in ``<a>`` tags,
as well as the ``src``, ``title`` and ``alt`` attributes in ``<img>`` tags.

For example::

```python
attrs = {
    '*': ['class'],
    'a': ['href', 'title', 'rel'],
    'img': ['src', 'title', 'alt'],
}
```

In this case, the ``class`` attribute is allowed on any allowed element (from
the ``tags`` argument), ``<a>`` tags are allowed to have ``href``, ``title`` and
``rel`` attributes, and so on.

You can also use a callable (instead of a list). If the callable returns True,
the attribute is allowed. Otherwise, it is stripped.

For example::

```python
def filter_src(name, value):
    if name in ('alt', 'title', 'height', 'width'):
        return True
    if name == 'src':
        p = urlparse(value)
        return (not p.netloc) or p.netloc == 'mydomain.com'
    return False
```

### Styles Whitelist

If you allow the ``style`` attribute, you will also need to whitelist styles
authors are allowed to set, for example ``color`` and ``background-color``. The
default value is an empty list.

For example, to allow authors to set the color and font-weight of spans::

```python
attrs = {
    'span': ['style']
}
attrs = dict(ALLOWED_ATTRIBUTES.items() + attr.items())
tags = ALLOWED_TAGS + ['span']
styles = ['color', 'font-weight']
```

### Stripping Markup

By default, Bleach *escapes* disallowed or invalid markup. For example::

```python
>>> md = markdown.Markdown(extensions=[BleachExtension()])
>>> md.convert('<span>is not allowed</span>')
u'<p>&lt;span&gt;is not allowed&lt;/span&gt;'
```

If you would rather Bleach stripped this markup entirely, you can pass
``strip=True``::

```python
>>> md = markdown.Markdown(extensions=[BleachExtension(strip=True)])
>>> md.convert('<span>is not allowed</span>')
u'<p>is not allowed</p>'
```

### Stripping Comments

By default, Bleach will strip out HTML comments. To disable this behavior, set
``strip_comments=False``::

```python
>>> html = 'my<!-- commented --> html'

>>> md = markdown.Markdown(extensions=[BleachExtension()])
>>> md.convert(html)
u'<p>my html</p>'

>>> md = markdown.Markdown(extensions=[BleachExtension(strip_comments=False)])
>>> md.convert(html)
u'<p>my<!-- commented --> html</p>'
```

## Links

- [Source](https://github.com/Wenzil/mdx_bleach)
- [Bleach](http://bleach.readthedocs.org/en/latest/)
- [Markdown](http://daringfireball.net/projects/markdown/)
- [Python-Markdown](https://pythonhosted.org/Markdown/)
