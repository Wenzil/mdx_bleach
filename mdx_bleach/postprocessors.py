import bleach
from markdown.postprocessors import Postprocessor
from .whitelist import ALLOWED_TAGS, ALLOWED_ATTRIBUTES, ALLOWED_STYLES

class BleachPostprocessor(Postprocessor):
    """ Sanitize the markdown output. """

    def __init__(self, md, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES,
                 styles=ALLOWED_STYLES, strip=False, strip_comments=True):
        self.markdown = md
        self.tags = tags
        self.attributes = attributes
        self.styles = styles
        self.strip = strip
        self.strip_comments = strip_comments

    def run(self, text):
        """ Sanitize the markdown output. """
        return bleach.clean(text, self.tags, self.attributes, self.styles, self.strip, self.strip_comments)
