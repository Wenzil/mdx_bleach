# Python Markdown Bleach

Markdown extension to sanitize the raw html within untrusted markdown text.

## Installation

    pip install python-markdown-bleach

## Basic Usage

    >>> import markdown
    >>> from mdx_bleach.extension import BleachExtension
    >>> md = markdown.Markdown(extensions=[BleachExtension(tags=['strong'])])
    >>> md.convert('<strong>is allowed</strong>')
    u'<strong>is allowed</strong>'
    >>> md.convert('<span>is not allowed</span>')
    u'&lt;span&gt;is not allowed&lt;/span&gt;'

## Overview

By design, Markdown allows html markup within any given markdown text. The raw html will go unprocessed so it can be rendered by a browser. While this is a nice feature, it also exposes some XSS vulnerabilities, which is a problem if the source of the markdown text is untrusted.

Python Markdown Bleach is a safer and more flexible alternative to [Python Markdown](https://pythonhosted.org/Markdown/reference.html)'s deprecated safe mode. It uses [Bleach](http://bleach.readthedocs.org/en/latest/), a robust a whitelist-based HTML sanitizer, to rid the untrusted markdown text of unwanted markup.

## Configuration

To configure the extension, pass the following keyword arguments to ``BleachExtension``:
* ``tags`` Tag Whitelist
* ``attributes`` Attribute Whitelist
* ``styles`` Styles Whitelist
* ``strip`` Stripping Markup
* ``strip_comments`` Stripping Comments

For example::

    md = markdown.Markdown(extensions=[BleachExtension(tags=bleach.ALLOWED_TAGS,
            attributes=bleach.ALLOWED_ATTRIBUTES, styles=bleach.ALLOWED_STYLES, strip=False, strip_comments=True)])

### Tag Whitelist

The ``tags`` kwarg is a whitelist of allowed HTML tags. It should be a list,
tuple, or other iterable. Any other HTML tags will be escaped or stripped from
the text.  Its default value is a relatively conservative list found in
``bleach.ALLOWED_TAGS``.

### Attribute Whitelist

The ``attributes`` kwarg is a whitelist of attributes. It can be a list, in
which case the attributes are allowed for any tag, or a dictionary, in which
case the keys are tag names (or a wildcard: ``*`` for all tags) and the values
are lists of allowed attributes.

For example::

    attrs = {
        '*': ['class'],
        'a': ['href', 'rel'],
        'img': ['src', 'alt'],
    }

In this case, ``class`` is allowed on any allowed element (from the ``tags``
argument), ``<a>`` tags are allowed to have ``href`` and ``rel`` attributes,
and so on.

The default value is also a conservative dict found in
``bleach.ALLOWED_ATTRIBUTES``.


#### Callable Filters

You can also use a callable (instead of a list) in the ``attributes`` kwarg. If
the callable returns ``True``, the attribute is allowed. Otherwise, it is
stripped. For example::

    def filter_src(name, value):
        if name in ('alt', 'height', 'width'):
            return True
        if name == 'src':
            p = urlparse(value)
            return (not p.netloc) or p.netloc == 'mydomain.com'
        return False

    attrs = {
        'img': filter_src,
    }

### Styles Whitelist

If you allow the ``style`` attribute, you will also need to whitelist styles
users are allowed to set, for example ``color`` and ``background-color``.

The default value is an empty list, i.e., the ``style`` attribute will be
allowed but no values will be.

For example, to allow users to set the color and font-weight of text::

    attrs = {
        '*': ['style']
    }
    tags = ['p', 'em', 'strong']
    styles = ['color', 'font-weight']

### Stripping Markup

By default, Bleach *escapes* disallowed or invalid markup. For example::

    >>> md = markdown.Markdown(extensions=[BleachExtension()])
    >>> md.convert('<span>is not allowed</span>')
    u'&lt;span&gt;is not allowed&lt;/span&gt;

If you would rather Bleach stripped this markup entirely, you can pass
``strip=True``::

    >>> md = markdown.Markdown(extensions=[BleachExtension(strip=True)])
    >>> md.convert('<span>is not allowed</span>')
    u'is not allowed'

### Stripping Comments

By default, Bleach will strip out HTML comments. To disable this behavior, set
``strip_comments=False``::

    >>> html = 'my<!-- commented --> html'

    >>> md = markdown.Markdown(extensions=[BleachExtension()])
    >>> md.convert(html)
    u'my html'

    >>> md = markdown.Markdown(extensions=[BleachExtension(strip_comments=False)])
    >>> md.convert(html)
    u'my<!-- commented --> html'

## Links

- [Source](https://github.com/Wenzil/python-markdown-bleach)
- [Bleach](http://bleach.readthedocs.org/en/latest/)
- [Markdown](http://daringfireball.net/projects/markdown/)
- [Python Markdown](https://pythonhosted.org/Markdown/)
