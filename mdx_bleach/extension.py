# -*- coding: utf-8 -*-
from markdown import Extension
from bleach import ALLOWED_TAGS, ALLOWED_ATTRIBUTES, ALLOWED_STYLES
from .postprocessors import BleachRawHtmlPostprocessor


class BleachExtension(Extension):

    def __init__(self, **kwargs):
        # set defaults
        self.config = {
            'tags': [
                ALLOWED_TAGS,
                "Whitelist of allowed HTML tags. It should be a list, tuple, "
                "or other iterable. Any other HTML tags will be escaped or "
                "stripped from the text. Its default value is a relatively "
                "conservative list found in bleach.ALLOWED_TAGS"
            ],
            'attributes': [
                ALLOWED_ATTRIBUTES,
                "Whitelist of attributes. It can be a list, in which case the "
                "attributes are allowed for any tag, or a dictionary, in which "
                "case the keys are tag names (or a wildcard: * for all tags) "
                "and the values are lists of allowed attributes. The default "
                "value is a conservative dict found in bleach.ALLOWED_ATTRIBUTES"
                "You can also use a callable (instead of a list). If the "
                "callable returns True, the attribute is allowed. Otherwise, it "
                "is stripped."
            ],
            'styles': [
                ALLOWED_STYLES,
                "If you allow the style attribute, you will also need to "
                "whitelist styles users are allowed to set, for example color "
                "and background-color. The default value is an empty list."
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
        strip = self.getConfig('strip', False)
        strip_comments = self.getConfig('strip_comments', True)

        md.postprocessors["raw_html"] = BleachRawHtmlPostprocessor(tags, attributes, styles, strip, strip_comments)
