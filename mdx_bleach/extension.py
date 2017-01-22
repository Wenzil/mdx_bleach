# -*- coding: utf-8 -*-
from markdown import Extension
from .whitelist import (
    ALLOWED_TAGS, ALLOWED_ATTRIBUTES, ALLOWED_STYLES, ALLOWED_PROTOCOLS
)
from .postprocessors import BleachPostprocessor
from .exceptions import ImproperlyConfigured

class BleachExtension(Extension):

    def __init__(self, **kwargs):
        # set defaults
        self.config = {
            'tags': [
                ALLOWED_TAGS,
                "Whitelist of allowed HTML tags. It should be a list, tuple, "
                "or other iterable. Any other HTML tags will be escaped or "
                "stripped from the text. This applies to the html output that "
                "Markdown produces. The default value is a conservative list of "
                "tags found in mdx_bleach.whitelist.ALLOWED_TAGS."
            ],
            'attributes': [
                ALLOWED_ATTRIBUTES,
                "Whitelist of attributes. It can be a list, in which case the "
                "attributes are allowed for any tag, or a dictionary, in which "
                "case the keys are tag names (or a wildcard: * for all tags) "
                "and the values are lists of allowed attributes. The default "
                "value is a conservative dictionary of attribute lists found in "
                "mdx_bleach.whitelist.ALLOWED_ATTRIBUTES. You can also use a "
                "callable (instead of a list). If the callable returns True, "
                "the attribute is allowed. Otherwise, it is stripped."
            ],
            'styles': [
                ALLOWED_STYLES,
                "If you allow the style attribute, you will also need to "
                "whitelist styles authors are allowed to set, for example color "
                "and background-color. The default value is an empty list."
            ],
            'protocols': [
                ALLOWED_PROTOCOLS,
                "If you allow tags that have attributes containing a URI "
                "value  (like the href attribute of an anchor tag,) you may "
                "want to adapt the accepted protocols. The default list only "
                "allows http, https and mailto."
            ],
            'strip': [
                False,
                "By default, Bleach escapes disallowed or invalid markup. If "
                "you would rather Bleach stripped this markup entirely, you can "
                "pass strip=True"
            ],
            'strip_comments': [
                True,
                "By default, Bleach will strip out HTML comments. To disable "
                "this behavior, set strip_comments=False"
            ],
        }
        super(BleachExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md, md_globals):
        if md.safeMode:
            raise ImproperlyConfigured("Markdown's safe mode is not supported.")

        tags = self.getConfig('tags', ALLOWED_TAGS)
        attributes = self.getConfig('attributes', ALLOWED_ATTRIBUTES)
        styles = self.getConfig('styles', ALLOWED_STYLES)
        protocols = self.getConfig('protocols', ALLOWED_PROTOCOLS)
        strip = self.getConfig('strip', False)
        strip_comments = self.getConfig('strip_comments', True)

        bleach_pp = BleachPostprocessor(md, tags, attributes, styles,
                                        protocols, strip, strip_comments)
        md.postprocessors.add('bleach', bleach_pp, '>raw_html')
