import markdown.postprocessors
import markdown.util
from bleach import clean, ALLOWED_TAGS, ALLOWED_ATTRIBUTES, ALLOWED_STYLES

class BleachRawHtmlPostprocessor(Postprocessor):
    """ Restore raw html to the document and sanitize it. """

    def __init__(self, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES,
                 styles=ALLOWED_STYLES, strip=False, strip_comments=True):
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
                html = clean(html, self.tags, self.attributes, self.styles, self.strip, self.strip_comments)
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
