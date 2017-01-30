import bleach
from markdown.postprocessors import Postprocessor
from .whitelist import (
    ALLOWED_TAGS, ALLOWED_ATTRIBUTES, ALLOWED_STYLES, ALLOWED_PROTOCOLS
)
class BleachPostprocessor(Postprocessor):
    """ Sanitize the markdown output. """

    def __init__(self, md, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES,
                 styles=ALLOWED_STYLES, protocols=ALLOWED_PROTOCOLS,
                 strip=False, strip_comments=True):
        self.markdown = md
        self.tags = tags
        self.attributes = attributes
        self.styles = styles
        self.protocols = protocols
        self.strip = strip
        self.strip_comments = strip_comments

    def run(self, text):
        """ Sanitize the markdown output. """
        return bleach.clean(text,
                            tags=self.tags,
                            attributes=self.attributes,
                            styles=self.styles,
                            protocols=self.protocols,
                            strip=self.strip,
                            strip_comments=self.strip_comments
        )
