import markdown.util
import bleach
from markdown.postprocessors import Postprocessor
from .whitelist import ALLOWED_TAGS, ALLOWED_ATTRIBUTES, ALLOWED_STYLES

class BleachRawHtmlPostprocessor(Postprocessor):
    """ Restore raw html to the document and sanitize it. """

    def __init__(self, md, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES,
                 styles=ALLOWED_STYLES, strip=False, strip_comments=True):
        self.markdown = md
        self.tags = tags
        self.attributes = attributes
        self.styles = styles
        self.strip = strip
        self.strip_comments = strip_comments

    def run(self, text):
        """ Iterate over html stash and restore and sanitize html """
        for i in range(self.markdown.htmlStash.html_counter):
            import pdb; pdb.set_trace()
            html, safe = self.markdown.htmlStash.rawHtmlBlocks[i]
            if not safe:
                html = bleach.clean(html, self.tags, self.attributes, self.styles, self.strip, self.strip_comments)
            if safe and self.isblocklevel(html):
                text = text.replace(
                    "<p>%s</p>" % (self.markdown.htmlStash.get_placeholder(i)),
                    html + "\n"
                )
            text = text.replace(
                self.markdown.htmlStash.get_placeholder(i), html
            )
        return text

    def isblocklevel(self, html):
        m = re.match(r'^\<\/?([^ >]+)', html)
        if m:
            if m.group(1)[0] in ('!', '?', '@', '%'):
                # Comment, php etc...
                return True
            return markdown.util.isBlockLevel(m.group(1))
        return False

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
